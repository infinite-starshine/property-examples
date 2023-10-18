# Property Examples

Examples on how to use properties and buildings within Metry's tree structure.

## Scripts

### is-feature-enabled.py

Check if your account has the property and building feature enabled.
If you don't have it enabled, you'll be met with a 400 status code when you try to use it.

```sh
export METRY_PAT=myprivateaccesstoken
./is-feature-enabled.py
```

### get-root-node.py

Prints the ID of the root node of your account. This is the absolute top of the tree structure.
Use this ID as a parent ID if you want to create a tree node as high up as possible.
Not setting it can result in an unstable tree structure.

```sh
export METRY_PAT=myprivateaccesstoken
./get-root-node.py
```

### create-property-node.py

Create a property node with some dummy data.
The parent node ID could be the root node ID, or any generic tree node.
Property nodes can't exist under other property nodes, or under building nodes.

```sh
export METRY_PAT=myprivateaccesstoken
./create-property-node.py myparentnodeid
```

### create-building-node.py

Create a building node with some dummy data.

```sh
export METRY_PAT=myprivateaccesstoken
./create-building-node.py myparentnodeid
```

### import-from-csv.py

Example of how to read a set of properties and buildings from a CSV and create a tree structure out of it in Metry.

```sh
export METRY_PAT=myprivateaccesstoken
./import-from-csv.py byggnader.csv
```

### list-properties.py

List all properties on your account along with their ID and property designations.

```sh
export METRY_PAT=myprivateaccesstoken
./list-properties.py
```

### search-property.py

Example of how to search in Metry for properties based on their data.

```sh
export METRY_PAT=myprivateaccesstoken
./search-property.py energy_class B
./search-property.py property_designation 'VÄRNAMO BORGAREN 13'
./search-property.py energy_classification_year 2018
```

