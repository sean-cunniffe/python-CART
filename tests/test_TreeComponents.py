from unittest import TestCase
import json

# Created By SEAN CUNNIFFE on 16/01/2021
from TreeComponents import Leaf, Entity


class Test(TestCase):
    def test_leaf(self):
        data_set = [{'red': 2}, {'green': 2}, {0: 1, 5: 1}, {-1: 1, 2: 1}, {2: 2}, {0: 2}, {'orange': 2},
                    {'apple': 2, 'banana': 1, 'lemon': 1}]
        leaf = Leaf(data_set, 7)

        json_str = json.dumps(leaf.to_json())
        print(json_str)
        self.assertEqual(
            '{"data_set": [{"red": 2}, {"green": 2}, {"0": 1, "5": 1}, {"-1": 1, "2": 1}, {"2": 2}, {"0": 2}, '
            '{"orange": 2}, {"apple": 2, "banana": 1, "lemon": 1}], "label_index": 7}'
            , json_str)

    def test_entity(self):
        entity = Entity(['Green', 3, 'Apple'])
        json_str = json.dumps(entity.__repr__())
        self.assertEqual('{"rows": ["Green", 3, "Apple"]}', json_str)

