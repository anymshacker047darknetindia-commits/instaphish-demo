
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime
import json
import os

HOST = "0.0.0.0"
PORT = 8000

# Fixed sample credential for local demonstration
DEMO_USERNAME = "demo_user"
DEMO_PASSWORD = "DEMO-1234"

LOG_FILE = "logs/log.txt"


def to_binary(value):
    return " ".join(
        format(byte, "08b")
        for byte in value.encode("utf-8")
    )


def write_log(username, status):
    timestamp = datetime.now().isoformat(timespec="seconds")
    binary = to_binary(DEMO_PASSWORD)

    entry = (
        f"Time: {timestamp}\n"
        f"Username: {username}\n"
        f"Status: {status}\n"
        f"Demo Password Binary: {binary}\n"
        f"{'-' * 45}\n"
    )

    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(entry)

    print(entry, flush=True)


class DemoHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        if self.path != "/demo-login":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))

        if length > 4096:
            self.send_error(413)
            return

        data = json.loads(self.rfile.read(length))

        username = str(data.get("username", ""))[:64]
        demo_code = str(data.get("demo_code", ""))[:64]

        if username == DEMO_USERNAME and demo_code == DEMO_PASSWORD:
            status = "SUCCESS"
        else:
            status = "FAILED"

        write_log(username, status)

        response = json.dumps({
            "success": status == "SUCCESS",
            "message": (
                "Demo login successful!"
                if status == "SUCCESS"
                else "Incorrect demo credentials."
            )
        }).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)


if __name__ == "__main__":
    print("Instagram Verified - Independent Demo")
    print(f"Server: http://localhost:{PORT}")
    print(f"Demo username: {DEMO_USERNAME}")
    print(f"Demo password: {DEMO_PASSWORD}")
    print("Passwords entered by visitors are not logged.")

    HTTPServer((HOST, PORT), DemoHandler).serve_forever()
