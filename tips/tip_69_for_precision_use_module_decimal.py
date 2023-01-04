# Tip 69 for precision use module decimal
# https://docs.python.org/3/library/decimal.html

from decimal import Decimal, ROUND_UP

rate = Decimal('0.05')
seconds = Decimal('5')
small_cost = rate * seconds / Decimal(60)
print(small_cost)
print(small_cost.quantize(Decimal('0.001'), rounding=ROUND_UP))
