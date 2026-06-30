from http.server import HTTPServer, BaseHTTPRequestHandler
import os

HTML = """
<!doctype html>
<html>
<head>
<title>OpenClaw CDP Snapshot Test</title>
</head>

<body>

<h1>Browser Snapshot XSS Test</h1>

<div id="test">

    <p>This is normal content.</p>

    <!-- Attacker-controlled HTML -->
    <img 
      src="invalid-image"
      onerror="document.body.setAttribute('data-xss-test','XSS_EXECUTED')"
    >

</div>

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


port = int(os.environ.get("PORT", 8080))

server = HTTPServer(
    ("0.0.0.0", port),
    Handler
)

print(f"Server running on port {port}")

server.serve_forever()
