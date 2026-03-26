print("🛫 BOOKING TICKET FOR YOUR TRIP 🛫")
destination = str(input("Where are you going for your trip?"))
quantity = int(input("How many ticket do you need?"))
price = float(input("what's the price of each ticket? (be honest)"))
hotel = str(input("Do you want to book a hotel?")) == "yes"
total = quantity * price

print("\n🎫 YOUR BOOKING SUMMARY 🎫")
print(f"Your destination: {destination}")
print(f"Amount of ticket: {quantity}")
print(f"price of each ticket: {price}")
print(f"Do you need hotel: {hotel}")
print(f"your total is: {total}")