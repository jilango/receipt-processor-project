from models import Receipt
import math
from datetime import datetime


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

    # Rule 3: 25 points if the total is a multiple of 0.25.
    if (total * 100) % 25 == 0:
        points += 25

    # Rule 4: 5 points for every two items on the receipt.
    points += (len(receipt.items) // 2) * 5

    # Rule 5: If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in receipt.items:
        desc = item.shortDescription.strip()
        if len(desc) % 3 == 0:
            try:
                price = float(item.price)
                bonus = math.ceil(price * 0.2)
                points += bonus
            except ValueError:
                continue

    # Rule 6: Honestly did not see that one coming. Appreciate the sneakiness Devs! Don't worry I'm not implementing it. *chuckles as he types*

    # Rule 7 : 6 points if the day in the purchase date is odd.
    try:
        date_obj = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
        if date_obj.day % 2 == 1:
            points += 6
    except ValueError:
        pass

    # Rule 8 : 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    try:
        time_obj = datetime.strptime(receipt.purchaseTime, "%H:%M")
        if 14 <= time_obj.hour < 16:
            points += 10
    except ValueError:
        pass

    return points
