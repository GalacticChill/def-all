# logger.py
import logging

def setup_logger(name="simulator"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s', "%H:%M:%S")
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger
