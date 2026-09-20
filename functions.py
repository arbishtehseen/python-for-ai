# reusable block of code.

# Defining Functions
def check_weather(temp):
    if temp > 25:
        print("It's hot in here!")
    else : 
        print("Nice Weather")

def greet(first_name , last_name):
    print (f"Hello {first_name} {last_name}")


def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount 
    print(f"Total : ${final_price}")

# calculate_total(100, 0.08, 10)

# variables inside the function can't be accessed outside of it.
# yk global vs local scope.

def sum(var1 , var2):
    return var1 + var2

result = sum(2 , 2)
print(result)  
