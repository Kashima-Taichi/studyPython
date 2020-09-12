import sqlite3

conn = sqlite3.connect('test_sqlite.db')

curs = conn.cursor()

# curs.execute(
#     'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
# )
# conn.commit()

# curs.execute(
#     'INSERT INTO persons(name) values("Mike")'
# )
# conn.commit()

# curs.execute('SELECT * FROM persons')
# print(curs.fetchall())

# curs.execute(
#     'INSERT INTO persons(name) values("Nancy")'
# )
# curs.execute(
#     'INSERT INTO persons(name) values("Jun")'
# )
# conn.commit()

curs.close()
conn.close()
