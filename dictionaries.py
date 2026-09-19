# has key-value pairs.
my_dict = {
    "name" : "alice" ,
    "age" : 30,
    "city" : "New York"
}

# rather than using index we use, keys.
print(my_dict["age"])
my_dict["name"] = "arbish"
my_dict["license"] = True
del my_dict["license"]
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

if "name" in my_dict:
    print("name found!!")

# updating multiple values
my_dict.update({"age" : 31, "city" : "Karachi"})
print(my_dict)