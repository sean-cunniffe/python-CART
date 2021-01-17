import TreeComponents
import TreeFactory
import json

entities = TreeFactory.get_entities_from_csv_file('hazelnut.csv')

TreeFactory.no_columns = 12
node: TreeComponents.Node = TreeFactory.build_tree(entities, 11)

#dump tree to json file for angular application
with open('data.json', 'w') as outfile:
    json.dump(node.to_json(), outfile)
