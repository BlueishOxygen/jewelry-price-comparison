PURITY_MAP = {
    "24K": 1.00,
    "22K": 0.916,
    "18K": 0.750,
    "14K": 0.585,
    "9K": 0.375
}

PURITY_MAP_SILVER = {
    "999":0.999,
    "995":0.995, 
    "958":0.958,
    "925":0.925,#argent sterling
    "900":0.900

}

# Def pour l'or

def gold_intrinsic_value(
    weight_grams: float,
    karat: str,
    gold_24k_price_per_gram: float
) -> float:
    """
    Calcule la valeur intrinsèque du bijou en or
    """
    purity = PURITY_MAP.get(karat)

    if purity is None:
        raise ValueError(f"Carat non reconnu : {karat}")

    return weight_grams * purity * gold_24k_price_per_gram

#def pour l'argent 

def silver_intrinsic_value(
    weight_grams: float,
    karat: str,
    silver_999_price_per_gram: float
) -> float:
    """
    Calcule la valeur intrinsèque du bijou en argent
    """
    purity = PURITY_MAP_SILVER.get(karat)

    if purity is None:
        raise ValueError(f"Carat non reconnu : {karat}")

    return weight_grams * purity * silver_999_price_per_gram
