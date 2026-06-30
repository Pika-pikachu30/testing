from http.server import HTTPServer, BaseHTTPRequestHandler
import os

HTML = """
<!doctype html>
<html>
<body>

<h1>Entity Render Test</h1>

&lt;b&gt;OPENCLAW_HTML_EXECUTED&lt;/b&gt;

</body>
</html>
"""



class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.encode())


port = int(os.environ.get("PORT", 8080))

server = HTTPServer(("0.0.0.0", port), Handler)

print(f"Server running on port {port}")

server.serve_forever()
