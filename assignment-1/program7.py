#  7. Create a list of numbers and perform :
#   - add an element
#   - remove an element
#   - find the sum
arr = [1,2,3,4,5];

arr.append(6);
print(f"add an element : {arr}");
arr.remove(3);
print(f"remove an element : {arr}")
print(f"sum of an element : {sum(arr)}");


# another way to find sum using for in loop
sum = 0;
for i in arr:
    sum += i;

print(f"sum of an element : {sum}")