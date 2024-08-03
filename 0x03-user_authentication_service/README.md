Here's the project requirements and tasks for the User Authentication Service:

---

**0x03. User Authentication Service**  
*Back-end*  
*Authentication*  
**Weight:** 1  
**Project Over:** Took place from Jun 10, 2024, 6:00 AM to Jun 14, 2024, 6:00 AM  
**Auto Review:** Launched at the deadline  

**In a Nutshell…**  
- **Auto QA Review:** 0.0/89 mandatory & 0.0/4 optional  
- **Altogether:** 0.0%  
- **Mandatory:** 0.0%  
- **Optional:** 0.0%  
- **Calculation:** 0.0% + (0.0% * 0.0%) = 0.0%

**Overview:**  
In the industry, it's recommended to use existing modules or frameworks for authentication (like Flask-User in Python-Flask). For learning purposes, you will build an authentication system from scratch to understand the process.

**Resources:**  
- Flask Documentation
- Requests Module
- HTTP Status Codes

**Learning Objectives:**  
By the end of this project, you should be able to:
- Declare API routes in a Flask app
- Get and set cookies
- Retrieve request form data
- Return various HTTP status codes

**Requirements:**
- Allowed editors: vi, vim, emacs
- Files interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- Files should end with a newline
- First line of all files should be `#!/usr/bin/env python3`
- A `README.md` file is mandatory at the root of the project folder
- Code should adhere to the `pycodestyle` style (version 2.5)
- Use SQLAlchemy 1.3.x
- All files must be executable
- The length of files will be tested using `wc`
- Modules, classes, and functions should be documented
- All functions should be type-annotated
- Flask app should only interact with `Auth` and not directly with the DB

**Setup:**  
You will need to install `bcrypt`:
```bash
pip3 install bcrypt
```

---

### Tasks

**0. User Model**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Create a SQLAlchemy model named `User` for a database table named `users`. The model should have the following attributes:
- `id`: Integer primary key
- `email`: Non-nullable string
- `hashed_password`: Non-nullable string
- `session_id`: Nullable string
- `reset_token`: Nullable string

**File:** `user.py`

**1. Create User**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement the `add_user` method in the `DB` class. This method should save a user to the database and return a `User` object. The method takes two required string arguments: `email` and `hashed_password`.

**File:** `db.py`

**2. Find User**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement the `find_user_by` method in the `DB` class. This method should take arbitrary keyword arguments and return the first row found in the `users` table matching the input arguments. Handle `NoResultFound` and `InvalidRequestError` exceptions as specified.

**File:** `db.py`

**3. Update User**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement the `update_user` method in the `DB` class. This method takes a required `user_id` integer and arbitrary keyword arguments to update the user's attributes in the database.

**File:** `db.py`

**4. Hash Password**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Define a `_hash_password` method that takes a password string and returns a salted hash using `bcrypt.hashpw`.

**File:** `auth.py`

**5. Register User**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement the `register_user` method in the `Auth` class. This method should register a user with an email and password, handle existing users, and hash the password before saving.

**File:** `auth.py`

**6. Basic Flask App**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Set up a basic Flask app with a single GET route ("/") returning a JSON payload: `{"message": "Bienvenue"}`. Run the app on `0.0.0.0` port `5000`.

**File:** `app.py`

**7. Register User Endpoint**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement the POST `/users` route in Flask to register a user. Handle user creation and error responses appropriately.

**File:** `app.py`

**8. Credentials Validation**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement the `valid_login` method in the `Auth` class to validate user credentials.

**File:** `auth.py`

**9. Generate UUIDs**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement a `_generate_uuid` function in the `auth` module to return a string representation of a new UUID.

**File:** `auth.py`

**10. Get Session ID**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement the `create_session` method in the `Auth` class to generate and return a new session ID for a user.

**File:** `auth.py`

**11. Log In**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement the POST `/sessions` route in Flask to handle user login, set session cookies, and respond with appropriate JSON payloads and status codes.

**File:** `app.py`

**12. Find User by Session ID**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement the `get_user_from_session_id` method in the `Auth` class to find a user by session ID.

**File:** `auth.py`

**13. Destroy Session**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)  
Implement the `destroy_session` method in the `Auth` class to handle session destruction and logout functionality.

**File:** `auth.py`

**14. Log Out**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

