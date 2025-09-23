my_dict = {"omkar":23,"mahesh":24,"lakhan":25,"hemesh":26,"pratik":27}

print(my_dict)

my_dict["ram"]= 90
print(my_dict)

my_dict["lakhan"] = 80
print(my_dict)

del my_dict["pratik"]
print(my_dict)

if "lakhan" in my_dict:
    print("the lakhan is present in the dictionary")
else:
    print("not present in dictionary")    
    
for i in my_dict:
    print(i)    
    
for i in my_dict.values():
    print(i)    
    
for i , j in my_dict .items():
        print(f"{i}:{j}")  

print(len(my_dict))          

my_dict.update({"sumit":23,"rohan":40})
print(my_dict)


keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
dict1 = dict(zip(keys, values))
print(dict1)

sorted_keys = dict(sorted(my_dict.items(), key=lambda x: x[0]))
print(sorted_keys)
sorted_items = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(f" {sorted_items}")

highest =max(my_dict.values())
print(highest)

lowest = min(my_dict.values())
print(lowest)

sentence = "programming"
char_frequency ={}
for i in sentence:
    char_frequency[i] = char_frequency.get(i,0) + 1
print(char_frequency)

square_dict = {key: key**2 for key in range(1,11)}
print(square_dict)

reversed_dict = {num : str(num)[::-1] for num in range(1,11)}
print(reversed_dict)

student_info = {
    "student1":{"name":"omkar","age":23,"gender":"male"},
    "student2":{"name":"pratik","age":21,"gender":"male"}   
    
}
print(student_info)

sentence = "programers house"
word = sentence.split()
frequency = {}
for i in sentence:
    frequency[i] = frequency.get(i,0) + 1
print(frequency)




# Write a program to swap keys and values in a dictionary (handle duplicate values).
keys = {"apple":1,"banana":2,"cherry":3,"date":4,"elderberry":5}
swapped_dict = {value:key for key,value in keys.items()}
print(swapped_dict)
# Write a program to remove all duplicate values from a dictionary.
dict3 = {"W":23,"m":54 ,"n":23,"o":54,}
swapped_dict = {value:key for key,value in keys.items()}
for key,value in dict3.items():
     if value in swapped_dict.values():
            swapped_dict.pop(value)
print(dict3)
# Create a dictionary of numbers (1–20) and store whether each number is even or odd.
even_odd_dict = {num : "even" if num % 2 == 0 else "odd" for num in range(1,21)}
print(even_odd_dict)

# Write a program to combine two dictionaries by adding values for common keys.
dict4 = {"a":1,"b":2,"c":3,"d":4,"e":5}
dict5 = {"b":6,"c":7,"d":8,"e":9,"f":10}
combined_dict = {**dict4 , **dict5}
print(combined_dict)

# Write a program to check if two dictionaries are equal.
dictionary1 = {"a":1,"b":2,"c":3,"d":4,"e":5}
dictionary2 = {"b":6,"c":7,"d":8,"e":9,"f":10}
print(dictionary1 == dictionary2)

# Write a program to clear all elements from a dictionary.
dict6 = {"a":1,"b":2,"c":3,"d":4,"e":5}
dict6.clear()
print(dict6)
# Write a program to extract all unique values from a dictionary.
dict7 = {"a":1,"b":2,"c":3,"d":4,"e":5}
unique_values = set(dict7.values())
print(unique_values)

# Write a program to count the frequency of vowels in a given string using a dictionary.
vowels = "aeiouAEIOU"
vowel_count = {i : sentence.count(i) for i in vowels}
print(vowel_count)
# Write a program to create a dictionary where keys are subjects and values are lists of student marks.
subjects = ["maths","science","english","history"]
marks = [54,65,66,76]
student_marks = dict(zip(subjects,marks))
print(student_marks)

# Write a program to convert a list of tuples into a dictionary.
tuples = [("apple",1),("banana",2),("cherry",3)]
dict8 = dict(tuples)
print(dict8)

lists = [1,2,3,4,5,6,7,8,9,10]
dict9 = {i : i for i in lists}
print(dict9)