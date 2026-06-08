"""
 * author Prasad Mahabare
 * created on 08-06-2026-22h-27m
 * github: https://github.com/MahabarePS
 * copyright 2026
"""

from binance.client import Client


class BinanceClient:

    def __init__(self, api_key, api_secret):

        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )

    def get_client(self):
        return self.client