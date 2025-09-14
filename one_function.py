# Write a program to print numbers from 1 to 10 using a one line function with out labda
def print_numbers():return [i for i in range(1,11)]
print(print_numbers())
# Write a program to print even numbers between 1 to 50 .
def even_numbers():return [i for i in range(2,51,2)]
print(even_numbers())
# Write a program to print odd numbers between 1 to 50
def odd_numbers():return[i for i in range(1,51,2)]
print(odd_numbers())     
# Write a program to print the multiplication table of a given number .
def multiplication_table(n):return [i*n for i in range(1,11)]
print(multiplication_table(5))
# Write a program to print the sum of the first 10 natural numbers .
def sum_of_number():return sum([i for i in range(1,11)])
print(sum_of_number())
# Write a program to calculate the factorial of a given number 
def factorial(n):return 1 if n==1 else n*factorial(n-1)
print(factorial(5))
# Write a program to reverse a given number 
def reversed(num): return int(str(num)[::-1])
print(reversed(12345))
# Write a program to count the number of digits in a given number 
def count_digit(num):return len(str(num))
print(count_digit(12345))                                                         
# Write a program to find the sum of digits of a given number 
def sum_digit(num):return sum (int(digit) for digit in str(num))
print(sum_digit(12345))
# Write a program to check whether a given number is a palindrome or not 
def palindrome(num):return str(num)==str(num)[::-1]
print(palindrome(12321))
# Write a program to check whether a given number is an Armstrong number or not
def is_armstrong(num):return num == sum (int(digit) ** len(str(num)) for digit in str(num))
print(is_armstrong(153))
# Write a program to generate the Fibonacci series up to n terms 
def fibonacci(n):return [0 for i in range(n)] + [i for i in range (2, n) if i % 2 == 0]
print(fibonacci(10))

# Write a program to print squares of numbers from 1 to n 
def squares(n):return [i**2 for i in range(1,n+1)]
print(squares(5))
# Write a program to print cubes of numbers from 1 to n u
def cubes(n):return [i ** 3 for i in range(1, n+1)]
print(cubes(5))
# Write a program to find the largest digit in a given number 
def largest_digit(num):return max(int (i) for i in str(num))
print(largest_digit(12345))

# Write a program to find the smallest digit in a given number 
def smaller_digit(num):return min(int (i) for i in str(num))
print(smaller_digit(12345))

# Write a program to calculate the power of a number (a^b) 
def power(a, b):return a ** b
print(power(23,45))

# Write a program to check whether a given number is prime or not 
def is_prime(num): return all(num % i != 0 for i in range(2, int(num/2)+1))
print(is_prime(7))
# Write a program to print all prime numbers between 1 to 100 
def prime_numbers(): return[i for i in range(2,101) if is_prime(i)] 
print(prime_numbers())

# Write a program to print all numbers divisible by 7 between 1 to 100 
def divisible_by_7():return [i for i in range(1 , 101) if i % 7 == 0] 
print(divisible_by_7())
# Write a program to convert a decimal number into binary 
def decimal_binary(num):return bin(num)
print(decimal_binary(10))
# Write a program to print the reverse of a string 
def reverse_string(str):return str[::-1]
print(reverse_string("hello"))

# Write a program to count the vowels in a given string using a while loop.
def count_vowels(str):return sum(1 for i in str if i in "aeiouAEIOU")
print(count_vowels("hello"))
# Write a program to print the sum of even digits and odd digits separately in a given number 
def sum_even_odd(num):return sum(int(i) for i in str(num) if int(i) % 2 == 0), sum(int(i) for i in str(num) if int(i) % 2 != 0)
print(sum_even_odd(12345))

# Write a program to keep taking input from the user until they enter 0, then print the sum of all entered numbers.
def sum_of_numbers():return sum(int(i) for i in input("Enter numbers (separated by spaces): ").split() if int(i) != 0)
print(sum_of_numbers())