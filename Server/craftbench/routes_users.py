import helpers
from flask import request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import jwt

from main import app

# Signup route!
@app.route("/users/create", methods=["POST"])
def users_create():
    if helpers.check_username_exists(request.json.get("username")):
        return jsonify({
            "success": False,
            "msg": "That username already exists."
        }), 400
    if helpers.create_new_user({
        "username": request.json.get("username"),
        "password_hash": generate_password_hash(request.json.get("password")),
        "name": request.json.get("name"),
        "email": request.json.get("email")
    }):
        return jsonify({
            "success": True,
            "msg": "Successfully created user."
        }), 201
    else: 
        return jsonify({
            "success": False,
            "msg": "An internal error occurred, retry later."
        }), 500

# Login route!
@app.route("/users/login", methods=["POST"])
def users_login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = helpers.user_by_username(username)

    if not user["success"]: return jsonify({
        "success": False,
        "msg": "Username doesn't exist."
    }), 400

    if not check_password_hash(user["user"]["data"]["password_hash"], password): return jsonify({
        "success": False,
        "msg": "Username and password don't match"
    }), 401


    return jsonify({
        "success": True,
        "token": jwt.encode(
            { "id": user["user"]["ref"].id() }, 
            app.config["JWT_SECRET_KEY"], 
            algorithm="HS256"
        ).decode()
    }), 201

# Check username
@app.route("/users/exists_by_username/<username>", methods=["GET"])
def users_exists_by_username(username):
    return jsonify({
        "success": True,
        "exists": helpers.check_username_exists(username)
    }), 200

