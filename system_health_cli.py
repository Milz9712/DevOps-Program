import argparse

parser = argparse.ArgumentParser(
    description="System health monitoring tool"
)

parser.add_argument(
    "--server",
    required=True,
    help="Name of the server being checked"
)

parser.add_argument(
    "--environment",
    choices=["development", "staging", "production"],
    required=True,
    help="Environment where the server is running"
)

args = parser.parse_args()

print(f"Checking server: {args.server}")
print(f"Environment: {args.environment}")
print("Health check complete")