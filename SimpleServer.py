import time
from pythonping import ping
from flask import Flask
import threading

app = Flask(__name__)

def check_dns_servers():
    dns_servers = ['1.1.1.1', '8.8.8.8']
    while True:
        for dns_server in dns_servers:
            ping(dns_server, verbose = True, count = 2)
        time.sleep(5)

@app.route('/health')
def health_check():
    return 'OK', 200

@app.route('/')
def start():
    return 'OK', 200

if __name__ == '__main__':
    flask_thread = threading.Thread(target=check_dns_servers)
    flask_thread.start()
    app.run(debug=True, port=8080, host='0.0.0.0')