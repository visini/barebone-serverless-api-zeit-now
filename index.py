from http.server import BaseHTTPRequestHandler
import debugserver
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {"hello": "world"}
        self.wfile.write(json.dumps(response).encode("utf-8"))

        return

if __name__ == '__main__':
    debugserver.serve(handler)
