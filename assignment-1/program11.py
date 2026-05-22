# 11. Write a program to count the number of vowels in a string.
str = "Khushali Patel";
vowels = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U'];

new_val = [];
for i in str:
    if(i in vowels):
        new_val.append(i);
   
print(f"the number of vowels in a string is : {len(new_val)}")