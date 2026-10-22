def rate_per_litre(fat, snf):
    return (fat * 5) + (snf * 2)

def payout(litres, rate):
    return litres * rate

if __name__ == "__main__":
    rate = rate_per_litre(4.5, 8.5)
    payment = payout(10, rate)

    print("Rate:", rate)
    print("Payment:", payment)
