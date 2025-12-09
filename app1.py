from flask import Flask, request, jsonify
import subprocess
import uuid
import os

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_code():
    # Ensure JSON
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({"error": "No code provided"}), 400

    code = data['code']

    # Limit code length
    if len(code) > 5000:
        return jsonify({"error": "Code too long"}), 400

    # Save code to temporary file
    filename = f"temp_{uuid.uuid4().hex}.py"
    with open(filename, 'w') as f:
        f.write(code)

    try:
        # Run code safely (timeout 5 sec, capture output)
        result = subprocess.run(
            ['python3', filename],
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        output = None
        return jsonify({"error": "Execution timed out"}), 408
    finally:
        # Remove temp file
        os.remove(filename)

    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
