
import json
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
import jq
import os
from yahoo_fin import stock_info as si

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
    return(path, malformed_lines_indexes)

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

##############################

# TODO: Count malformed lines with jq
def count_malformed(path):


    pass
#1. TODO: Function to handle malformed lines in file using jq
def remove_malformed_json_jq():
        
    pass

#2. Function to push a dataframe to MySQL as a new record from a JSONLines file
#Does not filter dataframe (I filtered in notebook using an edited version of this function. See data manipulation.py)
def df_to_SQL(fileobject):
    sql_Engine = create_engine('mysql+pymysql://mysql:mysql@localhost:3306/test_db')
    db_connection = sql_Engine.connect()
    df = pd.read_json(fileobject, lines=True)
    df.to_sql(con=db_connection, name="RedditPosts", if_exists="append")
    db_connection.close()

#Iterate every file in directory
def iterate_split_Jsons(path):
    for filename in os.listdir('/workspace/JSONFiles/submissionsSplit/'):
        df_to_SQL(filename)

def fetch_df_from_SQL():
    SQL_Engine = create_engine('mysql+pymysql://mysql:mysql@localhost:3306/test_db')
    db_connection = SQL_Engine.connect()

    #request data from mysql and store as dataframe
    # limit it to 100,000 records at a time.

    #pd.read_sql - Params - SQL (string of SQL or sqlalchemy selectable)  
    # con = sql connection




    pass


#TODO:
def extract_tickers(dataframe):



    pass




#TODO:
def extract_company_name(dataframe):

    pass

#TODO:
def df_to_SQL_existing(dataframe):

    pass


#TODO: rewrite this code
#This provides 11,000 stock tickers. Probably covers what we need?
def get_all_tickers_yahoo_finance():
    df1 = pd.DataFrame(si.tickers_sp500())
    df2 = pd.DataFrame(si.tickers_nasdaq())
    df3 = pd.DataFrame(si.tickers_dow())
    df4 = pd.DataFrame(si.tickers_other())
    sym1 = set(symbol for symbol in df1[0].values.tolist())
    sym2 = set(symbol for symbol in df2[0].values.tolist())
    sym3 = set(symbol for symbol in df3[0].values.tolist())
    sym4 = set(symbol for symbol in df4[0].values.tolist())
    symbols = set.union(sym1, sym2, sym3, sym4)
    return symbols



#What am I passing it? Pass it a dataframe that's already been called, write something else to handle the requests
# 


