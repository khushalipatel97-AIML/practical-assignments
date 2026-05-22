#15. write a function to check whether a number is prime or not.
def primeFun(num):
    if(num <= 1):
        return False;

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False;

    return True;    
    
val = int(input("Enter a number: "))
if primeFun(val):
    print(f"{val} is a prime number");
else:
    print(f"{val} is not a prime number");