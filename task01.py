farmer_id = input("Enter farmer ID: ")
litres = float(input("Enter milk litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))

base_rate = 32.00
fat_rate = 0.45

payment = litres * (base_rate + fat * fat_rate)

print("\n--- Milk Payment Details ---")
print("Farmer ID:", farmer_id)
print("Milk Litres:", litres)
print("Fat:", fat)
print("SNF:", snf)
print("Total Payment: Rs.", round(payment, 2))
