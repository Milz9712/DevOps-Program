import subprocess

result = subprocess.run(
    ["cat", "/proc/loadavg"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    load = result.stdout.split()
    print(f"CPU load (1 min): {load[0]}")
    print(f"CPU load (5 min): {load[1]}")
    print(f"CPU load (15 min): {load[2]}")
else:
    print(f"Command failed: {result.stderr.strip()}")