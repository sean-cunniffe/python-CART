from unittest import TestCase
import TreeFactory

# Created By SEAN CUNNIFFE on 15/01/2021
from TreeComponents import Entity, Question, Node, Leaf


class Test(TestCase):

    def setUp(self) -> None:
        TreeFactory.no_columns = 3
        self.test_arr = [Entity(['Green', 3, 'Apple']), Entity(['Yellow', 3, 'Apple']), Entity(['Red', 1, 'Grape']),
                         Entity(['Red', 1, 'Grape']), Entity(['Yellow', 3, 'Lemon'])]

        self.test_arr2 = [Entity(['Yellow', 3, 'Apple']), Entity(['Red', 1, 'Grape']),
                          Entity(['Red', 1, 'Grape']), Entity(['Yellow', 3, 'Lemon'])]

    def test_find_best_question(self):
        test = TreeFactory.find_best_question(0.64, self.test_arr, 2)
        self.assertEqual(3, test.question[0])

    def test_get_unique_values(self):
        test = TreeFactory.get_unique_values(self.test_arr)
        self.assertEqual([{'Green': 1, 'Yellow': 2, 'Red': 2}, {3: 3, 1: 2}, {'Apple': 2, 'Grape': 2, 'Lemon': 1}],
                         test)

    def test_calculate_impurity(self):
        self.assertEqual(0.64, TreeFactory.calculate_impurity(self.test_arr, 2))
        self.assertEqual(0.625, TreeFactory.calculate_impurity(self.test_arr2, 2))

    def test_build_tree(self):
        node = TreeFactory.build_tree(self.test_arr, 2)
        self.assertTrue(isinstance(node.true_node, Node))
        self.assertTrue(isinstance(node.false_node, Leaf))

    def test_ask_question(self):
        test = TreeFactory.ask_question(self.test_arr[0], Question('Green', 1, 0, [], []))
        self.assertTrue(test)

        test = TreeFactory.ask_question(self.test_arr[0], Question('Red', 1, 0, [], []))
        self.assertFalse(test)

        test = TreeFactory.ask_question(self.test_arr[0], Question(3, 1, 1, [], []))
        self.assertTrue(test)

        test = TreeFactory.ask_question(self.test_arr[0], Question(4, 1, 1, [], []))
        self.assertFalse(test)

    def test_get_entities_from_csv_file(self):
        test: [] = TreeFactory.get_entities_from_csv_file('../hazelnut.csv')
        self.assertEqual(201, len(test))
