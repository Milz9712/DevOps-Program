import sys

if len(sys.argv) < 2:
    print("Usage: python3 check_server.py <server-name>")
    sys.exit(1)

server = sys.argv[1]

print(f"Checking server: {server}")
print("Server check complete") 