from http.server import HTTPServer, BaseHTTPRequestHandler
import os

HTML = """
<!DOCTYPE html>
<html>
<body>

<h1>OpenClaw XSS Test Page</h1>

<p>Encoded HTML:</p>

<pre>
&lt;script&gt;
document.body.innerHTML="XSS_EXECUTED";
&lt;/script&gt;
</pre>

<p>Image test:</p>

<pre>
&lt;img src=x onerror="document.body.innerHTML='IMG_XSS_EXECUTED'"&gt;
</pre>

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
