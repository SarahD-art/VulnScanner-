import socket
import threading
from concurrent.futures import ThreadPoolExecutor

# A simple function to simulate vulnerability checks (placeholder)
def check_vulnerabilities(port, host):
    """Placeholder for vulnerability checking. In real use, you would integrate vulnerability scanning tools here."""
    print(f"Checking vulnerabilities on port {port}...")
    # Simulate vulnerability check (e.g., using nmap or other scanning tools)
    if port == 80:  # Simulate HTTP service vulnerability check
        print(f"Warning: Potential vulnerability on HTTP service (port {port}) at {host}")
    elif port == 443:  # Simulate HTTPS service vulnerability check
        print(f"Warning: Potential vulnerability on HTTPS service (port {port}) at {host}")
    # You can add more vulnerability checks based on port or service.

def check_port(host, port, timeout=1):
    """Check if a specific port on a host is open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)  # Set timeout for the connection attempt
        result = sock.connect_ex((host, port))  # Attempt connection
        sock.close()
        return result == 0  # Return True if port is open, else False
    except (socket.timeout, socket.error):  # Handle both socket error and timeout exceptions
        return False

def scan_port(host, port):
    """Wrapper function to scan port and print result, then check for vulnerabilities if open."""
    is_open = check_port(host, port)
    if is_open:
        print(f"Port {port} is open on {host}.")
        check_vulnerabilities(port, host)
    else:
        print(f"Port {port} is closed on {host}.")

def main():
    # Input host and range of ports
    host = input("Enter the host to check (e.g., localhost or IP): ")
    port_range_input = input("Enter port range to check (e.g., 1-1000): ")
    timeout = int(input("Enter timeout in seconds (default 1s): ") or 1)

    # Parse port range
    try:
        start_port, end_port = map(int, port_range_input.split('-'))
    except ValueError:
        print("Invalid port range format. Example format: 1-1000")
        return

    # Ensure the range is valid
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Port numbers must be between 1 and 65535.")
        return

    # Use ThreadPoolExecutor to handle threading more efficiently
    with ThreadPoolExecutor(max_workers=(end_port - start_port + 1)) as executor:
        # Submit tasks for each port in the range to scan concurrently
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)

if __name__ == "__main__":
    main()
