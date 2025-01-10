#jerelyn
#cfu18

# Version 2: Asking user for prices
prices = []
num_prices = int(input("How many prices do you want to add? "))

for i in range(num_prices):
    price = float(input(f"Enter the price of item {i + 1}: "))
    prices.append(price)

total = 0
for price in prices:
    total += price

print(f"Total: ${total:.2f}")


# Version 3: Asking user for prices and item names
items = []
prices = []

num_items = int(input("How many items do you want to add? "))

for i in range(num_items):
    item_name = input(f"Enter the name of item {i + 1}: ")
    item_price = float(input(f"Enter the price of {item_name}: "))
    items.append(item_name)
    prices.append(item_price)

total = 0
print("\nReceipt:")
for i in range(num_items):
    print(f"{items[i]}: ${prices[i]:.2f}")
    total += prices[i]
