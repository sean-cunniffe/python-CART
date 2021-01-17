# Created By SEAN CUNNIFFE on 15/01/2021
import json
from typing import Dict


class Node:

    def __init__(self, true_node, false_node, question):
        self.true_node = true_node
        self.false_node = false_node
        # question to ask at this node
        self.question: Question = question

    def to_json(self):
        # f'"true_node": {self.true_node.to_json()}, "false_node": {self.false_node.to_json()}, question:' \
        #        f'{self.question.to_json()}'
        return dict(true_node=self.true_node.to_json(), false_node=self.false_node.to_json(),
                    question=self.question.to_json())


class Leaf:

    def __init__(self, data_set: [{}], label_index: int):
        self.data_set: [{}] = data_set
        self.label_index = label_index

    def to_json(self):
        return self.__dict__

    @property
    def confidence(self) -> str:
        return_str: str = ''
        total_rows: int = 0
        for data in self.data_set[self.label_index].items():
            total_rows += data[1]

        for data in self.data_set[self.label_index].items():
            return_str += f'{data[0]}: {data[1] * 100 / total_rows}% confidence\n'
        return return_str


class Question:

    def __init__(self, question, info_gain, column_index: int, true_dataset: [], false_dataset: []):
        # question to ask, either a number or string
        self.question: any = question
        # question value of question
        self.info_gain = info_gain
        # column index of data to check question_value against
        self.column_index: int = column_index
        self.true_dataset = true_dataset
        self.false_dataset = false_dataset

    def to_json(self) -> dict:
        # return f'"question": {self.question}, "info_gain": {self.info_gain}, "column_index": '\
        #        f'{self.column_index}, "true_dataset": {self.true_dataset}'
        return dict(question=self.question, info_gain=self.info_gain, column_index=self.column_index)


class Entity:

    def __init__(self, rows: []):
        # row of data with x amount of columns representing entity
        self.rows: [] = rows

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return self.__dict__
