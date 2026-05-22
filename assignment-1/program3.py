# 3. Write a program to calculate final price after applying discount.
price = float(input("Enter price: "));
discount = float(input("Enter discount: "));
finalPrice = price - (price * discount / 100);
print("Final price after discount is : ", finalPrice);