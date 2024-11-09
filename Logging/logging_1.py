import logging


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

logging.debug("Debug message")
logging.info("Info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")