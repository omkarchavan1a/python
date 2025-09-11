import random
import string

# 1. Print "Hello, World!"
def print_hello():
    print("Hello, World!")

# 2. Add two numbers entered by the user
def add_numbers(a, b):
    return a + b
print(add_numbers(1 , 2))
# 3. Swap two variables without using a third variable
def swap(a, b):
    a, b = b, a
    return a, b
print(swap(22 ,11))
# 4. Check if a number is even or odd
def is_even(num):
    return num % 2 == 0
print(is_even(2))
# 5. Find the largest of three numbers
def largest_of_three(a, b, c):
    return max(a, b, c)
print(largest_of_three(1, 2, 3))
# 6. Calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print(factorial(5))
# 7. Generate the Fibonacci series up to n terms
def fibonacci(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series
print(fibonacci(10))
# 8. Reverse a number
def reverse_number(num):
    return int(str(num)[::-1])
print(reverse_number(123))
# 9. Check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))
# 10. Find the sum of digits of a number
def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))
print(sum_of_digits(123))
# 11. Find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(12, 18))
# 12. Check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(is_palindrome("racecar"))
# 13. Count vowels and consonants in a string
def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    v = c = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1
    return v, c
print(count_vowels_consonants("Hello"))
# 14. Find the ASCII value of a character
def ascii_value(char):
    return ord(char)
print(ascii_value("A"))
# 15. Sort a list without using built-in sort()
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
print(sort_list([3, 1, 2]))
# 16. Find the second largest number in a list
def second_largest(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None
print(second_largest([3, 1, 2]))
# 17. Remove duplicates from a list
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
print(remove_duplicates([1, 2, 2, 3]))
# 18. Check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())
print(are_anagrams("listen", "silent"))
# 19. Merge two sorted lists
def merge_sorted_lists(l1, l2):
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result.extend(l1[i:])
    result.extend(l2[j:])
    return result
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
# 20. Count the frequency of words in a string
def word_frequency(s):
    words = s.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
print(word_frequency("Hello, world!"))  
# 21. Simple calculator (add, subtract, multiply, divide)
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else None
    else:
        return None
print(calculator(1, 2, '+'))
# 22. Check Armstrong numbers
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d ** len(digits) for d in digits)
print(is_armstrong(153))
# 23. Convert decimal to binary, octal, and hexadecimal
def convert_bases(num):
    return bin(num)[2:], oct(num)[2:], hex(num)[2:]
print(convert_bases(10))
# 24. Create a dictionary from two lists
def lists_to_dict(keys, values):
    return dict(zip(keys, values))
print(lists_to_dict(['a', 'b', 'c'], [1, 2, 3]))
# 25. Find the largest and smallest elements in a tuple
def tuple_min_max(t):
    return min(t), max(t)
print(tuple_min_max((1, 2, 3, 4, 5)))
# 26. Factorial using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(5))
# 27. Read and write a file
def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
print(write_file("test.txt", "Hello, world!"))
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
print(read_file("test.txt"))
# 28. Find the common elements in two sets
def common_elements(set1, set2):
    return set1 & set2
print(common_elements({1, 2, 3}, {2, 3, 4}))
# 29. Implement a class for a student with attributes (name, age, grade)
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
print(Student("John", 20, 85))
# 30. Generate a random password of given length
def random_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

