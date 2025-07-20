from flask import Flask
import socket

app = Flask(__name__)

@app.route('/home')
def root():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return f"Hello, welcome to the DevOps world! Hostname: {hostname}, IP Address: {ip}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

