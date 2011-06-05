#!/usr/bin/python2

import sqlite3

def is_equal(user_result, good_result):
  return frozenset(user_result) == frozenset(good_result)

def get_select_results(cursor, query):
  cursor.execute(query)
  return cursor.fetchall()
  
def main():
  user_query = "select * from people;"
  good_query = "select * from people where sex = 'w';"

  database = sqlite3.connect("/tmp/s1")
  cursor = database.cursor()
  user_result = get_select_results(cursor, user_query);
  good_result = get_select_results(cursor, good_query);

  print is_equal(user_result, good_result)

if __name__ == '__main__':
  main()
