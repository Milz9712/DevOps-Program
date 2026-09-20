import subprocess
import logging

logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("System health check started")


def get_disk_usage():
    result = subprocess.run(
        ["df", "-h", "/"],
        capture_output=True,
        text=True
    )

    return result.stdout 


def get_memory_usage():
    result = subprocess.run(
        ["free", "-h"],
        capture_output=True,
        text=True
    )

    return result.stdout


def get_cpu_load():
    result = subprocess.run(
        ["cat", "/proc/loadavg"],
        capture_output=True,
        text=True
    )

    load = result.stdout.split()

    return {
        "1_min": load[0],
        "5_min": load[1],
        "15_min": load[2]
    }

def check_disk():
    result = subprocess.run(
        ["df", "/"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.splitlines()
    data = lines[1].split()

    usage = int(data[4].replace("%", ""))

    if usage >= 80:
        return f"WARNING: Disk usage is {usage}%"
    else:
        return f"OK: Disk usage is {usage}%"

def check_memory():
    result = subprocess.run(
        ["free", "-m"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.splitlines()
    memory_data = lines[1].split()

    total = int(memory_data[1])
    used = int(memory_data[2])

    usage = (used / total) * 100

    if usage >= 80:
        return f"WARNING: Memory usage is {usage:.1f}%"
    else:
        return f"OK: Memory usage is {usage:.1f}%"

def check_cpu():
    result = subprocess.run(
        ["cat", "/proc/loadavg"],
        capture_output=True,
        text=True
    )

    load = float(result.stdout.split()[0])

    if load >= 2.0:
        return f"WARNING: CPU load is {load}"
    else:
        return f"OK: CPU load is {load}"

def get_overall_status():
    checks = [
        check_disk(),
        check_memory(),
        check_cpu()
    ]

    for check in checks:
        if "WARNING" in check:
            return "SYSTEM STATUS: WARNING"

    return "SYSTEM STATUS: HEALTHY"

def main():
    print("=== SYSTEM HEALTH ===")

    print("\nDisk usage:")
    print(get_disk_usage())

    print("Memory usage:")
    print(get_memory_usage())

    cpu_load = get_cpu_load()

    print("CPU load:")
    print(f"1 minute: {cpu_load['1_min']}")
    print(f"5 minutes: {cpu_load['5_min']}")
    print(f"15 minutes: {cpu_load['15_min']}")

    print("Disk health:")
    print(check_disk())

    print("Memory health:")
    print(check_memory())

    print("CPU health:")
    print(check_cpu())

    print(get_overall_status())

    logging.info("System health check completed")


if __name__ == "__main__":
    main() 