In this task, you will implement a logout function to respond to the `DELETE /sessions` route.

**Requirements:**
- The request is expected to contain the session ID as a cookie with the key `session_id`.
- Find the user with the requested session ID.
- If the user exists, destroy the session and redirect the user to `GET /`.
- If the user does not exist, respond with a 403 HTTP status.

**Repo:**  
- **GitHub repository:** alx-backend-user-data  
- **Directory:** 0x03-user_authentication_service  
- **File:** app.py

---

**15. User Profile**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

In this task, you will implement a profile function to respond to the `GET /profile` route.

**Requirements:**
- The request is expected to contain a `session_id` cookie.
- Use it to find the user. If the user exists, respond with a 200 HTTP status and the following JSON payload:

  ```json
  {"email": "<user email>"}
  ```

- If the session ID is invalid or the user does not exist, respond with a 403 HTTP status.

**Repo:**  
- **GitHub repository:** alx-backend-user-data  
- **Directory:** 0x03-user_authentication_service  
- **File:** app.py

---

**16. Generate Reset Password Token**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

In this task, you will implement the `Auth.get_reset_password_token` method. It takes an email string argument and returns a string.

**Requirements:**
- Find the user corresponding to the email.
- If the user does not exist, raise a `ValueError` exception.
- If it exists, generate a UUID and update the user’s `reset_token` database field. Return the token.

**Repo:**  
- **GitHub repository:** alx-backend-user-data  
- **Directory:** 0x03-user_authentication_service  
- **File:** auth.py

---

**17. Get Reset Password Token**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

In this task, you will implement a `get_reset_password_token` function to respond to the `POST /reset_password` route.

**Requirements:**
- The request is expected to contain form data with the "email" field.
- If the email is not registered, respond with a 403 status code.
- Otherwise, generate a token and respond with a 200 HTTP status and the following JSON payload:

  ```json
  {"email": "<user email>", "reset_token": "<reset token>"}
  ```

**Repo:**  
- **GitHub repository:** alx-backend-user-data  
- **Directory:** 0x03-user_authentication_service  
- **File:** app.py

---

**18. Update Password**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

In this task, you will implement the `Auth.update_password` method. It takes a `reset_token` string argument and a `password` string argument and returns `None`.

**Requirements:**
- Use the `reset_token` to find the corresponding user.
- If the user does not exist, raise a `ValueError` exception.
- Otherwise, hash the password and update the user’s `hashed_password` field with the new hashed password and the `reset_token` field to `None`.

**Repo:**  
- **GitHub repository:** alx-backend-user-data  
- **Directory:** 0x03-user_authentication_service  
- **File:** auth.py

---

**19. Update Password Endpoint**  
**Mandatory**  
**Score:** 0.0% (Checks completed: 0.0%)

In this task, you will implement the `update_password` function in the app module to respond to the `PUT /reset_password` route.

**Requirements:**
- The request is expected to contain form data with fields "email", "reset_token", and "new_password".
- Update the password. If the token is invalid, catch the exception and respond with a 403 HTTP code.
- If the token is valid, respond with a 200 HTTP code and the following JSON payload:

  ```json
  {"email": "<user email>", "message": "Password updated"}
  ```

**Repo:**  
- **GitHub repository:** alx-backend-user-data  
- **Directory:** 0x03-user_authentication_service  
- **File:** app.py

---

**20. End-to-End Integration Test**  
**Advanced**  
**Score:** 0.0% (Checks completed: 0.0%)

Start your app. Open a new terminal window.

Create a new module called `main.py`. Create one function for each of the following tasks. Use the `requests` module to query your web server for the corresponding end-point. Use `assert` to validate the response’s expected status code and payload (if any) for each task.

- `register_user(email: str, password: str) -> None`
- `log_in_wrong_password(email: str, password: str) -> None`
- `log_in(email: str, password: str) -> str`
- `profile_unlogged() -> None`
- `profile_logged(session_id: str) -> None`
- `log_out(session_id: str) -> None`
- `reset_password_token(email: str) -> str`
- `update_password(email: str, reset_token: str, new_password: str) -> None`

Then copy the following code at the end of the `main` module:

```python
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
```

Run `python main.py`. If everything is correct, you should see no output.

**Repo:**  
- **GitHub repository:** alx-backend-user-data  
- **Directory:** 0x03-user_authentication_service  
- **File:** main.py

---
