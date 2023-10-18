#!/usr/bin/env python3

from common import get_pat, HttpClient
import sys
import csv

if 2 != len(sys.argv):
    print('Usage: %s CSV_FILENAME' % (sys.argv[0]))
    exit(1)

csv_filename = sys.argv[1]

# Create a structure where buildings are categorized by property designation
properties = {}
with open(csv_filename) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    # Skip header row
    next(reader, None)

    for row in reader:
        building_name = row[0]
        property_designation = row[1]
        property_area = row[2]
        property_classification_year = row[3]
        property_energy_class = row[4]

        if not property_designation in properties:
            properties[property_designation] = {
                'classification_year': property_classification_year,
                'energy_class': property_energy_class,
                'property_area': property_area,
                'buildings': [],
            }
        properties[property_designation]['buildings'].append(building_name)

METRY_PAT = get_pat()
client = HttpClient(METRY_PAT)

# Get root node ID to put properties under
root_node_response = client.get('/api/2.0/trees?parent=null')
root_node_id = root_node_response.body_dict['data'][0]['_id']

for property_designation, property_data in properties.items():
    property_response = client.post('/api/2.0/trees', {
        'parent': root_node_id,
        'name': property_designation,
        'type': 'property',
        'property': {
            'property_designation': property_designation,
            'energy_class': property_data['energy_class'],
            'energy_classification_year': property_data['classification_year'],
            'area': property_data['property_area'],
        },
    })
    # Get property node ID to put buildings under
    property_node_id = property_response.body_dict['data']['_id']
    # Create buildings under their properties
    for building_name in property_data['buildings']:
        property_response = client.post('/api/2.0/trees', {
            'parent': property_node_id,
            'name': building_name,
            'type': 'building',
            'building': {
                'address': building_name,
            },
        })
