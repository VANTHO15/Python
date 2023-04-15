import sqlite3
db=sqlite3.connect("school.sql")
db.execute("DROP TABLE IF EXISTS student")
db.execute("CREATE TABLE student (id INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , name VARCHAR)")

db.execute("INSERT INTO student (name) VALUES ('Nguyễn Văn Thọ')")
db.execute("INSERT INTO student (name) VALUES ('Nguyễn Văn A')")
db.execute("INSERT INTO student (name) VALUES ('Nguyễn Văn B')")
db.execute("INSERT INTO student (name) VALUES ('Nguyễn Văn C')")
db.commit()  # hoàn thành

dulieu=db.execute("SELECT * FROM student")
for i in dulieu:
    print(i)
db.execute("UPDATE student SET name= \"Nguyễn Thị Bảo yến\" WHERE id=2")
dulieu=db.execute("SELECT * FROM student")
for i in dulieu:
    print(i)