print("HELLOOO, welcome to our store🥳🥳")
shopping = str(input("What a wonderful day, What will be your item today?"))
quantity = int(input("Andd how many item is it?"))
price = float(input("There is so many inflation, so what the price of each item?"))
member = str(input("do you have any member from our store? (yes or no)"))
tbd = quantity*price
discount = tbd*0.10
total = tbd - discount

print("\nYOUR BILLS IS...")
print("your item" + " " + shopping)
print(f"item(S) you take {quantity}")
print(f"and the price for each item is {price}")

if member == "yes":
    print(f"because you have a member your discount is {discount}")
    print(f"so your total is {total}")
else:
    print(f"your total is (please dont have a heart attack) {tbd}")