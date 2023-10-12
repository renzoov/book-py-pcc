request_topping = "mushrooms"

if request_topping != "anchovies":
  print("Hold the anchovies!")
  
print("\n------------------------------\n")
  
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
  print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
  print("Adding pepperoni.")
  
for requested_topping in requested_toppings:
  print(f"Adding {requested_topping}.")
  
print("\nFinished making your pizza!")

print("\n------------------------------\n")

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print(f"Adding {requested_topping}.")
  else:
    print(f"Sorry, we don't have {requested_topping}.")
    
print("\nFinished making your pizza!")

print("\n------------------------------\n")