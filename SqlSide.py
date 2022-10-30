import csv
import sqlite3




db = sqlite3.connect("UsersData.db")

c = db.cursor()

c.execute("DROP TABLE IF EXISTS user_interests")
c.execute("DROP TABLE IF EXISTS user")
c.execute("DROP TABLE IF EXISTS interests")

c.execute("""CREATE TABLE IF NOT EXISTS user(
user_ID integer primary key autoincrement,
first_name text not null,
last_name text not null, 
age integer not null,
company text not null
)""")

c.execute("""CREATE TABLE IF NOT EXISTS interests(
interest_ID integer primary key autoincrement,
interest_name text not NULL
)""")


c.execute("""CREATE TABLE IF NOT EXISTS user_interests(
user_ID integer not NULL references user (user_ID),
interest_ID integer not null references interests(interest_ID),
primary key (user_ID, interest_ID)
)
""")
c.execute("INSERT INTO interests (interest_name) VALUES('книги'),('спорт'),('пиво'),('футбол')")
c.execute("""INSERT INTO user (first_name,last_name,age,company) VALUES('Вася','Жопин',17,'Яндекс'),
('Иван','Ручкин',18,'Сбер'),
('Анатолий','Ноготочки', 30,'twiiter')""")
c.execute("INSERT INTO user_interests (user_ID,interest_ID) values(3,1),(3,3),(1,2),(1,4)")
c.execute("SELECT interest_name FROM interests")

def add_to_db(first_name,last_name,age,company,interest,interests):
    global c
    c.execute(f"INSERT INTO user(first_name,last_name,age,company) VALUES(?,?,?,?)",
              (first_name, last_name, age, company))
    c.execute(f"INSERT INTO user(first_name,last_name,age,company) VALUES(?,?,?,?)",
              (first_name, last_name, age, company))
    user = c.execute("SELECT last_insert_rowid()").fetchone()
    print(user)
    for inter in interests:
        int_id = c.execute(f"SELECT interest_ID ,interest_name FROM interests WHERE interest_name = ?", (inter,))
        interest = c.fetchone()
        if interest is None:
            c.execute(f"INSERT INTO interests('interest_name') VALUES(?)", (inter,))
        int_id = c.execute(f"SELECT interest_ID ,interest_name FROM interests WHERE interest_name = ?", (inter,))
        interest = int_id.fetchone()
        # c.execute(f"INSERT INTO user_interests(user_ID,'interest_ID') VALUES(?,?)",(user[0], interest[0],))
        c.execute(f"INSERT INTO user_interests(user_ID,'interest_ID') VALUES(?,?)", (user[0], interest[0],))




'''

'''
db.commit()
db.close()
