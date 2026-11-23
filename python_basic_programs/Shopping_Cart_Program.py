# Shopping Cart Program

# Product Dictionary
products = {
    "Laptop": 65000,
    "Phone": 25000,
    "Mouse": 800,
    "Keyboard": 1200,
    "Monitor": 9000,
    "Speaker": 2500
}

cart = {}

print("========== Welcome to Shopping Cart ==========")

# Add Products
while True:
    print("\nAvailable Products:")
    for item in products:
        print(item, "- ₹", products[item])

    product = input("\nEnter Product Name: ").title()

    # Validate Product
    if product not in products:
        print("Invalid Product! Please try again.")
        continue

    quantity = int(input("Enter Quantity: "))

    # Validate Quantity
    if quantity <= 0:
        print("Quantity should be greater than 0.")
        continue

    # Add to Cart
    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity

    choice = input("Do you want to add more products? (yes/no): ")

    if choice.lower() != "yes":
        break

# Invoice
print("\n")
print("============== INVOICE ==============")
print("{:<12} {:<10} {:<10} {:<10}".format("Item", "Quantity", "Price", "Total"))

subtotal = 0

for item in cart:
    price = products[item]
    qty = cart[item]
    total = price * qty
    subtotal += total

    print("{:<12} {:<10} {:<10} {:<10}".format(item, qty, price, total))

# Discount
discount_percent = 0

if subtotal > 60000:
    discount_percent = 15
elif subtotal > 30000:
    discount_percent = 10
elif subtotal > 10000:
    discount_percent = 5

discount = subtotal * discount_percent / 100
final_amount = subtotal - discount

print("--------------------------------------")
print("Subtotal       : ₹", subtotal)
print("Discount (", discount_percent, "% ) : ₹", discount)
print("Final Amount   : ₹", final_amount)
print("======================================")
print("Thank You for Shopping!")