#5.1
store = 'target'
print("Is store =='target'? I predict True:")
print(store == 'target')

print("Is store == 'walmart'? I predict False:")
print(store == 'walmart')

plants = 'cebu blue'
print("Is plants =='cebu blue'? I predict Ture:")
print(plants == 'cebu blue')

print("Is plants == 'ppp'? I predict False:")
print(plants == 'ppp')

baby = 'Neo'
print("Is baby =='Neo'? I predict Ture:")
print(baby == 'Neo')

print("Is baby == 'Sam'? I predict False:")
print(baby== 'Sam')

candy = 'Air Head'
print("Is candy =='Air Head'? I predict Ture:")
print(candy == 'Air Head')

print("Is candy == 'M&M'? I predict False:")
print(candy == 'M&M')

drink = 'coffee'
print("Is store =='target'? I predict Ture:")
print(drink == 'coffee')

print("Is store == 'tea'? I predict False:")
print(drink == 'tea')

#5.2
#a attached picture in 'tryityourself5 answers'
#b
names = ['Morty', 'Rick', 
		 'Summer', 'Beth', 	
		 'Jerry']

for names in names:
    if names == 'Morty':
        print(names.upper())
    else:
        print(names.lower())

#c, d, and e attached picture in 'tryityourself5 answers'
#f
fruits = ['Jackfruit', 'Mango',
		  'Durian']

veggie = 'bok choi'
if veggie not in fruits:
    print(f'{veggie.title()} is not a fruit.')

#5.3
alien_color = 'green'
if alien_color == 'green':
    print("Player 1 just earned 5 points.")

if alien_color == 'purple':
    print("Player 1 just earned 5 points.")

#5.4
alien_color = 'Purple'

if alien_color == 'Purple':
    print("Player 1 earned 5 points.")
else:
    print("Player 1 earned 10 points.")

alien_color = 'Pink'

if alien_color == 'Yellow':
    print("Player 2 earned 5 points.")

else:
    print("Player 2 earned 10 points.")

#5.5
alien_color = 'Blue'

if alien_color == 'Pink':
    print("Player 1 earned 5 points.")

elif alien_color == 'Yellow':
    print("Player 1 earned 10 points.")

else:
    print("Player 1 earned 15 points.")

alien_color = 'Pink'

if alien_color == 'Pink':
    print("Player 1 earned 5 points.")

elif alien_color == 'Yellow':
    print("Player 1 earned 10 points.")

else:
    print("Player 1 earned 15 points.")

alien_color = 'Yellow'

if alien_color == 'Pink':
    print("Player 1 earned 5 points.")

elif alien_color == 'Yellow':
    print("Player 1 earned 10 points.")

else:
    print("Player 1 earned 15 points.")

#5.6
age = 66

if age < 2:
    print("You're a baby.")
elif (age >= 2) and (age <= 4):
    print("You're a toddler.") 

elif (age >= 4) and (age <= 13):
    print("You're a kid.") 

elif (age >= 13) and (age <= 20):
    print("You're a teenager.") 

elif (age >= 20) and (age <= 65):
    print("You're a adult.") 

else:
    print("You're an eldery.")

#5.7
favorite_fruits = ['mangosteen', 'lychee', 
				   'mata kuching']

if 'mata kuching' in favorite_fruits:
    print("I love mata kuching")
if 'mangosteen' in favorite_fruits:
    print("I love mangosteen")
if 'durian' in favorite_fruits:
    print("I love durian")

print("\nI love Malaysian fruits!")

#5.8
usernames = ['mictchell', 'melissa', 'matt',
              'joe', 'jenna', 'admin']
for usernames in usernames:
    if usernames == 'admin':
        print("Hello admin, would you like to see a status report?")
    else: 
        print(f'Hello {usernames.title()}, thank you for logging in again.')

#5.9
usernames = []
if usernames:
    for usernames in usernames:
        if usernames == 'admin':
            print("Hello admin, would you like to see a status report?")
else: 
    print("We need to find some users!")

#5.10
current_users = ['mitchell', 'melissa', 'matt',
                 'Neo', 'admin', 'chris']

new_users = ['jon', 'neo', 'mel',
             'Mitchell', 'CHRIS']

current_users_lower = []
for x in current_users:
    current_users_lower.append(x.lower())

for new_users in new_users:
    if new_users.lower() in current_users_lower:
        print(f"Username {new_users} is not available.")
    else: 
        print(f"{new_users} is still available.")

#5.11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numbers in numbers:
    if numbers == 1:
        print("1st")
    elif numbers == 2:
        print("2nd")
    elif numbers == 3:
        print("3rd")
    else:
        print(f"{numbers}th")

    
