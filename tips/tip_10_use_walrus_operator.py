# Tip 10 use walrus operator
import random


def get_apple_price():
    return random.randint(1, 200)


if (price := get_apple_price()) % 2 == 0:
    print(f"Even price: {price}")
else:
    print(f"Not even price: {price}")

print(price)
