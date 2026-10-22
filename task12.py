from decimal import Decimal

BASE = Decimal("32.00")
FAT_STEP = Decimal("0.45")
BONUS = Decimal("0.50")
LIMIT = Decimal("500")

def rate_per_litre(fat, month):
    if month.lower() in ["april", "may", "june"]:
        return BASE + fat * FAT_STEP
    raise ValueError("Non-seasonal rate card not provided")

def bonus(total_litres):
    if total_litres > LIMIT:
        return total_litres * BONUS
    return Decimal("0.00")

month = input("Enter month: ")
litres = Decimal(input("Enter ten-day litres: "))
fat = Decimal(input("Enter fat value: "))

rate = rate_per_litre(fat, month)
payment = litres * rate
extra = bonus(litres)

print(f"Rate: Rs. {rate:.2f}")
print(f"Payment: Rs. {payment:.2f}")
print(f"Bonus: Rs. {extra:.2f}")
print(f"Total: Rs. {payment + extra:.2f}")
