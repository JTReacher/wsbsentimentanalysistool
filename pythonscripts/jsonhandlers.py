
import json
import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="test_db"
)


#TODO: Rewrite this
def dump_jsonl(data, output_path, append=False):
    """
    Write list of objects to a JSON lines file.
    """
    mode = 'a+' if append else 'w'
    with open(output_path, mode, encoding='utf-8') as f:
        for line in data:
            json_record = json.dumps(line, ensure_ascii=False)
            f.write(json_record + '\n')
    print('Wrote {} records to {}'.format(len(data), output_path))

# Extracts every key present in the JSON file for formatting SQL columns
def extract_json_keys(path):
    json_keys = []
    with open(path, 'r', encoding='utf-8') as jsonfile:
        for line in jsonfile:
            try:
                json_data = json.loads(line.rstrip('\n|\r'))
            except:
                continue
            for key in json_data.keys():
                if key not in json_keys:
                  json_keys.append(key)
    return json_keys

#Checks how many jsonlines are malformed in file and lists line indexes
def find_malformed_lines(path):
    malformed_lines_counter = 0
    malformed_lines_indexes = []
    counter = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            counter += 1
            try:
              json_data = json.loads(line.rstrip('\n|\r'))
            except:
                malformed_lines_counter += 1
                malformed_lines_indexes.append(counter)
                continue
    print(malformed_lines_counter, malformed_lines_indexes)
    return(malformed_lines_indexes)

# Extracts each json line from the jsonlines file as python dictionaries and then stores them in a list
def extract_jsonl(path):
    jsonlist = []
    with open(path, 'r', encoding='utf-8') as jsonlfile:
        for line in jsonlfile:
            try:
                jsonlist.append(json.loads(line.rstrip('\n|\r')))
            except:
              continue
    return jsonlist


def json_to_df(path):

    #with open(path, 'r', encoding='utf-8') as jsonlfile:
    #1. Open big file as json object
    #2. create a write file
    #3. iterate big file and copy to new file
    #4. when new file length is 2000 create dataframe

    


    
    pass






