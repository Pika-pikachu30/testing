from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>OpenClaw XSS Test</title>
</head>

<body>

<h1>OpenClaw HTML Entity Test</h1>

<p>This is normal content.</p>

<p>
Encoded payload:
</p>

<pre>
&lt;script&gt;
document.body.innerHTML="XSS_EXECUTED";
&lt;/script&gt;
</pre>

<p>
Image payload:
</p>

<pre>
&lt;img src=x onerror="document.body.innerHTML='IMG_XSS_EXECUTED'"&gt;
</pre>

</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.encode())


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8080), Handler)

    print("Test server running:")
    print("http://127.0.0.1:8080/test.html")

    server.serve_forever()
