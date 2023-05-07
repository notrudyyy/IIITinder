from flask import Flask, request, jsonify, make_response
import logging, json
import sqlite3
import sys
import os

try:
    os.remove("users.db")
except OSError:
    pass

class DBclass:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(self.path, check_same_thread=False)
        self.cur = self.db.cursor()
    def execute(self, query, values=None):
        if values == None:
            self.cur.execute(query)
        else:
            self.cur.execute(query, values)
        if self.cur.description != None:
            return [i[0] for i in self.cur.description], self.cur.fetchall()
        else:
            return None
    def commit(self):
        self.db.commit()
user_db = DBclass("users.db")

user_db.execute("""CREATE TABLE IF NOT EXISTS users 
                    (user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                     first_name VARCHAR(50), last_name VARCHAR(50), 
                     age INT, 
                     phone_no INT, 
                     email VARCHAR(100),
                     password VARCHAR(100),
                     hostel VARCHAR(20),
                     desc VARCHAR(500),
                     lang VARCHAR(20),
                     floor VARCHAR(5),
                     sleep VARCHAR(5),
                     env VARCHAR(5),
                     guest VARCHAR(5),
                     branch VARCHAR(5),
                     hobby VARCHAR(50),
                     nonveg VARCHAR(5),
                     clean VARCHAR(5),
                     UNIQUE(email))""")

user_db.commit()

print(user_db.execute("SELECT * FROM users"), file=sys.stderr)

user_db.execute(""" INSERT INTO users( 
                     first_name, last_name, 
                     age, 
                     phone_no, 
                     email,
                     password,
                     hostel,
                     desc ,
                     lang,
                     floor ,
                     sleep,
                     env ,
                     guest ,
                     branch,
                     hobby ,
                     nonveg ,
                     clean ) VALUES(
    "Ananya","Madireddy",18,1234567890,"ananya@gmail.com","123456","parijat-a","i am introverted kid likes to stay alone","tel",3,1,1,1,"cse","playing badminton",1,2

)
""")

user_db.commit()

user_db.execute(""" INSERT INTO users(
    first_name, last_name, 
                     age, 
                     phone_no, 
                     email,
                     password,
                     hostel,
                     desc ,
                     lang,
                     floor ,
                     sleep,
                     env ,
                     guest ,
                     branch,
                     hobby ,
                     nonveg ,
                     clean ) VALUES(
    "asdfg","Madireddi",18,6248446123,"asdfg@gmail.com","drthfs","parijat-a","like to mingle","tel",3,1,1,1,"csd","playing badminton",2,1

)
""")

user_db.commit()

user_db.execute(""" INSERT INTO users(
    first_name, last_name, 
                     age, 
                     phone_no, 
                     email,
                     password,
                     hostel,
                     desc ,
                     lang,
                     floor ,
                     sleep,
                     env ,
                     guest ,
                     branch,
                     hobby ,
                     nonveg ,
                     clean ) VALUES(
    "roshan","naik",19,9734652454,"roshan@gmail.com","grgjheyufb","bakul","like to stay outdoors mostly","hin",2,1,1,2,"cse","playing basketball cricket",1,1

)
""")    
user_db.commit()
user_db.execute(""" INSERT INTO users(
    first_name, last_name, 
                     age, 
                     phone_no, 
                     email,
                     password,
                     hostel,
                     desc ,
                     lang,
                     floor ,
                     sleep,
                     env ,
                     guest ,
                     branch,
                     hobby ,
                     nonveg ,
                     clean ) VALUES(
    "anirudh","vempati",18,2354668643,"notruddy@gmail.com","sfshfh","bakul","i love helping ,and i am considerate towards others","eng",1,1,1,1,"chd","coding",1,2

)
""")
user_db.commit()
user_db.execute(""" INSERT INTO users(
    first_name, last_name, 
                     age, 
                     phone_no, 
                     email,
                     password,
                     hostel,
                     desc ,
                     lang,
                     floor ,
                     sleep,
                     env ,
                     guest ,
                     branch,
                     hobby ,
                     nonveg ,
                     clean ) VALUES(
    "dileep","kumar",18,9873751234,"dileep@gmail.com","dipppad","bakul","sfdttr ffgf dfdtde vcbgdd fdf","tel",2,3,1,2,"cse","watching movies",2,1

)
""")    
user_db.commit()
user_db.execute(""" INSERT INTO users(
    first_name, last_name, 
                     age, 
                     phone_no, 
                     email,
                     password,
                     hostel,
                     desc ,
                     lang,
                     floor ,
                     sleep,
                     env ,
                     guest ,
                     branch,
                     hobby ,
                     nonveg ,
                     clean ) VALUES(
    "laasya","inala",18,7823573635,"laasya@gmail.com","3552fdfg","parijat-b","i am introverted kid likes to stay alone","mall",1,2,2,1,"ece","chess and readig books",1,2

)
""") 
user_db.commit()
user_db.execute(""" INSERT INTO users(
    first_name, last_name, 
                     age, 
                     phone_no, 
                     email,
                     password,
                     hostel,
                     desc ,
                     lang,
                     floor ,
                     sleep,
                     env ,
                     guest ,
                     branch,
                     hobby ,
                     nonveg ,
                     clean ) VALUES(
    "prashanth","venkata",19,1267686823,"pv@gmail.com","efjgdvdg","obh","loves explaoring the nature","hin",2,1,1,2,"ece","riding and teaching",2,2

)
""")  
user_db.commit()
user_db.execute(""" INSERT INTO users(
    first_name, last_name, 
                     age, 
                     phone_no, 
                     email,
                     password,
                     hostel,
                     desc ,
                     lang,
                     floor ,
                     sleep,
                     env ,
                     guest ,
                     branch,
                     hobby ,
                     nonveg ,
                     clean ) VALUES(
    "rohan","naidu",18,8465962356,"rohan@gmail.com","sdgsdg","obh","i love doing research","mall",2,1,1,2,"csd","reading books",2,2

)
""")
user_db.commit()
user_db.execute(""" INSERT INTO users(
    first_name, last_name, 
                     age, 
                     phone_no, 
                     email,
                     password,
                     hostel,
                     desc ,
                     lang,
                     floor ,
                     sleep,
                     env ,
                     guest ,
                     branch,
                     hobby ,
                     nonveg ,
                     clean ) VALUES(
    "nishita","kannan",18,9566356665,"nishita@gmail.com","dfhshhf","parijat-a","i am introverted kid likes to stay alone and i always receive people with smile","tam",1,1,1,1,"cse","reading books",1,1

)
""")
user_db.commit()

print(user_db.execute("SELECT * FROM users"), file=sys.stderr)