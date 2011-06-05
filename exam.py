#!/usr/bin/python2

import sqlite3

def is_equal(user_result, good_result):
  return frozenset(user_result) == frozenset(good_result)

def get_select_results(cursor, query):
  cursor.execute(query)
  return cursor.fetchall()

user_query = "select * from messages where user_from = (select id from people where name = 'Alice');"

good_queries = [
  "select * from messages where user_from = '1'",
  "select distinct p.name from people p, messages m\
   where (p.id = m.user_from) or (p.id = m.user_to)",
  "select select p.name, COUNT(p.name) from people p, messages m\
  where (p.id = m.user_from)\
  group by p.name;"
];
  
def main():
  database = sqlite3.connect("/tmp/s1")
  cursor = database.cursor()
  user_result = get_select_results(cursor, user_query);
  good_result = get_select_results(cursor, good_queries[0]);

  print is_equal(user_result, good_result)

if __name__ == '__main__':
  main()
