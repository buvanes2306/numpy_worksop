#write a program to find the factorial of a nummber
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number for factorial: "))
print("Factorial of", num, "is", factorial(num))
