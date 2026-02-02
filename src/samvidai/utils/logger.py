import logging


def get_logger(name: str = "samvidai") -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger  # avoid duplicate handlers

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
