def rate_per_litre(fat, snf):
    return (fat * 5) + (snf * 2)

def payout(litres, rate):
    return litres * rate

def ten_day_total(payments):
    return sum(payments)

rate = rate_per_litre(4.5, 8.5)
payment = payout(10, rate)
total = ten_day_total([payment] * 10)

print("Rate:", rate)
print("Payment:", payment)
print("10-day total:", total)
