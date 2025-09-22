dict = {"omkar":23,"mahesh":24,"lakhan":25,"hemesh":26,"pratik":27}

print(dict)

dict["ram"]= 90
print(dict)

dict["lakhan"] = 80
print(dict)

del dict["pratik"]
print(dict)

if "lakhan" in dict:
    print("the lakhan is present in the dictionary")
else:
    print("not present in dictionary")    
    
for i in dict:
    print(i)    
    
for i in dict.values():
    print(i)    
    
for i , j in dict .items():
        print(f"{i}:{j}")  

print(len(dict))          

dict.update({"sumit":23,"rohan":40})
print(dict)

# .Create a dictionary from two lists: one of keys and one of values.
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
dict1 = dict(zip(keys, values))
print(dict1)


