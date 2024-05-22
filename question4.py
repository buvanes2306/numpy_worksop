#write a program to find the sum of digits of a given number'
n = int(input("Enter the number of digits to be added: "))
sum = 0
for i in range(1,n+1):
  num = int(input("Enter a number: "))
  sum = sum + num
print("the sum of given number is ",sum)
  
  
