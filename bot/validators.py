"""
 * author Prasad Mahabare
 * created on 08-06-2026-22h-28m
 * github: https://github.com/MahabarePS
 * copyright 2026
"""


def validate_side(side):

    valid_sides = ["BUY", "SELL"]

    if side not in valid_sides:
        raise ValueError(
            f"Invalid side: {side}"
        )

def validate_order_type(o_type):

    valid_orders = ["MARKET", "LIMIT"]

    if o_type not in valid_orders:
        raise ValueError(
            f"Invalid order type: {o_type}"
        )

def validate_quantity(quantity):

    if quantity <= 0:
        raise ValueError(
            f"Quantity must be greater than 0. Got: {quantity}"
        )

def validate_price(price):

    if price is None:
        raise ValueError(
            "Price is required for LIMIT orders"
        )

    if price <= 0:
        raise ValueError(
            f"Price must be greater than 0. Got: {price}"
        )

def validate_symbol(symbol):

    VALID_SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "BNBUSDT"]

    if symbol not in VALID_SYMBOLS:
        raise ValueError(
            f"Unsupported symbol: {symbol}"
        )