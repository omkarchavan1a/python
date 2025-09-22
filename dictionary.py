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