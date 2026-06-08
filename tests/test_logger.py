"""
 * author Prasad Mahabare
 * created on 08-06-2026-23h-22m
 * github: https://github.com/MahabarePS
 * copyright 2026
"""

# test_logger.py

from bot.logging_config import setup_logger

logger = setup_logger()

logger.info("Application Started")
logger.error("Sample Error")