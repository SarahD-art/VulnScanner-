This project is a simple Python script for scanning a range of ports on a given host (IP address or domain). It checks whether each port in the specified range is open or closed and prints the results. The script is designed to run efficiently using concurrent threading to scan multiple ports simultaneously.

Features
Port Range Scanning: Allows you to specify a range of ports to scan (e.g., 1-1000).
Concurrency: Uses Python's ThreadPoolExecutor to scan multiple ports concurrently, speeding up the process.
Simple Output: Prints the status (open or closed) for each port in the specified range.
Requirements
Python 3.x
No external libraries are required (standard Python library).

Installation
Clone the repository or download the port_scanner.py file to your local machine.

bash code
git clone https://github.com/yourusername/port-scanner.git

How It Works
User Input: The script takes user input for the host and port range.
Port Scanning: The script attempts to connect to each port in the specified range on the given host. If the connection is successful, the port is marked as "open". If it fails, the port is marked as "closed".
Concurrency: The script uses Python’s ThreadPoolExecutor to scan multiple ports concurrently, speeding up the process significantly compared to scanning ports sequentially.
Output: The status of each port (whether it is open or closed) is printed to the console.
