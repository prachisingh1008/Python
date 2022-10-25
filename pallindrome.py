
# Python code for the above approach
import math as Math
 
# Function to find if the number is a
# palindrome or not
def isPalindrome(n):
    if (n < 0):
        return False
    if (n < 10):
        return True
 
    # Find the length of the number
    K = Math.ceil(Math.log(n) / Math.log(10))
 
    ans = 0
 
    # Partition the number into 2 halves
    for i in range(0, K // 2):
        ans = ans * 10 + n % 10
        n = Math.floor(n / 10)
    if (K % 2 == 1):
        ans = ans * 10 + n % 10
 
    # Equality Condition
    return (ans == n)
 
# Driver Code
print("Yes, it is Palindrome") if isPalindrome(
    1001) else print("No, not Palindrome")
