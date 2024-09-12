from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sqlalchemy


app = Flask(__name__)

CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

db = sqlalchemy.create_engine(
    "mariadb+pymysql://root:@localhost:3306/userdb", echo=True
    )


@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/register", methods=["POST"])
@cross_origin()
def register():
    data = request.get_json()
    
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    
    register_new_user_to_db(username, password, email)
    
    return jsonify({"message": "Registration was succesful"}), 200    
    

def get_users():
    with db.connect() as conn:
        result = conn.execute(sqlalchemy.text("SELECT * FROM users;"))
        print(result.all())
        




def register_new_user_to_db(username, password, eamil):
    with db.connect() as conn:
        result = conn.execute(
            sqlalchemy.text(
                """
                INSERT INTO users (id, username, password, email)
                VALUES (NULL,  :username, :password, :email)
                """
            ),
            {
                "username": username,
                "password": password,
                "email": eamil,
            },
            
        )
        conn.commit()  


if __name__=="__main__":
    app.run(port=5001, debug=True)