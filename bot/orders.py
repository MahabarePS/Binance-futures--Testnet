"""
 * author Prasad Mahabare
 * created on 08-06-2026-22h-27m
 * github: https://github.com/MahabarePS
 * copyright 2026
"""

# orders.py

def place_market_order(
    client,
    symbol,
    side,
    quantity,
    logger
):

    logger.info(
        f"MARKET ORDER | {side} | {symbol} | Qty={quantity}"
    )

    response = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logger.info(
        f"ORDER RESPONSE | {response}"
    )

    return response