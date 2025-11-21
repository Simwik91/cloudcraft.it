import http.server
import socketserver
import webbrowser
import threading
import time

PORT = 8000
HOST = 'localhost'

# Build the URL to open
URL = f"http://{HOST}:{PORT}/index.html"

# Define the HTTP request handler
Handler = http.server.SimpleHTTPRequestHandler

def run_server():
    """Starts the HTTP server."""
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://{HOST}:{PORT}")
        print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()

# Run the server in a separate thread.
# This is a non-daemon thread, so the main script will wait for it to complete.
# Since serve_forever() runs forever, the script will run until interrupted.
server_thread = threading.Thread(target=run_server)
server_thread.start()

# Wait a moment for the server to be ready
time.sleep(1)

# Open the web browser to the index.html page
print(f"Opening browser to {URL}...")
webbrowser.open(URL)
