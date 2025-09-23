# Write a program to print numbers from 1 to 10 using a one line function with out lambda
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

# Write a Python program to print "Hello, World!".
def hello_world():return "Hello, World!"
print(hello_world())
# Write a program to add two numbers entered by the user.
def add_numbers(num1, num2):return num1 + num2
print(add_numbers(1, 2))
# Write a program to swap two variables without using a third variable.
def swap_variables(num1, num2):return num2, num1
print(swap_variables(1, 2))
# Write a program to check if a number is even or odd.
def is_even(num):return num % 2 == 0
print(is_even(2))
# Write a program to find the largest of three numbers.
def largest_number(num1, num2, num3):return max(num1, num2, num3)
print(largest_number(1, 2, 3))
# Write a program to calculate the factorial of a number.
def factorial(num):return 1 if num == 0 else num * factorial(num - 1)
print(factorial(5))
# Write a program to generate the Fibonacci series up to n terms.
def fibonacci(n):return [0, 1] + [fibonacci(n-1)[-1] + fibonacci(n-1)[-2] for i in range(2, n)]
print(fibonacci(10))

# Write a program to reverse a number.
def reverse_number(num):return int(str(num)[::-1])
print(reverse_number(12345))
# Write a program to check if a number is prime.
def is_prime(num):return all(num % i != 0 for i in range(2, int(num/2)+1))
print(is_prime(7))
# Write a program to find the sum of digits of a number.
def sum_digits(num):return sum(int(i) for i in str(num))
print(sum_digits(12345))
# Write a program to find the GCD of two numbers.
def gcd(num1 ,num2):return num1 if num2 == 0 else gcd(num2, num1 % num2)
print(gcd(12 , 18))
# Write a program to check if a string is a palindrome.
def is_palidrome(str):return str == str[::-1]
print(is_palidrome("omo"))
# Write a program to count vowels and consonants in a string.
def count_vowels_consonants(str):return sum (1 for i in "aeiou" if i in str) 
print(count_vowels_consonants("hello"))
# Write a program to find the ASCII value of a character.
def ascii(num):return ord(num)
print(ascii("o"))
# Write a program to sort a list without using built-in sort().
def sort_list(list):return sorted(list)
print(sort_list([4,2,5,6]))
# Write a program to find the second largest number in a list.
def second_largest(list):return sorted(list)[-2]
print(second_largest([4,2,5,6]))
# Write a program to remove duplicates from a list.
def remove_duplicates(list): return list(set(list))
print(remove_duplicates([1,2,2,3]))
# Write a program to check if two strings are anagrams.
def anagrams(str1,str2):return sorted(str1) == sorted(str2)
print(anagrams ("omkar","marko"))
# Write a program to merge two sorted lists.
def merge(str2 , str3):return sorted(str2 + str3)
print(merge([1,3,5,9],[1,5,4,8]))
# Write a program to count the frequency of words in a string.
def count_frequency(s):return {w: s.split().count(w) for w in s.split()}
print(count_frequency("hello"))
# Advanced (21–30)
# Write a program to implement a simple calculator (add, subtract, multiply, divide).
def calculator(num1, num2, operator):return eval(f"{num1} {operator} {num2}")
print(calculator(1, 2, "+"))    
# Write a program to check Armstrong numbers.
def armstrong(num):return num == sum (int(i)** len(str(num))for i in str(num))
print(armstrong(12312))
# Write a program to convert decimal to binary, octal, and hexadecimal.
def convert(num): return bin(num), oct(num), hex(num)
print(convert(10))
# Write a program to create a dictionary from two lists.
def create_dict(list1 , list2):return dict(zip(list1, list2))
print(create_dict(["a", "b", "c"], [1, 2, 3]))
# Write a program to find the largest and smallest elements in a tuple.
def largest_smallest_tuple(tuple):return max(tuple), min(tuple)
print(largest_smallest_tuple((1, 2, 3, 4, 5)))
# Write a program to find the factorial of a number using recursion.
def factorial_recursive(n):return 1 if n == 0 or n == 1 else: factorial_recursive(n-1) * n
print(factorial_recursive())
# Write a program to read and write a file.
# Write a program to find the common elements in two sets.
# Write a program to implement a class for a student with attributes (name, age, grade).
# Write a program to generate a random password of given length.