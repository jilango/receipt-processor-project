from models import Receipt


def calculate_points(receipt: Receipt) -> int:
    points = 0

    # Rule 1: One point for every alphanumeric character in the retailer name.
    points += sum(c.isalnum() for c in receipt.retailer)

    # Rule 2: 50 points if the total is a round dollar amount with no cents.
    try:
        total = float(receipt.total)
        if total.is_integer():
            points += 50
    except ValueError:
        pass

    return points
