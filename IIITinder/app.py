
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
                     clean VARCHAR(5))""")

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

# print(user_db.execute("SELECT * FROM users"), file=sys.stderr)



user_db.commit()

def insert_into_db(inputdata):
    check = user_db.execute("SELECT * FROM users WHERE email = '"+inputdata["email"].strip()+"'")
    if check[1] != []:
        print(check, file=sys.stderr)
        return {"success":"false"}
    query = """
        INSERT INTO users (
            first_name,
            last_name,
            age,
            phone_no,
            email,
            password
        ) VALUES (?, ?, ?, ?, ?, ?)
    """
    values = (
        inputdata["first_name"],
        inputdata["last_name"],
        inputdata["age"],
        inputdata["phone_no"],
        inputdata["email"],
        inputdata["password"]
    )
    user_db.execute(query, values)
    user_db.commit()
    print(user_db.execute("SELECT * FROM users"), file=sys.stderr)
    return {"success":"true"}

def get_matches_from_db(hostel):
    matchdata = user_db.execute("SELECT * FROM users WHERE hostel=\'"+str(hostel["hostel"])+"\'")
    matchdict = {"matches":[], "success":"true"}
    for i in matchdata[1]:
        newdict={}
        newdict["first_name"]=i[1]
        newdict["last_name"]=i[2]
        newdict["age"]=i[3]
        newdict["number"]=i[4]
        newdict["email"]=i[5]
        newdict["hostel"]=i[7]
        newdict["desc"]=i[8]
        newdict["lang"]=i[9]
        newdict["floor"]=i[10]
        newdict["sleep"]=i[11]
        newdict["env"]=i[12]
        newdict["guests"]=i[13]
        newdict["branch"]=i[14]
        newdict["hobby"]=i[15]
        newdict["non-veg"]=i[16]
        newdict["room-desc"]=i[17]
        matchdict["matches"].append(newdict)
    return matchdict

def log_user_in(userdata):
    check = user_db.execute("SELECT * FROM users WHERE email=\'"+str(userdata["email"])+"\' AND password=\'"+str(userdata["password"])+"\'")
    if check == None:
        userdne = {"success":"false"}
        return userdne
    else:
        userdata = check[1][0]
        userdat = {"success":"true", "first_name": userdata[1],
            "last_name": userdata[2],
            "age" : str(userdata[3]),
            "number" : str(userdata[4]),
            "email" : userdata[5],
            "hostel": userdata[6],
            "desc": userdata[7],
            "lang": userdata[8],
            "floor": userdata[9],
            "sleep": userdata[10],
            "env": userdata[11],
            "guests": userdata[12],
            "branch": userdata[13],
            "hobby": userdata[14],
            "non-veg": userdata[15],
            "room-desc": userdata[16]}
        return userdat

def update_user_data(userdata):
    query = """
        UPDATE users SET
            hostel = ?,
            desc = ?,
            lang = ?,
            floor = ?,
            sleep = ?,
            env = ?,
            guest = ?,
            branch = ?,
            hobby = ?,
            nonveg = ?,
            clean = ? 
        WHERE email = ?
    """
    values = (
        userdata["hostel"],
        userdata["desc"],
        userdata["lang"],
        userdata["floor"],
        userdata["sleep"],
        userdata["env"],
        userdata["guest"],
        userdata["branch"],
        userdata["hobby"],
        userdata["nonveg"],
        userdata["clean"],
        userdata["email"]
    )
    user_db.execute(query, values)
    user_db.commit()
    print(user_db.execute("SELECT * FROM users"), file=sys.stderr)
    return {"success":"true"}

app = Flask(__name__)

@app.route("/auth-signup", methods=['POST', "OPTIONS"])
def parse_request():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "POST": # The actual request following the preflight
        retdata = insert_into_db(dict(request.json))
        return _corsify_actual_response(jsonify(retdata))
    else:
        raise RuntimeError("Don't know how to handle method {}".format(request.method))
    
@app.route("/auth-login", methods=['POST', "OPTIONS"])
def auth_login():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "POST": # The actual request following the preflight
        retdata = log_user_in(dict(request.json))
        return _corsify_actual_response(jsonify(retdata))
    else:
        raise RuntimeError("Don't know how to handle method {}".format(request.method))
    
@app.route("/auth-update", methods=['POST', "OPTIONS"])
def auth_update():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "POST": # The actual request following the preflight
        retdata = update_user_data(dict(request.json))
        return _corsify_actual_response(jsonify(retdata))
    else:
        raise RuntimeError("Don't know how to handle method {}".format(request.method))

@app.route("/get-matches", methods=['POST', "OPTIONS"])
def return_matches():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "POST": # The actual request following the preflight
        matchdata = get_matches_from_db(dict(request.json))
        return _corsify_actual_response(jsonify(matchdata))
    else:
        raise RuntimeError("Don't know how to handle method {}".format(request.method))

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
 
app.run(host='localhost',port=5000, debug=True)