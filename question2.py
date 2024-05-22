# find if the given number is a palindrome or not?
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # remove spaces and convert to lowercase
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
n = input("Enter a string:")
print(is_palindrome(n))  
