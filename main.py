# ==========================
# DONNÉES DU BIJOU OR
# ==========================
from config import gold_24k_price_per_gram, min_margin
from valuation import gold_intrinsic_value
from fees import max_bid_price

weight_grams = 2.6
karat = "18K"

auction_fee_percent = 0.30   # 28 %
shipping_cost = 0         # €


# CALCULS

intrinsic_value = gold_intrinsic_value(
    weight_grams=weight_grams,
    karat=karat,
    gold_24k_price_per_gram=gold_24k_price_per_gram
)

bid_max = max_bid_price(
    estimated_value=intrinsic_value,
    auction_fee_percent=auction_fee_percent,
    shipping_cost=shipping_cost,
    min_margin=min_margin
)

# AFFICHAGE

print("Prix or 24K (€/g) :", gold_24k_price_per_gram)
print("Poids du bijou    :", weight_grams, "g")
print("Carat             :", karat)
print("Valeur métal      :", round(intrinsic_value, 2), "€")
print(" Mise max rentable :", round(bid_max, 2), "€")


# ==========================
# DONNÉES DU BIJOU ARGENT
# ==========================

from config import silver_999_price_per_gram, min_margin
from valuation import silver_intrinsic_value
from fees import max_bid_price


weight_grams = 0.6
karat = "925"

auction_fee_percent = 0.24   # 28 %
shipping_cost = 0         # €


# CALCULS

intrinsic_value = silver_intrinsic_value(
    weight_grams=weight_grams,
    karat=karat,
    silver_999_price_per_gram=silver_999_price_per_gram
)

bid_max = max_bid_price(
    estimated_value=intrinsic_value,
    auction_fee_percent=auction_fee_percent,
    shipping_cost=shipping_cost,
    min_margin=min_margin
)

# AFFICHAGE

print("Prix argent 999 (€/g) :", silver_999_price_per_gram)
print("Poids du bijou    :", weight_grams, "g")
print("Carat             :", karat)
print("Valeur métal      :", round(intrinsic_value, 2), "€")
print(" Mise max rentable :", round(bid_max, 2), "€")