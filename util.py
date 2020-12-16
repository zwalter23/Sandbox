# Helper functions which can be called from any other layer
import connection
import time
import csv


def field_separator():
    with open("sample_data/question.csv", "r") as field_search:
        lines = field_search.readlines()
        fields = []
        for row in lines:
            fields.append(row)
        return fields[0]


def questions_separator():
    with open("sample_data/question.csv", "r") as field_search:
            lines = field_search.readlines()
            details = []
            for row in lines:
                line_breaker = row.strip("\n'")
                new_list = line_breaker.split(", ")
                details.append(new_list)
            return details[1::]


def question_counter(details):
    count = 0
    for amount in details:
        count += 1
    return count
    

def time_stamper():
    return int(time.time())


def id_generator():
    new_id = 0
    for i in questions:
        new_id += 1
    return (new_id+1)

fields = field_separator() # Gets the headers
questions = questions_separator()
question_count = question_counter(questions) # Counts the questions
actual_time = time_stamper() # Gets Unix timestamp
new_id = id_generator() # Generates new id