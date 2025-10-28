
from __future__ import annotations

import math
import itertools as it
from collections import Counter, defaultdict
from typing import List, Tuple, Dict, Iterable, Any

###############################################
# 1. Basic Input/Output & Arithmetic (1–15)
###############################################

# 1. Add two numbers
add_two_numbers_a = lambda a, b: a + b
add_two_numbers_b = sum

# 2. Square of a number
square_a = lambda x: x * x
square_b = lambda x: pow(x, 2)

# 3. Cube of a number
cube_a = lambda x: x * x * x
cube_b = lambda x: pow(x, 3)

# 4. Area of a circle
area_circle_a = lambda r: math.pi * r * r
area_circle_b = lambda r: math.pi * pow(r, 2)

# 5. Area of a rectangle
area_rectangle_a = lambda length, width: length * width
area_rectangle_b = lambda l, w: (l * w)

# 6. Celsius to Fahrenheit
c_to_f_a = lambda c: (c * 9 / 5) + 32
c_to_f_b = lambda c: 32 + (c * 1.8)

# 7. Kilometers to miles
km_to_miles_a = lambda km: km * 0.621371
km_to_miles_b = lambda km: km / 1.60934

# 8. Swap two numbers without third variable
swap_a = lambda a, b: (b, a)
swap_b = lambda a, b: (a ^ b ^ a, a ^ b ^ b) if all(isinstance(x, int) for x in (a, b)) else (b, a)

# 9. Simple interest
simple_interest_a = lambda p, r, t: (p * r * t) / 100
simple_interest_b = lambda p, r, t: p * (r / 100) * t

# 10. Compound interest (amount)
compound_amount_a = lambda p, r, n, t: p * pow(1 + r / (100 * n), n * t)
compound_amount_b = lambda p, r, n, t: p * math.exp((n * t) * math.log(1 + r / (100 * n)))

# 11. Even or odd
is_even_a = lambda n: (n % 2) == 0
is_even_b = lambda n: (n & 1) == 0

# 12. Max of three
max_three_a = lambda a, b, c: max(a, b, c)
max_three_b = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)

# 13. Min of three
min_three_a = lambda a, b, c: min(a, b, c)
min_three_b = lambda a, b, c: a if (a <= b and a <= c) else (b if b <= c else c)

# 14. Average of three
avg_three_a = lambda a, b, c: (a + b + c) / 3
avg_three_b = lambda a, b, c: sum((a, b, c)) / 3

# 15. Remainder a % b
remainder_a = lambda a, b: a % b
remainder_b = lambda a, b: divmod(a, b)[1]

###############################################
# 2. Control Statements & Loops (16–35)
###############################################

# 16. Natural numbers 1..N
naturals_a = lambda n: list(range(1, n + 1))
naturals_b = lambda n: [i for i in range(1, n + 1)]

# 17. Evens 1..100
E_HUNDRED = tuple(range(2, 101, 2))
evens_1_100_a = lambda: list(E_HUNDRED)
evens_1_100_b = lambda: [i for i in range(1, 101) if i % 2 == 0]

# 18. Odds 1..100
odds_1_100_a = lambda: [i for i in range(1, 101, 2)]
odds_1_100_b = lambda: [i for i in range(1, 101) if i % 2 == 1]

# 19. Sum of first N naturals
sum_naturals_a = lambda n: n * (n + 1) // 2
sum_naturals_b = lambda n: sum(range(1, n + 1))

# 20. Factorial
factorial_a = lambda n: math.prod(range(1, n + 1)) if n >= 0 else None

def factorial_b(n: int) -> int:
    if n < 2:
        return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

# 21. Multiplication table
table_a = lambda n, upto=10: [n * i for i in range(1, upto + 1)]
table_b = lambda n, upto=10: list(map(lambda i: n * i, range(1, upto + 1)))

# 22. Count digits
count_digits_a = lambda n: len(str(abs(int(n))))
count_digits_b = lambda n: 1 if n == 0 else int(math.log10(abs(n))) + 1

# 23. Reverse a number
reverse_number_a = lambda n: int(str(abs(n))[::-1]) * (1 if n >= 0 else -1)

