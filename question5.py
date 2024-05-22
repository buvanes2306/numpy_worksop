#write a program to find if the given number is prime no or not
def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, n//2 + 1):
        if n % divisor == 0:
            print(f"{n} is not a prime number")
            return
    print(f"{n} is a prime number")
num = int(input("Enter the number: "))
is_prime(num)    
          
