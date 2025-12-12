**Safe Code Executor - Learning Project**

Overview

Safe Code Executor is a learning project that demonstrates how to safely run user-submitted Python and JavaScript code inside Docker containers. The goal is to provide an API and simple frontend that executes code securely while preventing resource abuse and malicious actions.

Users can submit code through:

API (POST /run)

Frontend UI (HTML page with textarea and Run button)

Outputs are returned safely without compromising the host system.

Features
Run Python and JavaScript (Node.js) code inside isolated Docker containers.
Prevent untrusted code from crashing the system:
Timeout after 10 seconds
Memory limit 128MB
Network disabled
Optional read-only filesystem
Simple frontend to test code execution.

Clear output and error reporting.

Project Structure
safe-code-executor/
├── backend/
│   ├── app.py           # Flask API
│   └── index.html       # Frontend UI
└── runner/
    ├── python/
    │   └── Dockerfile   # Python container
    └── node/
        ├── run.js       # Node.js runner
        └── Dockerfile.node  # Node.js container

Setup Instructions
1. Prerequisites

Python 3.11+ installed

<img width="1286" height="117" alt="image" src="https://github.com/user-attachments/assets/eeeb4f3b-9f87-4a92-894f-97d1314c182e" />


Docker installed and running

Flask installed:
 <img width="1390" height="287" alt="image" src="https://github.com/user-attachments/assets/bb107b22-9e15-4e26-a569-223c6e7004ba" />

pip install flask


Optional: Postman or curl for API testing.

2. Build Docker Images
Node.js Container
docker build -t node-runner -f runner/node/Dockerfile.node .

Python Container
docker build -t python-runner -f runner/python/Dockerfile .

3. Run the Flask Backend
cd backend
python app.py


Server runs at: http://127.0.0.1:5000

4. Open Frontend

Open browser: http://127.0.0.1:5000

Features:

Language selection (Python / Node.js)

Code textarea
<img width="613" height="295" alt="image" src="https://github.com/user-attachments/assets/65a4c90d-0ccf-4776-b8b8-599260f19812" />

Run button

Output display

API Usage
Endpoint
POST /run

Request Body
{
  "language": "python",
  "code": "print(2 + 2)"
}
<img width="1376" height="729" alt="image" src="https://github.com/user-attachments/assets/ef46e843-2e9e-4dde-b0ac-8febe70bc668" />


Response
{
  "output": "4\n",
  "error": ""
}


Replace "language": "python" with "node" for JavaScript execution.

Example curl
curl -X POST http://127.0.0.1:5000/run \
-H "Content-Type: application/json" \
-d '{"language":"python","code":"print(5*5)"}'

Security Measures Implemented

Timeout: Container stops after 10 seconds.

<img width="704" height="515" alt="image" src="https://github.com/user-attachments/assets/e3a68e58-6877-471e-8a04-abbea1abac42" />

Memory limit: 128MB per execution.

Network isolation: --network none prevents internet access.

Optional read-only filesystem: Prevent writing to host files.

Execution in Docker containers: Provides sandboxing.

Testing

Test your system with malicious or heavy code:


<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/bf06104e-038e-4084-82e3-25a7b34db9a5" />

Infinite loop:

while True:
    pass


→ Should terminate after timeout.

Memory heavy:

x = "a" * 1000000000


→ Container dies safely.

Network access attempt:

import requests
print(requests.get("http://google.com").text)


→ Fails due to network restriction.

Filesystem write test:

with open("/tmp/test.txt","w") as f:
    f.write("hello")
<img width="689" height="558" alt="image" src="https://github.com/user-attachments/assets/f5db5583-3ad2-4945-bc53-e6d9c4ee0b1b" />


→ Fails if --read-only is enabled.

Learning Outcomes

By completing this project, you will understand:

How to run code inside Docker containers from an API

Why running untrusted code is dangerous

Basic Docker security features: timeouts, memory limits, network isolation

Limits of Docker security

How to document and present a project
