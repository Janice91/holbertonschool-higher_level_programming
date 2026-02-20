#!/usr/bin/python3
"""
Simple API using Python's http.server module
"""


import http.server
import socketserver
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler
    """

    def do_GET(self):
        """
        Handle GET requests
        """
        if self.path == '/':
            # Root endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # Data endpoint - return JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            # Status endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # Info endpoint - return JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())

        else:
            # 404 for undefined endpoints
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error = {
                "error": "Endpoint not found"
            }
            self.wfile.write(json.dumps(error).encode())


def run(port=8000):
    """
    Run the HTTP server
    """
    server_address = ('', port)
    httpd = socketserver.TCPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
