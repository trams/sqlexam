#!/usr/bin/python2

import sqlite3

def main():
  database = sqlite3.connect("/tmp/s1")
  cursor = database.cursor()

  cursor.execute("create table people\
      (\
      id integer primary key,\
      name varchar(30) not null,\
      sex varchar(1)\
      );")

  cursor.execute("insert into people values (1, 'Alice', 'w');");
  cursor.execute("insert into people values (2, 'Bob', 'm');");
  cursor.execute("insert into people values (3, 'Alex', 'm');");
  cursor.execute("insert into people values (4, 'Dima', 'm');");
  cursor.execute("insert into people values (5, 'Masha', 'w');");
  database.commit()

if __name__ == '__main__':
  main()

