from http.server import BaseHTTPRequestHandler
import json
import database
import debugserver

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        conn = database.connect()

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        cur = conn.cursor()
        cur.execute("""SELECT * from blog_posts""")
        columns = ('id', 'title', 'post')
        results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))

        self.wfile.write(json.dumps(results).encode("utf-8"))

        return

if __name__ == '__main__':
    debugserver.serve(handler)
