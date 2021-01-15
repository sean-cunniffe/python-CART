# Created By SEAN CUNNIFFE on 15/01/2021

class Node:

    def __init__(self, children_nodes: [], question):
        # two children that this node leads to. Can be either a node or leaf
        self.children_node: [] = children_nodes
        # question to ask at this node
        self.question = question
        # specifies if the node is a leaf
        self.is_leaf: bool = False
        if len(children_nodes) <= 0:
            self.is_leaf = True


class Leaf:

    def __init__(self, confidence: float):
        self.confidence = confidence


class Question:

    def __init__(self, question_value, column_index: int):
        # question value of question
        self.question_value = question_value
        # column index of data to check question_value against
        self.column_index: int = column_index


class Entity:

    def __init__(self, rows: []):
        # row of data with x amount of columns representing entity
        self.rows: [] = rows
