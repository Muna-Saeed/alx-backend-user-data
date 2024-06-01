# Personal Data Protection

This project focuses on implementing security measures to protect personal data in a Python application. It covers hashing passwords, filtering sensitive information, and securely connecting to a database.

## Table of Contents

- [Task 0: Regex-ing](#task-0-regex-ing)
- [Task 1: Log formatter](#task-1-log-formatter)
- [Task 2: Create logger](#task-2-create-logger)
- [Task 3: Connect to secure database](#task-3-connect-to-secure-database)
- [Task 4: Read and filter data](#task-4-read-and-filter-data)
- [Task 5: Encrypting passwords](#task-5-encrypting-passwords)
- [Task 6: Check valid password](#task-6-check-valid-password)
- [Description](#description)
- [Features](#features)
- [Files](#files)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Task 0: Regex-ing

Write a function called `filter_datum` that returns the log message obfuscated using regular expressions. The function should replace occurrences of certain field values based on a provided list of fields and a redaction string.

```python
#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
```

## Task 1: Log formatter

Implement a log formatter class called `RedactingFormatter` that accepts a list of fields constructor argument. The formatter should filter values in incoming log records using the `filter_datum` function.

```python
#!/usr/bin/env python3
"""
Main file
"""

import logging

RedactingFormatter = __import__('filtered_logger').RedactingFormatter

message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))
```

## Task 2: Create logger

Implement a function called `get_logger` that returns a `logging.Logger` object named "user_data". The logger should only log up to `logging.INFO` level and should have a StreamHandler with `RedactingFormatter` as formatter.

```python
#!/usr/bin/env python3
"""
Main file
"""

import logging

get_logger = __import__('filtered_logger').get_logger

logger = get_logger()
logger.info("Information message")
logger.error("Error message")
```

## Task 3: Connect to secure database

Implement a function called `get_db` that returns a connector to a MySQL database. Use environment variables to obtain credentials for database connection.

```python
#!/usr/bin/env python3
"""
Main file
"""

get_db = __import__('filtered_logger').get_db

db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()
```

## Task 4: Read and filter data

Implement a main function that retrieves all rows from the users table in the database and logs each row under a filtered format.

```python
#!/usr/bin/env python3
"""
Main file
"""

main = __import__('filtered_logger').main

main()
```

## Task 5: Encrypting passwords

Implement a function called `hash_password` that takes a password string as input and returns a salted, hashed password as a byte string using bcrypt.

```python
#!/usr/bin/env python3
"""
Main file
"""

hash_password = __import__('encrypt_password').hash_password

password = "MyAmazingPassw0rd"
print(hash_password(password))
```

## Task 6: Check valid password

Implement a function called `is_valid` that takes a hashed password (bytes) and a plaintext password (string) as input and returns a boolean indicating whether the plaintext password matches the hashed password.

```python
#!/usr/bin/env python3
"""
Main file
"""

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(is_valid(encrypted_password, password))
```

## Description

In this project, we implement several functionalities to ensure the security of personal data within a Python application. This includes:

- **Hashing Passwords**: Securely hash passwords using the bcrypt algorithm to prevent storing plaintext passwords in the database.
- **Filtering Sensitive Information**: Implement logging functionalities to filter sensitive information (such as passwords, SSNs) before logging to files.
- **Secure Database Connection**: Connect to a secure database using environment variables to protect sensitive database credentials.
- **Validating Passwords**: Check if a provided password matches a hashed password securely using bcrypt.

## Features

- Hash passwords securely using bcrypt.
- Filter sensitive information before logging.
- Connect to a secure database using environment variables.
- Validate passwords against their hashed counterparts securely.

## Files

- `encrypt_password.py`: Contains functions to hash and validate passwords using bcrypt.
- `filtered_logger.py`: Implements functionalities to filter sensitive information before logging.
- `main.py`: Main file to demonstrate the usage of implemented functionalities.
- `README.md`: Documentation for the project.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Muna-Saeed/alx-backend-user-data.git
   ```

2. Navigate to the project directory:

   ```bash
   cd personal-data-protection
   ```

3. Run the main file to see the implemented functionalities in action:

   ```bash
   ./main.py
   ```

## Dependencies

This project requires the following dependencies:

- Python 3
- bcrypt
- mysql-connector-python

You can install the required packages using pip:

```bash
pip install bcrypt mysql-connector-python
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
