"""
 * author Prasad Mahabare
 * created on 08-06-2026-22h-27m
 * github: https://github.com/MahabarePS
 * copyright 2026
"""

# bot/logging_config.py

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

import logging

def setup_logger():

    logging.basicConfig(
        filename="logs/trading.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )