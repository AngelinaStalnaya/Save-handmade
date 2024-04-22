from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
from database.core import crud

HOST = '192.168.0.78'

POST = 5353

class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        self.wfile.write(bytes('<html><body><h1>ыупраплрошд</h1></body></html>', 'utf-8'))
        
    def do_POST(self):
        self.send_response(200)
        # self.send_header('Content-type', 'application/json')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        date = datetime.now()    
        self.wfile.write(bytes(f'<html><body><h1>time: + {date}</h1></body></html>', 'utf-8'))
            
server = HTTPServer((HOST, POST), NeuralHTTP)
print('server now running...')

server.serve_forever()
server.server_close()
print('server stopped!')