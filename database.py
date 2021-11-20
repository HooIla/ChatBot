import sqlite3
import json
from datetime import datetime
from sqlite3.dbapi2 import Connection


timeframe = '2012-12'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)")

if __name__ == '__main__':
    create_table()
    row_counter = 0
    paired_row = 0

    with open("C:/Users/alyyy52/Downloads/{}".format(timeframe),buffer=1000)

