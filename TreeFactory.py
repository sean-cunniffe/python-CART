# Created By SEAN CUNNIFFE on 15/01/2021

from TreeComponents import Entity, Question, Node, Leaf

# no of columns in entity
no_columns: int
info_gain_threshold: int = 0


def build_tree(dataset: [], label_column_index):
    impurity = calculate_impurity(dataset, label_column_index)
    question = find_best_question(impurity, dataset, label_column_index)
    if question.info_gain == info_gain_threshold:
        return Leaf(get_unique_values(dataset), label_column_index)

    return Node(
        build_tree(question.true_dataset, label_column_index), build_tree(question.false_dataset, label_column_index),
        question)


def categories_entity(entity, starting_node: Node):
    current_node: any = starting_node

    # keep going till we get a leaf
    while current_node is not isinstance(current_node, Leaf):
        if ask_question(entity, current_node.question):
            current_node = current_node.true_node
        else:
            current_node = current_node.false_node


def ask_question(entity: Entity, question: Question) -> bool:
    # check if question is a str or int
    if isinstance(question.question, str):
        return question.question == entity.rows[question.column_index]
    else:
        return question.question <= entity.rows[question.column_index]


def find_best_question(previous_impurity: float, dataset: [Entity], label_column_index) -> Question:
    # To find the best question look at each attribute of each row
    # find every unique value and then the gini of it
    top_question: Question = Question(None, None, 0, [], [])
    top_info_gain: float = 0
    # get unique values in columns so we dont check the same values multiple times
    unique_values: [] = get_unique_values(dataset)
    for i in range(no_columns - 1):
        # check all columns but the label_column
        if i is not label_column_index:
            for value in unique_values[i].items():
                # split dataset from value
                split_dataset: [[Entity]] = split_data(dataset, value[0], i)
                # calculate impurity of split dataset
                impurity1_wa = calculate_impurity(split_dataset[0], label_column_index) * (
                        len(split_dataset[0]) / len(dataset))
                impurity2_wa = calculate_impurity(split_dataset[1], label_column_index) * (
                        len(split_dataset[1]) / len(dataset))
                # get weighted average
                w_avg_impurity = (impurity2_wa + impurity1_wa)
                temp_info_gain = previous_impurity - w_avg_impurity
                if temp_info_gain >= top_info_gain:
                    top_info_gain = temp_info_gain
                    top_question = Question(value, top_info_gain, i, split_dataset[0], split_dataset[1])
    return top_question


# calculate the impurity based on the label_column_index
def calculate_impurity(dataset: [Entity], label_column_index) -> float:
    unique_values: [{any: int}] = get_unique_values(dataset)
    calc: float = 0
    for value in unique_values[label_column_index].items():
        prob = value[1] / len(dataset)
        calc = calc + (prob * (1 - prob))
    return calc


# list of columns->[map of values with their count->{key-> label_value: value-> count_of_label}]
def get_unique_values(dataset: [Entity]) -> [{any: int}]:
    attribute_values = []
    for i in range(no_columns):
        attribute_values.append({})

    # Go through entities to get unique values of each column
    for entity in dataset:
        # go through each column of row in Entity
        for col_index in range(0, no_columns):
            # get value of entity attribute
            att_value = entity.rows[col_index]
            # check if the value already exists, if not then add it
            if attribute_values[col_index].get(att_value) is None and att_value is not None:
                # unique value isn't added yet, add it
                attribute_values[col_index][att_value] = 1
            elif att_value is not None:
                # unique value exists, increment count of unique
                attribute_values[col_index][att_value] += 1
    return attribute_values


def split_data(dataset: [Entity], value: any, col_index) -> [[Entity]]:
    if isinstance(value, str):
        return split_data_str(dataset, value, col_index)
    else:
        return split_data_int(dataset, value, col_index)


def split_data_str(dataset: [Entity], value: str, col_index) -> [[Entity]]:
    true_data = []
    false_data = []
    for data in dataset:
        if data.rows[col_index] is value:
            true_data.append(data)
        else:
            false_data.append(data)
    return [true_data, false_data]


def split_data_int(dataset: [Entity], value: int, col_index) -> [[Entity]]:
    true_data = []
    false_data = []
    for data in dataset:
        if data.rows[col_index] >= value:
            true_data.append(data)
        else:
            false_data.append(data)
    return [true_data, false_data]


def get_entities_from_csv_file(file_path) -> []:
    f = open(file_path)
    entities: [] = []
    while True:
        line = f.readline()
        if line == '':
            break
        line = line.replace('\n', '').replace('ï»¿', '')
        attributes: [] = line.split(",")
        entity: Entity = Entity([])
        for att in attributes:
            try:
                entity.rows.append(float(att))
            except ValueError:
                entity.rows.append(att)
        entities.append(entity)
    f.close()
    return entities
