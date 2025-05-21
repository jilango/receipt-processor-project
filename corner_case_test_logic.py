import pytest
from models import Item, Receipt
from logic import calculate_points


def test_retailer_with_symbols():
    receipt = Receipt(
        retailer="$$$!!!###",
        purchaseDate="2022-01-01",
        purchaseTime="13:00",
        total="5.00",
        items=[Item(shortDescription="Apple", price="5.00")]
    )
    points = calculate_points(receipt)
    assert points == 81


def test_invalid_price_format_ignored():
    receipt = Receipt(
        retailer="Test",
        purchaseDate="2022-01-01",
        purchaseTime="13:00",
        total="not-a-number",
        items=[Item(shortDescription="Item", price="also-wrong")]
    )
    points = calculate_points(receipt)
    assert points == 10


def test_empty_items_list_graceful_fail():
    receipt = Receipt(
        retailer="Target",
        purchaseDate="2022-01-01",
        purchaseTime="13:00",
        total="10.00",
        items=[]
    )
    points = calculate_points(receipt)
    assert points == 87


def test_description_multiple_of_3_triggers_bonus():
    receipt = Receipt(
        retailer="Store",
        purchaseDate="2022-01-01",
        purchaseTime="13:00",
        total="5.00",
        items=[
            Item(shortDescription="ABC", price="4.00")
        ]
    )
    points = calculate_points(receipt)
    assert points == 87


def test_time_before_and_after_bonus_window():
    receipt_before = Receipt(
        retailer="X",
        purchaseDate="2022-01-01",
        purchaseTime="13:59",
        total="5.00",
        items=[Item(shortDescription="x", price="5.00")]
    )
    receipt_after = Receipt(
        retailer="X",
        purchaseDate="2022-01-01",
        purchaseTime="16:01",
        total="5.00",
        items=[Item(shortDescription="x", price="5.00")]
    )
    points_before = calculate_points(receipt_before)
    points_after = calculate_points(receipt_after)
    assert points_before == 82
    assert points_after == 82
