# 12. Write a program to create a file, write data and read it.
file = open("demo.txt", "w");
file.write("Hello Khushali...");
file.close();

file2 = open("demo.txt","r");
print(file2.read())