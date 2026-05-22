# 2. Write a program to find the largest of three numbers.
val1 = int(input("Enter value 1: "));
val2 = int(input("Enter value 2: "));
val3 = int(input("Enter value 3: "));

print("Largest number of three values is :" ,max(val1, val2, val3))

# second way is using if-else
if((val1 > val2) and (val1 >val3)):
    print("Largets number of value is : ", val1);
elif((val2 > val1) and (val2 > val3)):
    print("Largets number of value is : ", val2);
else:
    print("Largets number of value is : ", val3);

