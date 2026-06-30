from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(500)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(
            b"<script>alert('XSS')</script>"
        )

server = HTTPServer(("0.0.0.0", 8080), Handler)

print("running")
server.serve_forever()
