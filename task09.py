try:
    farmer_id = input("Enter farmer ID: ")
    litres = float(input("Enter milk quantity: "))
    rate = float(input("Enter rate per litre: "))

    if litres <= 0:
        print("Invalid milk quantity")
    elif rate < 0:
        print("Invalid rate")
    else:
        payment = litres * rate
        print("Farmer ID:", farmer_id)
        print(f"Payment: Rs. {payment:.2f}")

except ValueError:
    print("Invalid input. Enter numbers correctly.")
