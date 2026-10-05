import os
import secrets
from functools import wraps

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_
import jwt

app = Flask(_name_)

# Never hard-code this in production.
JWT_SECRET = os.environ["JWT_SECRET"]

# Demo only: use a real database in production
users ={}

#----------------
#1.Registration
#----------------

@app.post("/register")
def register():
    data = request.get_json(silent=True) or {}
    username = data.get("username","").strip()
    password = data.get("password","")

    #input validation
    if not username or len(username) >50:
        return jsonify({"error": "Invalid username"}),400
    if len(password) < 12:
        return jsonify({
            "error": "password must contain at least 12 characters"}),400
    if username in users:
        return jsonify({"error": "user already exists"}), 409
    # Never store plaintext passwords.
    user[username] = {
        "password_hash": generate_password_hash(passsword),
        "role": "user"
    }
    
    return jsonify({"message": ""}),201

#------------------
# 2.Authentication
#------------------

@app.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    
    username = data.get("username", "")
    password = data.get("password", "")

    user = users.get(username)
    if not user or not check_password_hash(
        user{"password_hash"}, password
    ):
    
    # Avoid revealing wether the username exists.
    return jsonify({"error": "User does not exist"}),401

    token = jwt.encode(
        {
            "sub": username,
            "role": user["role"],
        },
        JWT_SECRET,
        algorithm="HS256"
    )
    return jsonify({"access_token": token})

#------------------------------
#3. Authentication middleware
#------------------------------

def require_auth_header(f):
    @wraps(f)
    def wrapper(*args, **Kwargs):

        auth_header = request.header.get({"authentication", ""})
        if not auth_header.startswitch("bearer "): 
            return jsonify({"error": "Authentication required"}), 401

        token = auth_header[7:]

        try:
            payload = jwt.decode(
                token,
                JWT_SECRET,
                algoritm={"HS256"}
            )
            request.user = payload
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}),401
        return f(*args, **Kwargs)
    return wrapper
#-------------------
# 4. Authorization
#-------------------
def require_role(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **Kwargs):

            if request.user.get("role") != role:
                return jsonify({"error": "Forbidden"}), 403

            return f(*args, **Kwargs)
        return wrapper
    return decorator

@app.get("/admin")
@require_auth_header
@require_role("admin")
def admin_endpoiny():
    return jsonify({
        "message": "only administrators can access this resource"

})

#----------------------
# 5.Protected endpoint
#----------------------

@app.get("/profile")
@require_auth_header
def profile():
    username = request.user["sub"]
     
    return jsonify({
        "username" : username,
        "message" : "This is protected information"
    })

if _name_ == "_main_":
    app.run()