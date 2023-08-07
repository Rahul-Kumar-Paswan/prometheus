from prometheus_client import start_http_server, Counter
import time

# Create a counter metric
requests_total = Counter('http_requests_total', 'Total number of HTTP requests')

# Simulate some requests
def process_request():
    requests_total.inc()

# Start the Prometheus HTTP server
start_http_server(8000)

# Simulate requests every second
while True:
    process_request()
    time.sleep(1)