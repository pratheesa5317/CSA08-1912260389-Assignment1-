from decimal import Decimal

BASE_RATE = Decimal("32.00")
FAT_STEP = Decimal("0.45")

def calculate_payment(litres, fat):
    rate = BASE_RATE + fat * FAT_STEP
    payment = litres * rate
    return rate, payment

litres = Decimal(input("Enter milk litres: "))
fat = Decimal(input("Enter fat value: "))

rate, payment = calculate_payment(litres, fat)

print(f"Rate: Rs. {rate:.2f}")
print(f"Payment: Rs. {payment:.2f}")
