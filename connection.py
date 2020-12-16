# Common functions to read/write/append CSV files without feature specific knowledge.
# The layer that have access to any kind of long term data storage.


import csv

def question_reader():
    with open('sample_data/question.csv', 'r') as questions:
        reader = csv.reader(questions)
        lined_questions = []
        for row in reader:
            lined_questions.append(row)
        return lined_questions


def question_writer():
    with open('sample_data/question.csv', 'w') as questions:
        reader = csv.write(questions)
    return reader


def answer_reader():
    pass


def answer_writer():
    pass
