Here's the revised version of your project requirements and tasks for the User Authentication Service:

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

---
