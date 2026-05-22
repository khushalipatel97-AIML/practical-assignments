# write a program to calculate the average of 5 numbers.
val1 = int(input("Enter value 1: "));
val2 = int(input("Enter value 2: "));
val3 = int(input("Enter value 3: "));
val4 = int(input("Enter value 4: "));
val5 = int(input("Enter value 5: "));

def avgFun(val1, val2, val3, val4, val5):
    return (val1 + val2 + val3 + val4 + val5) / 5;

print("Average value of five numbers is : " , avgFun(val1, val2, val3, val4, val5));
