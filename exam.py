#!/usr/bin/python2

import sqlite3

def load_data():
  def add_line(string):
    if string is None:
      return ""
    else:
      return string + "\n"

  data = {}
  id = None
  desc = None
  solution = None

  id_state, desc_state, sol_state = range(3)

  f = open("tasks.dat", 'r');
  state = id_state
  for line in f:
    clean_line = line.strip(" \n")

    if state == id_state:
      id = clean_line
      state = desc_state
    elif state == desc_state:
      if clean_line == "":
        state = sol_state
      else:
        desc = add_line(desc)
        desc += clean_line
    elif state == sol_state:
      if clean_line == "":
        data[id] = (desc, solution)
        id = None
        desc = None
        solution = None
        state = id_state
      else:
        solution = add_line(solution)
        solution += clean_line
    else:
      pass

  return data

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
