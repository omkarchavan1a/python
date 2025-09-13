# 1.Write a program to check if a number is divisible by 5 and 11.
def check_number(num):
    if num % 5 == 0 and num % 11 == 0:
        return True
    else:
        return False

print(check_number(7))
    
 
# 2. Write a program to check whether a given number is Armstrong number or not.
def is_armstrong(num):
     sum = len(str(num))
     sum = 0
     for i in range(sum):
         digit = digit % 10
         sum += digit ** num
         return num == num

print(is_armstrong(10))     
 
# 3. Write a program to print the square of first 10 numbers using a loop.
def square_of_numbers(n):
    """Print the square of numbers from 1 to n."""
    for i in range(1, n + 1):
        print(i ** 2)

square_of_numbers(10)
# 4. Write a program to check whether a number is perfect number or not.
def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return num == sum 

print(perfect_number(6)) 
# 5. Write a program to find the greatest common divisor (GCD) of two numbers using a loop.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(12, 18))
 
 
# 6. Write a program to print all numbers from 1 to 50 which are divisible by 7.
def divisible_by_7():
    for i in range(1, 51):
        if i % 7 == 0:
            print(i)

divisible_by_7()
 
 
# 7. Write a program to print the sum of even numbers between 1 and n.
def sum_of_even(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum += i
    return sum

print(sum_of_even(10))

 
 
# 8. Write a program to print the sum of odd numbers between 1 and n.
def sum_of_add(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum += i
    return sum
 
 
# 9. Write a program to check if a number is a Harshad number (divisible by sum of its digits).
def is_harshad(num):
    sum = sum(int(digit) for digit in str(num))
    return num % sum == 0

print(is_harshad(18))
 
 
# 10. Write a program to print the first 10 terms of the arithmetic progression (AP) series.
def arithmatic_progression(num):
    for i in range(1, num + 1):
        return(i * num)
    
print(arithmatic_progression(10))
# 11. Write a program to print the first 10 terms of the geometric progression (GP) series.
def geometric_progression(num):
    for i in range(1, num + 1):
        return(i * num)
    
print(geometric_progression(10))
 
# 12. Write a program to check whether a given string is a palindrome or not.
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

print(is_palindrome("racecar")) 
# 13. Write a program to count the number of vowels in a string using a loop.
def count_vowels(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count += 1
    return count

print(count_vowels("hello"))
 
 
# 14. Write a program to count the number of uppercase and lowercase letters in a string.
def count_upper_lower(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower

print(count_upper_lower("Hello"))
 
 
# 15. Write a program to print the multiplication tables from 1 to 10 using nested loops.
def multiplication_tables():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

multiplication_tables()