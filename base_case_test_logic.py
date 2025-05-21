import pytest
from models import Item, Receipt
from logic import calculate_points


def test_target_example_receipt():
    receipt = Receipt(
        retailer="Target",
        purchaseDate="2022-01-01",
        purchaseTime="13:01",
        total="35.35",
        items=[
            Item(shortDescription="Mountain Dew 12PK", price="6.49"),
            Item(shortDescription="Emils Cheese Pizza", price="12.25"),
            Item(shortDescription="Knorr Creamy Chicken", price="1.26"),
            Item(shortDescription="Doritos Nacho Cheese", price="3.35"),
            Item(shortDescription="Klarbrunn 12-PK 12 FL OZ", price="12.00")
        ]
    )
    points = calculate_points(receipt)
    assert points == 28


def test_m_and_m_corner_market_example_receipt():
    receipt = Receipt(
        retailer="M&M Corner Market",
        purchaseDate="2022-03-20",
        purchaseTime="14:33",
        total="9.00",
        items=[
            Item(shortDescription="Gatorade", price="2.25"),
            Item(shortDescription="Gatorade", price="2.25"),
            Item(shortDescription="Gatorade", price="2.25"),
            Item(shortDescription="Gatorade", price="2.25")
        ]
    )
    points = calculate_points(receipt)
    assert points == 109
