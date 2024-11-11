import socket
from concurrent.futures import ThreadPoolExecutor


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


def check_vulnerabilities(port, host):
    """Simulate vulnerability checks for open ports."""
    # In a real implementation, you might call `nmap` or check service versions here.
    print(f"Checking vulnerabilities on port {port} of {host}...")
    if port == 80:
        return "Potential HTTP vulnerability detected."
    elif port == 443:
        return "Potential HTTPS vulnerability detected."
    elif port == 22:
        return "SSH service - check for weak passwords."
    # Add more conditions as needed based on port/service
    return "No vulnerabilities detected."


def scan_port(host, port, save_to_file=False):
    """Scan a port, check vulnerabilities, and print/save result."""
    is_open = check_port(host, port)
    status = "open" if is_open else "closed"

    result = f"Port {port} is {status} on {host}"

    if is_open:
        vuln = check_vulnerabilities(port, host)
        result += f"\n    {vuln}"

    print(result)

    # Save results to a file if specified
    if save_to_file:
        with open('output.txt', 'a') as f:
            f.write(result + "\n\n")


def main():
    # Input for hosts and port range
    hosts_input = input("Enter the hosts to check (comma-separated): ")
    hosts = [host.strip() for host in hosts_input.split(",")]

    port_range_input = input("Enter port range to check (e.g., 1-1000): ")

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

    # Ask if the user wants to save results to a file
    save_to_file = input("Would you like to save the results to a file? (y/n): ").lower() == 'y'

    # Use ThreadPoolExecutor to scan ports concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        for host in hosts:
            for port in range(start_port, end_port + 1):
                executor.submit(scan_port, host, port, save_to_file)


if __name__ == "__main__":
    main()
