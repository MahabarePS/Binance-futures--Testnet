"""
 * author Prasad Mahabare
 * created on 08-06-2026-22h-28m
 * github: https://github.com/MahabarePS
 * copyright 2026
"""

import logging

def setup_logger():

    logger = logging.getLogger("trading_bot")

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler(
            "logs/trading.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger