# Safe Code Executor

A safe Python code execution API with a simple web UI. Runs untrusted Python code in a secure Docker sandbox.

---

## Features

- Runs Python code safely in Docker
- Enforces:
  - **Network disabled** (`--network none`)
  - **Memory limit** (`128MB`)
  - **CPU limit** (`0.5 cores`)
  - **Read-only filesystem**
  - **Execution timeout** (10 seconds)
  - **Max code length** (5000 characters)
- Simple web UI for testing code
- Returns output or error messages clearly

---

## Requirements

- Python 3.11+
- Flask
- Docker installed

---

## Setup

1. Clone the project
2. Create a Python virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy code
pip install flask
Run the app:

bash
Copy code
python3 app.py
Usage
Open your browser:

cpp
Copy code
http://127.0.0.1:5000/
Type Python code and click Run Code. Output will appear below.

API Example
POST /run
Request Body:

json
Copy code
{
  "code": "print(2+2)"
}
Response:

json
Copy code
{
  "output": "4\n"
}
Security Measures
--network none: Prevents internet access

--memory=128m: Limits memory usage

--cpus=0.5: Limits CPU usage

--read-only: Prevents writing to container filesystem

timeout=10: Stops infinite loops

MAX_CODE_LENGTH=5000: Prevents very large code

What I Learned
Docker isolates code execution

Containers can protect your system from untrusted code

Some files inside the container can still be read

Memory, CPU, network, and filesystem limits prevent crashes or attacks

Optional Enhancements
Add support for JavaScript (Node.js)

Syntax highlighting in UI

History of executed code

Run multiple containers in parallel

Use a non-root user and custom seccomp profile

yaml
Copy code

---

# ✅ **Next Steps**

1. Make sure your **Docker daemon is running**  
2. Run the server:

```bash
python3 app.py
Open browser → http://127.0.0.1:5000/

Test:

Normal code (print("Hello"))

Infinite loop (while True: pass)

Large memory allocation (x = "a"*1000000000)

Network access (import requests# project-docker
