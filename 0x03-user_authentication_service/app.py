#!/usr/bin/env python3
"""
basic Flask app
"""
from flask import Flask, request, jsonify
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """Login user and create session"""
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Log out the user by destroying their session."""
    session_id = request.cookies.get('session_id')

    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            response = redirect('/')
            response.delete_cookie('session_id')
            return response
        else:
            abort(403)
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """Return the user's profile based on session_id."""
    session_id = request.cookies.get('session_id')

    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email})

    abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Handle POST request to /reset_password to generate a reset token."""
    email = request.form.get('email')

    if email is None:
        abort(400, description="Missing email parameter")

    try:
        # Generate reset token
        reset_token = auth.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        # If email is not registered
        abort(403, description="Email not registered")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
