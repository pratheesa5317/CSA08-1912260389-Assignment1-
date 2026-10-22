try:
    farmer_id = input("Enter farmer ID: ")
    litres = float(input("Enter milk quantity: "))
    fat = float(input("Enter fat percentage: "))

    if litres <= 0:
        print("Invalid milk quantity")
    elif fat < 0 or fat > 100:
        print("Invalid fat percentage")
    else:
        print(f"Farmer ID: {farmer_id}")
        print(f"Milk quantity: {litres:.2f}")
        print(f"Fat percentage: {fat:.2f}")

except ValueError:
    print("Please enter valid numeric values")
