import logging

logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("System health check started")
logging.warning("Disk usage is getting high")
logging.error("Example error message")