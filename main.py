from TreeComponents import Node, Entity
import TreeFactory
import json

entities = TreeFactory.get_entities_from_csv_file('hazelnut.csv')

TreeFactory.no_columns = 12
# change for generalisation
TreeFactory.info_gain_threshold = 0

node: Node = TreeFactory.build_tree(entities, 11)
output = TreeFactory.categories_entity(
    Entity([71, 11.67, 12.8025, 8.055074738, 34.65, 1375.5, 0.93005, 19.145, 4.4604, 0.048667685, 0.175]), node)
print(output)

# dump tree to json file for angular application
with open('data.json', 'w') as outfile:
    json.dump(node.to_json(), outfile)
