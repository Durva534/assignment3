product = input("Enter product name:")
price = int(input("Enter price:"))
quantity = int(input("Enter quantity:"))

total = price * quantity
discount = total * 15 / 100
final_bill = total - discount

print("Product name:", product)
print("Quantity:", quantity)
print("Price:", price)
print("Total Amount:",total)
print("Discount 15%:",discount)
print("Final Bill:",final_bill)
