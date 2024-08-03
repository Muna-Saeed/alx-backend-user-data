#!/usr/bin/env python3
"""
 End-to-end integration test
"""

import requests


BASE_URL = "http://localhost:5000"  # Adjust this to your server's base URL


def register_user(email: str, password: str) -> None:
    """Test user registration."""
    response = requests.post(
     f"{BASE_URL}/users", data={"email": email, "password": password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login with incorrect password."""
    response = requests.post(
     f"{BASE_URL}/sessions", data={"email": email, "password": password})
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Test login with correct credentials and return session ID."""
    response = requests.post(
     f"{BASE_URL}/sessions", data={"email": email, "password": password})
    assert response.status_code == 200
    assert "session_id" in response.cookies
    return response.cookies["session_id"]


def profile_unlogged() -> None:
    """Test accessing profile without login."""
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Test accessing profile with a valid session ID."""
    response = requests.get(
     f"{BASE_URL}/profile", cookies={"session_id": session_id})
    assert response.status_code == 200
    assert response.json() == {"email": EMAIL}


def log_out(session_id: str) -> None:
    """Test logout."""
    response = requests.delete(
     f"{BASE_URL}/sessions", cookies={"session_id": session_id})
    assert response.status_code == 302  # Redirect status code


def reset_password_token(email: str) -> str:
    """Request a reset password token."""
    response = requests.post(
     f"{BASE_URL}/reset_password", data={"email": email})
    assert response.status_code == 200
    return response.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update the password using the reset token."""
    response = requests.put(
     f"{BASE_URL}/reset_password", data={
      "email": email, "reset_token": reset_token,
      "new_password": new_password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
