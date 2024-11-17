# Vulnerable API for Security Testing

This project is a simple Flask API designed to demonstrate common web security vulnerabilities, including:

1. **Unrestricted Resource Consumption**
2. **Server-Side Request Forgery (SSRF)**
3. **Security Misconfiguration**
4. **Unsafe Consumption of APIs**

This project is intended for educational purposes to help students and security engineers learn how vulnerabilities work and how they can be exploited in real-world applications.

---

## API Endpoints

### 1. **Unrestricted Resource Consumption**
- **Vulnerability**: The server allows users to upload large files without any restrictions, potentially leading to Denial of Service (DoS) by over-consuming resources.
- **Description**: The server accepts file uploads via the `POST` request and responds with the size of the uploaded file.

#### **How to Test via `curl`**
- **POST Request** (Upload a file):
  ```bash
  curl -X POST http://127.0.0.1:5000/unrestricted \
       -F "file=@example.txt"
This command uploads a file (example.txt) to the server.

- **GET Request** (Request previously uploaded file):
  ```bash
  curl -X GET "http://127.0.0.1:5000/unrestricted"
This command retrieves the uploaded file.

### 2. Server-Side Request Forgery (SSRF)
- **Vulnerability**: The server makes HTTP requests to external URLs provided by users without validating or sanitizing the URL, potentially allowing attackers to send malicious requests to internal resources.
- **Description**: The server will send a request to any URL provided by the user, including potentially dangerous internal URLs.

#### **How to Test via `curl`**
- **GET Request** (Send a request to an external URL):
  ```bash
  curl -X GET "http://127.0.0.1:5000/ssrf?url=http://127.0.0.1:5000/secret"
This command sends a request to an internal service (/secret).

### 3. Security Misconfiguration
- **Vulnerability**: The server exposes sensitive environment variables, such as PATH, when requested by users, potentially leaking private configuration data.
- **Description**: The server returns environment variables when queried with a specific variable name, revealing sensitive information.

#### **How to Test via `curl`**
- **GET Request** (Fetch a specific environment variable, e.g., PATH):

  ```bash
  curl "http://127.0.0.1:5000/misconfig?env=PATH"
This command retrieves the PATH environment variable.

- **GET Request** (Fetch all environment variables):

  ```bash
  curl "http://127.0.0.1:5000/misconfig"
This command retrieves all environment variables stored on the server.

### 4. Unsafe Consumption of APIs
- **Vulnerability**: The server consumes data from external APIs provided by users without validating or sanitizing the URLs, potentially allowing attackers to access internal services or malicious external APIs.
- **Description**: The server makes an HTTP POST request to an external API provided by the user and returns the response.

#### **How to Test via `curl`**
- **POST Request** (Consume an external API):
  ```bash
  curl -X POST http://127.0.0.1:5000/unsafe-consume \
       -H "Content-Type: application/json" \
       -d '{"api_url": "https://httpbin.org/post", "payload": {"key": "value"}}'
This command sends a POST request to httpbin.org and returns the response.

## How to Run the Vulnerable API
- Clone the repository:

  ```bash
  git clone https://github.com/Jonah-gr/unsafe-api.git
  cd unsafe-api
  
- Install dependencies: Make sure you have Python and pip installed. Then install the required dependency:

  ```bash
  pip install Flask

- Run the Flask application:

  ```bash
  python api.py
By default, the application will run at http://127.0.0.1:5000/.

Test the vulnerabilities: Use the provided curl commands in a bash shell to test each vulnerability.
