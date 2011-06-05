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

  cursor.execute("create table messages\
  (\
  id integer primary key,\
  message varchar(250) NOT NULL,\
  user_from integer references people,\
  user_to integer references people\
  );")

  cursor.execute("create table friendship\
  (\
  fid integer primary key,\
  first_user integer references people,\
  second_user integer references people,\
  check (first_user < second_user)\
  );")

  cursor.execute("insert into people values (1, 'Alice', 'w');");
  cursor.execute("insert into people values (2, 'Bob', 'm');");
  cursor.execute("insert into people values (3, 'Alex', 'm');");
  cursor.execute("insert into people values (4, 'Dima', 'm');");
  cursor.execute("insert into people values (5, 'Masha', 'w');");

  cursor.execute("insert into messages values (1, 'Hello', 1, 2);")
  cursor.execute("insert into messages values (3, 'Would you like to have a cup of coffee', 1, 2);")
  cursor.execute("insert into messages values (4, 'Will you go to db lessons?', 2, 3);")
  cursor.execute("insert into messages values (5, 'No', 3, 2);")
  cursor.execute("insert into messages values (6, 'But why?', 2, 3);")

  cursor.execute("insert into friendship values (1, 2, 3);")
  cursor.execute("insert into friendship values (2, 2, 5);")
  cursor.execute("insert into friendship values (3, 3, 4);")
  cursor.execute("insert into friendship values (4, 4, 5);")

  database.commit()

if __name__ == '__main__':
  main()