def reverse_number_b(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n:
        rev = rev * 10 + (n % 10)
        n //= 10
    return sign * rev

# 24. Palindrome number
is_pal_number_a = lambda n: str(n) == str(n)[::-1]

def is_pal_number_b(n: int) -> bool:
    s = str(n)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# 25. Armstrong number (3-digit or generalized)
armstrong_a = lambda n: n == sum(int(d) ** len(str(n)) for d in str(n))

def armstrong_b(n: int) -> bool:
    s = str(n)
    p = len(s)
    return n == sum(pow(int(ch), p) for ch in s)

# 26. Fibonacci up to N terms
fib_series_a = lambda n: list(it.islice(_fib_inf(), n))

def _fib_inf():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fib_series_b(n: int) -> List[int]:
    if n <= 0:
        return []
    a, b = 0, 1
    out = []
    for _ in range(n):
        out.append(a)
        a, b = b, a + b
    return out

# 27. Sum of digits
sum_digits_a = lambda n: sum(int(d) for d in str(abs(n)))

def sum_digits_b(n: int) -> int:
    n = abs(n)
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

# 28. Product of digits
product_digits_a = lambda n: math.prod(int(d) for d in str(abs(n))) if n != 0 else 0

def product_digits_b(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    p = 1
    while n:
        p *= (n % 10)
        n //= 10
    return p

# 29. Count even/odd digits
count_even_odd_digits_a = lambda n: (
    sum((int(d) % 2 == 0) for d in str(abs(n))),
    sum((int(d) % 2 == 1) for d in str(abs(n))),
)

def count_even_odd_digits_b(n: int) -> Tuple[int, int]:
    n = abs(n)
    ev = od = 0
    if n == 0:
        return (1, 0)
    while n:
        d = n % 10
        if (d & 1) == 0:
            ev += 1
        else:
            od += 1
        n //= 10
    return (ev, od)

# 30. Largest digit
largest_digit_a = lambda n: max(int(d) for d in str(abs(n)))

def largest_digit_b(n: int) -> int:
    n = abs(n)
    m = 0
    while n:
        m = max(m, n % 10)
        n //= 10
    return m

# 31. Smallest digit
smallest_digit_a = lambda n: min(int(d) for d in str(abs(n)))

def smallest_digit_b(n: int) -> int:
    n = abs(n)
    m = 9
    if n == 0:
        return 0
    while n:
        m = min(m, n % 10)
        n //= 10
    return m

# 32. Power using loop
power_loop_a = lambda base, exp: base ** exp if isinstance(exp, int) and exp >= 0 else base ** exp

def power_loop_b(base: float, exp: int) -> float:
    if exp < 0:
        base, exp = 1 / base, -exp
    res = 1.0
    for _ in range(exp):
        res *= base
    return res

# 33. Primes 1..100
primes_1_100_a = lambda: [n for n in range(2, 101) if all(n % d for d in range(2, int(n ** 0.5) + 1))]

def primes_1_100_b() -> List[int]:
    N = 100
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(N ** 0.5) + 1):
        if sieve[p]:
            for m in range(p * p, N + 1, p):
                sieve[m] = False
    return [i for i, ok in enumerate(sieve) if ok]

# 34. Prime check
is_prime_a = lambda n: n >= 2 and all(n % d for d in range(2, int(n ** 0.5) + 1))

def is_prime_b(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

# 35. GCD
gcd_a = math.gcd

def gcd_b(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

###############################################
# 3. Functions (36–55)
###############################################

# 36. even/odd function
is_even_func_a = is_even_a
is_even_func_b = lambda n: not (n & 1)

# 37. factorial function
fact_func_a = factorial_a
fact_func_b = factorial_b

# 38. palindrome number func
pal_num_func_a = is_pal_number_a
pal_num_func_b = is_pal_number_b

# 39. fibonacci function
fib_func_a = fib_series_a
fib_func_b = fib_series_b

# 40. power function
power_func_a = power_loop_b
power_func_b = pow

# 41. prime check function
prime_func_a = is_prime_a
prime_func_b = is_prime_b

# 42. sum of digits
sum_digits_func_a = sum_digits_a
sum_digits_func_b = sum_digits_b

# 43. count vowels in string
count_vowels_a = lambda s: sum(ch.lower() in "aeiou" for ch in s)
count_vowels_b = lambda s: sum(1 for ch in s if ch in set("aeiouAEIOU"))

# 44. area of triangle
area_triangle_a = lambda b, h: (b * h) / 2
area_triangle_b = lambda a, b, c: math.sqrt(((a + b + c) / 2) * (((a + b + c) / 2) - a) * (((a + b + c) / 2) - b) * (((a + b + c) / 2) - c))

# 45. max of three
max_three_func_a = max_three_a
max_three_func_b = max_three_b

# 46. min of three
min_three_func_a = min_three_a
min_three_func_b = min_three_b

# 47. string palindrome
str_pal_a = lambda s: s == s[::-1]

def str_pal_b(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# 48. reverse string
reverse_str_a = lambda s: s[::-1]
reverse_str_b = lambda s: "".join(reversed(s))

# 49. factorial recursion

def fact_rec_a(n: int) -> int:
    return 1 if n <= 1 else n * fact_rec_a(n - 1)

fact_rec_b = fact_rec_a

# 50. print table of a number (return list)
print_table_a = table_a
print_table_b = table_b

# 51. perfect number
is_perfect_a = lambda n: n == sum(d for d in range(1, n) if n % d == 0)

def is_perfect_b(n: int) -> bool:
    if n < 2:
        return False
    s = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            s += d
            if d * d != n:
                s += n // d
        d += 1
    return s == n

# 52. sum of list elements
sum_list_a = lambda xs: sum(xs)
sum_list_b = lambda xs: math.fsum(xs)

# 53. max element in list
max_list_a = max
max_list_b = lambda xs: sorted(xs)[-1]

# 54. min element in list
min_list_a = min
min_list_b = lambda xs: sorted(xs)[0]

# 55. list sorted
is_sorted_a = lambda xs: all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1))
is_sorted_b = lambda xs: xs == sorted(xs)

###############################################
# 4. String Manipulation (56–80)
###############################################

# 56. Count vowels and consonants
count_vowels_consonants_a = lambda s: (
    sum(ch.lower() in "aeiou" for ch in s if ch.isalpha()),
    sum(ch.isalpha() and ch.lower() not in "aeiou" for ch in s),
)

def count_vowels_consonants_b(s: str) -> Tuple[int, int]:
    vowels = set("aeiouAEIOU")
    v = sum(1 for ch in s if ch in vowels)
    c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return v, c

# 57. Count words
count_words_a = lambda s: len(s.split())
count_words_b = lambda s: sum(1 for _ in filter(None, s.split(" ")))

# 58. Reverse string
reverse_string_a = reverse_str_a
reverse_string_b = reverse_str_b

# 59. Anagrams
are_anagrams_a = lambda a, b: sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())
are_anagrams_b = lambda a, b: Counter(a.replace(" ", "").lower()) == Counter(b.replace(" ", "").lower())

# 60. Remove spaces
remove_spaces_a = lambda s: s.replace(" ", "")
remove_spaces_b = lambda s: "".join(ch for ch in s if ch != " ")

# 61–62. Case conversions
upper_a = str.upper
upper_b = lambda s: "".join(ch.upper() for ch in s)
lower_a = str.lower
lower_b = lambda s: "".join(ch.lower() for ch in s)

# 63. Toggle case
toggle_case_a = lambda s: "".join(ch.lower() if ch.isupper() else ch.upper() if ch.islower() else ch for ch in s)

def toggle_case_b(s: str) -> str:
    out = []
    for ch in s:
        if ch.islower():
            out.append(ch.upper())
        elif ch.isupper():
            out.append(ch.lower())
        else:
            out.append(ch)
    return "".join(out)

# 64. Count occurrences of each char
count_chars_a = lambda s: dict(Counter(s))

def count_chars_b(s: str) -> Dict[str, int]:
    d: Dict[str, int] = {}
    for ch in s:
        d[ch] = d.get(ch, 0) + 1
    return d

# 65. Frequency of specific char
char_freq_a = lambda s, ch: s.count(ch)
char_freq_b = lambda s, ch: sum(1 for c in s if c == ch)

# 66. Replace word
replace_word_a = lambda s, old, new: s.replace(old, new)
replace_word_b = lambda s, old, new: (new).join(s.split(old))

# 67. Remove vowels
remove_vowels_a = lambda s: "".join(ch for ch in s if ch.lower() not in "aeiou")
remove_vowels_b = lambda s: re_sub_vowels(s)

def re_sub_vowels(s: str) -> str:
    import re
    return re.sub(r"[aeiouAEIOU]", "", s)

# 68. Remove special characters
remove_specials_a = lambda s: "".join(ch for ch in s if ch.isalnum() or ch.isspace())

def remove_specials_b(s: str) -> str:
    import re
    return re.sub(r"[^\w\s]", "", s)

# 69. Length without len()
length_without_len_a = lambda s: sum(1 for _ in s)

def length_without_len_b(s: str) -> int:
    i = 0
    for _ in s:
        i += 1
    return i

# 70. Only digits
only_digits_a = str.isdigit
only_digits_b = lambda s: all(ch.isdigit() for ch in s) and s != ""

# 71. Count alphabets, digits, symbols
count_types_a = lambda s: (
    sum(ch.isalpha() for ch in s),
    sum(ch.isdigit() for ch in s),
    sum(not (ch.isalnum() or ch.isspace()) for ch in s),
)

def count_types_b(s: str) -> Tuple[int, int, int]:
    a = d = sym = 0
    for ch in s:
        if ch.isalpha():
            a += 1
        elif ch.isdigit():
            d += 1
        elif not ch.isspace():
            sym += 1
    return a, d, sym

# 72. All substrings
all_substrings_a = lambda s: [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

def all_substrings_b(s: str) -> List[str]:
    out = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            out.append(s[i:j])
    return out

# 73. Substring check
is_substring_a = lambda a, b: a in b
is_substring_b = lambda a, b: b.find(a) != -1

# 74. First non-repeating char
first_non_repeating_a = lambda s: next((ch for ch, c in Counter(s).items() if c == 1), None)

def first_non_repeating_b(s: str) -> str | None:
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None

# 75. Most repeated char
most_repeated_char_a = lambda s: Counter(s).most_common(1)[0][0] if s else None

def most_repeated_char_b(s: str) -> str | None:
    if not s:
        return None
    counts = Counter(s)
    m = max(counts.values())
    for ch, c in counts.items():
        if c == m:
            return ch
    return None

# 76. Sort characters alphabetically
sort_chars_a = lambda s: "".join(sorted(s))
sort_chars_b = lambda s: "".join(sorted(list(s)))

# 77. Concatenate without +
concat_no_plus_a = lambda a, b: "".join([a, b])
concat_no_plus_b = lambda a, b: f"{a}{b}"

# 78. Count upper/lowercase
count_upper_lower_a = lambda s: (
    sum(ch.isupper() for ch in s),
    sum(ch.islower() for ch in s),
)
count_upper_lower_b = lambda s: tuple(map(sum, zip(*[((1, 0) if ch.isupper() else (0, 1)) for ch in s if ch.isalpha()])))

# 79. Reverse order of words
reverse_words_order_a = lambda s: " ".join(reversed(s.split()))
reverse_words_order_b = lambda s: " ".join(s.split()[::-1])

# 80. Capitalize first letter of each word
capitalize_words_a = lambda s: s.title()
capitalize_words_b = lambda s: " ".join(w[:1].upper() + w[1:].lower() if w else w for w in s.split(" "))

###############################################
# 5. List Programs (81–105)
###############################################

sum_list2_a = sum_list_a
sum_list2_b = sum_list_b

avg_list_a = lambda xs: (sum(xs) / len(xs)) if xs else 0
avg_list_b = lambda xs: (math.fsum(xs) / len(xs)) if xs else 0

max_min_list_a = lambda xs: (max(xs), min(xs))
max_min_list_b = lambda xs: (sorted(xs)[-1], sorted(xs)[0])

remove_duplicates_a = lambda xs: list(dict.fromkeys(xs))
remove_duplicates_b = lambda xs: list(set(xs))

reverse_list_a = lambda xs: list(reversed(xs))
reverse_list_b = lambda xs: xs[::-1]

sort_asc_a = lambda xs: sorted(xs)
sort_asc_b = lambda xs: list(sorted(xs))

sort_desc_a = lambda xs: sorted(xs, reverse=True)
sort_desc_b = lambda xs: list(sorted(xs, reverse=True))

second_largest_a = lambda xs: sorted(set(xs))[-2] if len(set(xs)) >= 2 else None
second_largest_b = lambda xs: max(x for x in xs if x != max(xs)) if len(set(xs)) >= 2 else None

second_smallest_a = lambda xs: sorted(set(xs))[1] if len(set(xs)) >= 2 else None
second_smallest_b = lambda xs: min(x for x in xs if x != min(xs)) if len(set(xs)) >= 2 else None

count_occurrences_a = lambda xs, x: xs.count(x)
count_occurrences_b = lambda xs, x: Counter(xs)[x]

merge_lists_a = lambda a, b: a + b
merge_lists_b = lambda a, b: [*a, *b]

common_elements_a = lambda a, b: list(set(a) & set(b))
common_elements_b = lambda a, b: [x for x in a if x in set(b)]

only_in_a_a = lambda a, b: list(set(a) - set(b))
only_in_a_b = lambda a, b: [x for x in a if x not in set(b)]

square_each_a = lambda xs: [x * x for x in xs]
square_each_b = lambda xs: list(map(lambda x: x * x, xs))

remove_evens_a = lambda xs: [x for x in xs if x % 2 == 1]
remove_evens_b = lambda xs: list(filter(lambda x: x % 2 == 1, xs))

remove_odds_a = lambda xs: [x for x in xs if x % 2 == 0]
remove_odds_b = lambda xs: list(filter(lambda x: x % 2 == 0, xs))

find_index_a = lambda xs, x: (xs.index(x) if x in xs else -1)

def find_index_b(xs: List[Any], x: Any) -> int:
    for i, v in enumerate(xs):
        if v == x:
            return i
    return -1

product_of_list_a = lambda xs: math.prod(xs) if xs else 1

def product_of_list_b(xs: Iterable[float]) -> float:
    p = 1
    for v in xs:
        p *= v
    return p

replace_negatives_a = lambda xs: [x if x >= 0 else 0 for x in xs]
replace_negatives_b = lambda xs: list(map(lambda x: x if x >= 0 else 0, xs))

insert_at_index_a = lambda xs, i, val: xs[:i] + [val] + xs[i:]

def insert_at_index_b(xs: List[Any], i: int, val: Any) -> List[Any]:
    ys = xs.copy()
    ys.insert(i, val)
    return ys

list_palindrome_a = lambda xs: xs == xs[::-1]
list_palindrome_b = lambda xs: all(xs[i] == xs[-i - 1] for i in range(len(xs) // 2))

even_positions_a = lambda xs: [xs[i] for i in range(1, len(xs), 2)]
even_positions_b = lambda xs: [v for i, v in enumerate(xs) if (i % 2 == 1)]

odd_positions_a = lambda xs: [xs[i] for i in range(0, len(xs), 2)]
odd_positions_b = lambda xs: [v for i, v in enumerate(xs) if (i % 2 == 0)]

separate_pos_neg_a = lambda xs: ([x for x in xs if x >= 0], [x for x in xs if x < 0])

def separate_pos_neg_b(xs: Iterable[int]) -> Tuple[List[int], List[int]]:
    pos, neg = [], []
    for x in xs:
        (pos if x >= 0 else neg).append(x)
    return pos, neg

range_diff_a = lambda xs: (max(xs) - min(xs)) if xs else 0
range_diff_b = lambda xs: (sorted(xs)[-1] - sorted(xs)[0]) if xs else 0

###############################################
# 6. Tuple & Set Programs (106–120)
###############################################

create_tuple_access_a = lambda *xs: (xs, xs[0] if xs else None)
create_tuple_access_b = lambda *xs: (tuple(xs), (tuple(xs)[-1] if xs else None))

len_tuple_a = lambda t: len(t)
len_tuple_b = lambda t: sum(1 for _ in t)

convert_tuple_list_a = lambda t: list(t)
convert_list_tuple_a = lambda xs: tuple(xs)
convert_tuple_list_b = lambda t: [*t]
convert_list_tuple_b = lambda xs: (*xs,)

max_min_tuple_a = lambda t: (max(t), min(t))
max_min_tuple_b = lambda t: (sorted(t)[-1], sorted(t)[0])

sum_tuple_a = lambda t: sum(t)
sum_tuple_b = lambda t: math.fsum(t)

concat_tuples_a = lambda a, b: a + b
concat_tuples_b = lambda a, b: (*a, *b)

element_in_tuple_a = lambda t, x: x in t
element_in_tuple_b = lambda t, x: any(v == x for v in t)

count_in_tuple_a = lambda t, x: t.count(x)
count_in_tuple_b = lambda t, x: sum(1 for v in t if v == x)

index_in_tuple_a = lambda t, x: (t.index(x) if x in t else -1)
index_in_tuple_b = lambda t, x: next((i for i, v in enumerate(t) if v == x), -1)

create_set_add_a = lambda xs: set(xs)

def create_set_add_b(xs: Iterable[Any]) -> set:
    s = set()
    for x in xs:
        s.add(x)
    return s

remove_from_set_a = lambda s, x: (s - {x}) if x in s else set(s)

def remove_from_set_b(s: set, x: Any) -> set:
    s2 = set(s)
    s2.discard(x)
    return s2

union_sets_a = lambda a, b: a | b
union_sets_b = lambda a, b: set(it.chain(a, b))

intersection_sets_a = lambda a, b: a & b
intersection_sets_b = lambda a, b: {x for x in a if x in b}

difference_sets_a = lambda a, b: a - b
difference_sets_b = lambda a, b: {x for x in a if x not in b}

is_subset_a = lambda a, b: a <= b
is_subset_b = lambda a, b: all(x in b for x in a)

###############################################
# 7. Dictionary Programs (121–140)
###############################################

create_dict_print_keys_a = lambda d: list(d.keys())
create_dict_print_keys_b = lambda d: [k for k in d]

values_from_dict_a = lambda d: list(d.values())
values_from_dict_b = lambda d: [d[k] for k in d]

add_kv_a = lambda d, k, v: {**d, k: v}

def add_kv_b(d: Dict[Any, Any], k: Any, v: Any) -> Dict[Any, Any]:
    nd = dict(d)
    nd[k] = v
    return nd

remove_key_a = lambda d, k: {kk: vv for kk, vv in d.items() if kk != k}

def remove_key_b(d: Dict[Any, Any], k: Any) -> Dict[Any, Any]:
    nd = dict(d)
    nd.pop(k, None)
    return nd

key_exists_a = lambda d, k: k in d
key_exists_b = lambda d, k: any(kk == k for kk in d)

freq_via_dict_a = lambda xs: dict(Counter(xs))

def freq_via_dict_b(xs: Iterable[Any]) -> Dict[Any, int]:
    d: Dict[Any, int] = defaultdict(int)
    for x in xs:
        d[x] += 1
    return dict(d)

merge_dicts_a = lambda a, b: {**a, **b}

def merge_dicts_b(a: Dict[Any, Any], b: Dict[Any, Any]) -> Dict[Any, Any]:
    m = dict(a)
    m.update(b)
    return m

key_with_max_value_a = lambda d: max(d, key=d.get) if d else None

def key_with_max_value_b(d: Dict[Any, Any]) -> Any | None:
    best_k, best_v = None, None
    for k, v in d.items():
        if best_v is None or v > best_v:
            best_k, best_v = k, v
    return best_k

key_with_min_value_a = lambda d: min(d, key=d.get) if d else None

def key_with_min_value_b(d: Dict[Any, Any]) -> Any | None:
    best_k, best_v = None, None
    for k, v in d.items():
        if best_v is None or v < best_v:
            best_k, best_v = k, v
    return best_k

invert_dict_a = lambda d: {v: k for k, v in d.items()}

def invert_dict_b(d: Dict[Any, Any]) -> Dict[Any, Any]:
    inv: Dict[Any, Any] = {}
    for k, v in d.items():
        inv[v] = k
    return inv

sort_dict_by_key_a = lambda d: dict(sorted(d.items()))
sort_dict_by_key_b = lambda d: {k: d[k] for k in sorted(d)}

sort_dict_by_value_a = lambda d: dict(sorted(d.items(), key=lambda kv: kv[1]))

def sort_dict_by_value_b(d: Dict[Any, Any]) -> Dict[Any, Any]:
    return dict(sorted(d.items(), key=lambda kv: kv[1]))

sum_of_values_a = lambda d: sum(d.values())
sum_of_values_b = lambda d: math.fsum(d.values())

from_two_lists_a = lambda keys, vals: dict(zip(keys, vals))

def from_two_lists_b(keys: Iterable[Any], vals: Iterable[Any]) -> Dict[Any, Any]:
    d: Dict[Any, Any] = {}
    for k, v in zip(keys, vals):
        d[k] = v
    return d

remove_duplicate_values_a = lambda d: {k: v for k, v in d.items() if list(d.values()).index(v) == list(d.values())[:list(d.keys()).index(k)+1].count(v)-1}

def remove_duplicate_values_b(d: Dict[Any, Any]) -> Dict[Any, Any]:
    seen = set()
    out: Dict[Any, Any] = {}
    for k, v in d.items():
        if v not in seen:
            out[k] = v
            seen.add(v)
    return out

unique_values_only_a = lambda d: list(set(d.values()))
unique_values_only_b = lambda d: [*{*d.values()}]

dicts_equal_a = lambda a, b: a == b

def dicts_equal_b(a: Dict[Any, Any], b: Dict[Any, Any]) -> bool:
    if a.keys() != b.keys():
        return False
    for k in a:
        if a[k] != b[k]:
            return False
    return True

combine_multiple_dicts_a = lambda dicts: dict(it.chain.from_iterable(d.items() for d in dicts))

def combine_multiple_dicts_b(dicts: Iterable[Dict[Any, Any]]) -> Dict[Any, Any]:
    out: Dict[Any, Any] = {}
    for d in dicts:
        out.update(d)
    return out

squares_1_to_10_a = lambda: {i: i * i for i in range(1, 11)}
squares_1_to_10_b = lambda: dict(map(lambda i: (i, i * i), range(1, 11)))

char_count_dict_a = lambda s: dict(Counter(s))

def char_count_dict_b(s: str) -> Dict[str, int]:
    d: Dict[str, int] = {}
    for ch in s:
        d[ch] = d.get(ch, 0) + 1
    return d

###############################################
# 8. Miscellaneous Logical Problems (141–150)
###############################################

# 141. Pascal's Triangle

def pascal_triangle_a(rows: int) -> List[List[int]]:
    tri: List[List[int]] = []
    for r in range(rows):
        row = [1] * (r + 1)
        for c in range(1, r):
            row[c] = tri[r - 1][c - 1] + tri[r - 1][c]
        tri.append(row)
    return tri

pascal_triangle_b = lambda rows: [
    [math.comb(r, c) for c in range(r + 1)] for r in range(rows)
]

# 142. All primes up to N
primes_upto_a = lambda n: [x for x in range(2, n + 1) if all(x % d for d in range(2, int(x ** 0.5) + 1))]

def primes_upto_b(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for m in range(p * p, n + 1, p):
                sieve[m] = False
    return [i for i, ok in enumerate(sieve) if ok]

# 143. Perfect numbers up to N
perfects_upto_a = lambda n: [x for x in range(2, n + 1) if is_perfect_b(x)]
perfects_upto_b = lambda n: [x for x in range(2, n + 1) if x == sum(d for d in range(1, x) if x % d == 0)]

# 144. Sum of primes up to N
sum_primes_upto_a = lambda n: sum(primes_upto_b(n))

def sum_primes_upto_b(n: int) -> int:
    s = 0
    for x in range(2, n + 1):
        if is_prime_b(x):
            s += x
    return s

# 145. Star pyramid (return as list of strings)
star_pyramid_a = lambda h: [" " * (h - i - 1) + "*" * (2 * i + 1) for i in range(h)]

def star_pyramid_b(h: int) -> List[str]:
    lines: List[str] = []
    for i in range(h):
        spaces = " " * (h - i - 1)
        stars = "*" * (2 * i + 1)
        lines.append(spaces + stars)
    return lines

# 146. Number triangle
number_triangle_a = lambda h: [" ".join(str(j + 1) for j in range(i + 1)) for i in range(h)]

def number_triangle_b(h: int) -> List[str]:
    lines: List[str] = []
    for i in range(h):
        lines.append(" ".join(map(str, range(1, i + 2))))
    return lines

# 147. Leap year
leap_year_a = lambda y: (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
leap_year_b = lambda y: (not (y % 400)) or ((not (y % 4)) and (y % 100 != 0))

# 148. Decimal to binary (string)
dec_to_bin_a = lambda n: bin(n)[2:]

def dec_to_bin_b(n: int) -> str:
    if n == 0:
        return "0"
    bits = []
    while n:
        bits.append("1" if (n & 1) else "0")
        n >>= 1
    return "".join(reversed(bits))

# 149. Binary to decimal
bin_to_dec_a = lambda s: int(s, 2)

def bin_to_dec_b(s: str) -> int:
    v = 0
    for ch in s:
        v = v * 2 + (1 if ch == "1" else 0)
    return v

# 150. LCM of two numbers
lcm_a = lambda a, b: abs(a * b) // math.gcd(a, b) if a and b else 0

def lcm_b(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd_b(a, b) * b)


if __name__ == "__main__":
    # Minimal demo
    print("Add two numbers:", add_two_numbers_a(3, 5), add_two_numbers_b([3, 5]))
    print("Factorial:", factorial_a(5), factorial_b(5))
    print("Primes 1..20:", primes_upto_b(20))
    print("Star pyramid h=3:\n" + "\n".join(star_pyramid_a(3)))
