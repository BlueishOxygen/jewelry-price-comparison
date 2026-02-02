#esimation of the max bid

def max_bid_price(
    estimated_value: float,
    auction_fee_percent: float,
    shipping_cost: float,
    min_margin: float
) -> float:
    """
    Calcule la mise maximale pour respecter la marge minimale
    """
    return (estimated_value - shipping_cost) / (
        1 + auction_fee_percent + min_margin
    )
