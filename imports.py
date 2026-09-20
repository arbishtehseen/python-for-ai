# import math 
# result = math.sqrt(16)
# print(result)

# from math import sqrt, pi
# result = sqrt(9) * pi
# print(result)

# import random 
# number = random.randint(1 , 10)
# choice = random.choice(["apple","banana" ,"arbish"])
# print(number)
# print(choice)

# Common built-in modules.

# Date and Time 
import datetime 
today = datetime.date.today()
print(today)

# Operating System
import os 
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name" : "Alice", "age" : 30}
json_string = json.dumps(data)
print(json_string)

# import with alias 
# import panda as pd
# df = pd.dataFrame(data)