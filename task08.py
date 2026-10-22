farmer_id = input("Enter farmer ID: ")
litres = float(input("Enter milk quantity: "))
rate = float(input("Enter rate per litre: "))

if litres <= 0:
    print("Invalid milk quantity")
else:
    payment = litres * rate
    print("Farmer ID:", farmer_id)
    print("Payment:", payment)
