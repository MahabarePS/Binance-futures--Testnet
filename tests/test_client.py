"""
 * author Prasad Mahabare
 * created on 08-06-2026-23h-27m
 * github: https://github.com/MahabarePS
 * copyright 2026
"""

# test_client.py

# from config import API_KEY, API_SECRET
# from bot.client import BinanceClient

# binance_client = BinanceClient(
#     API_KEY,
#     API_SECRET
# )

# client = binance_client.get_client()

# print("Connected Successfully")

from config import API_KEY, API_SECRET
from bot.client import BinanceClient

client = BinanceClient(
    API_KEY,
    API_SECRET
).get_client()

account_info = client.futures_account()

print("Connection Successful")
print(account_info["totalWalletBalance"])