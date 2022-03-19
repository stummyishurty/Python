#7.1
car = input("[?] What kind of car would you like:")
print(f"Let me see if I can find you a {car}.")

#7.2
dinner = input("[?] How many people are in your dinner group:")
dinner = int(dinner)

if dinner >= 8 :
    print("You will have to wait for a table.")
else: 
    print("You table is ready!")

#7.3
number = input("[!]Enter a number:")
number = int(number)

if number % 10 == 0:
    print(f"YEPPPP,{number} it is a multiple of 10.")

else: 
    print(f"NOPEEE, {number} is not a multiple of 10.")

#7.4
prompt = "[?] Please enter your pizza toppings:"
prompt += "\n(Enter 'quit' when you're done choosing your toppings)"

while True:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        break

    else:
        print(f"{pizza_topping.title()} added to your pizza.")

#7.5
prompt = "[?] Enter age:"
prompt += "\n(Enter 'quit' when you're finished.)"

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3 :
        print("You get a free ticket.")

    elif age <= 13:
        print("Your ticket is $10.")

    else:
        print("Your ticket is $15.")

#7.6
prompt = "[?] Please enter your pizza toppings:"
prompt += "\n(Enter 'quit' when you're done choosing your toppings)"

active = True
while active:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        active = False
        break

    else:
        print(f"{pizza_topping.title()} added to your pizza.")


#7.8
sandwich_order =['chicken', 'tuna', 'beef']
finished_sandwiches =[]

while sandwich_order:
    making_sandwich = sandwich_order.pop()
    print(f"\nYour {making_sandwich} sandwich is being made")
    finished_sandwiches.append(making_sandwich)

for sandwich in finished_sandwiches:
    print(f"\nYour {sandwich} sandwich is ready for pickup.")

#7.9
sandwich_order =[
                 'chicken', 'pastrami', 'tuna', 
                 'pastrami', 'beef', 'pastrami',
                 ]

finished_sandwiches =[]

while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')
print("Sorry, but we ran out of pastami :(")

while sandwich_order:
    making_sandwich = sandwich_order.pop()
    print(f"\nYour {making_sandwich} sandwich is being made")
    finished_sandwiches.append(making_sandwich)

for sandwich in finished_sandwiches:
    print(f"\nYour {sandwich} sandwich is ready for pickup.")

#7.10
dream_vacation = {}

active = True

while active:
    name = input("\nEnter name:")
    place = input("[?] If you could visit one place in the world, where would you go:")

    dream_vacation[name] = place

    repeat = input("[?] Is there anywhere else you would like to visit:(yes/ no)")
    if repeat == 'no':
        active = False

print("\n---Poll results---")
for name, place in dream_vacation.items():
    print(f"{name} would love to visit {place}.")