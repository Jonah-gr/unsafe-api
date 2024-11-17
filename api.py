from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
content = ''

# Unrestricted Resource Consumption (e.g., no rate limiting or file size restrictions)
@app.route('/unrestricted', methods=['GET', 'POST'])
def unrestricted_resource():
    global content
    if request.method == 'GET':
        return content, 200

    elif request.method == 'POST':
        # Accepts a large file upload with no restriction
        file = request.files.get('file')
        if file:
            content = file.read()  # Read file without size validation
            return jsonify({"message": "File received", "size": len(content)}), 200
        else:
            return jsonify({"error": "No file provided"}), 400


# Server Side Request Forgery (SSRF)
@app.route('/ssrf', methods=['GET'])
def ssrf():
    target_url = request.args.get('url')
    if target_url:
        # Directly fetches the target URL without validation
        response = requests.get(target_url)
        return jsonify({
            "status_code": response.status_code,
            "content": response.text[:200]  # Limit the content shown for demo
        }), 200
    return jsonify({"error": "URL parameter is required"}), 400

@app.route('/secret', methods=['GET'])
def secret():
    return jsonify({"message": "This is a secret message"}), 200

# Security Misconfiguration
@app.route('/misconfig', methods=['GET'])
def security_misconfig():
    all_env_vars = dict(os.environ)
    env_var = request.args.get('env')
    if env_var:
        # value = os.getenv(env_var, "Environment variable not set")
        value = all_env_vars.get(env_var)
        return jsonify({env_var: value}), 200
    else:
        all_env_vars = dict(os.environ)
        return jsonify(all_env_vars), 200


# Unsafe Consumption of APIs
@app.route('/unsafe-consume', methods=['POST'])
def unsafe_consumption():
    # Consumes data from external APIs without sanitization
    data = request.get_json()
    external_api = data.get('api_url')
    if external_api:
        # Fetch data from the provided external API
        response = requests.post(external_api, json=data.get('payload', {}))
        return jsonify({
            "external_api_response": response.json()
        }), 200
    return jsonify({"error": "api_url is required in the payload"}), 400


if __name__ == '__main__':
    app.run(debug=True)
