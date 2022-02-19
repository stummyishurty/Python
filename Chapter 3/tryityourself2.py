#3.1
name = ['rick' ,'morty' ,'summer', 'beth', 'jerry']

#3.2
message = f"\n{name[0].title()} is super smart. Could it be the megaseeds?"
print(message)
message = f"\nIs the original C-137 evil {name[1].title()} ?"
print(message)
message = f'\n{name[2].upper()} says, "Losers look stuff up while the rest of us are carpin all them diems."'
print(message)
message = f'\nSo, which {name[-2].lower()} is the real {name[3].upper()}'
print(message)
message = f"\nIs Bruce Chutback {name[-1].title()}'s secret lovechild?"
print(message)

#3.3
vehicle = ['Honda', 'Toyota', 'Audi', 'BMW', 'Nissan']
message = f'\nI sure do love myself a {vehicle[1].upper()} prius.'
print(message)

#3.4
print("\n\tLet's invite 3 people to dinner shall we?")

guest = ['edith', 'robert', 'neo']
print(guest)

#3.5 
del guest[1]
del_guest = 'robert'
print(guest)
print(f"\n\tOh no! {del_guest.title()} couldn't make it.Let's invite somebody else.")

guest.append('jon')
print(f"{guest[0].title()} You're invited!")
print(f"{guest[1].title()} You're invited!")
print(f"{guest[2].title()} You're invited!")

#3.6 
print(f"\n\tWe got a bigger table, Let's invite 3 more peeps")

guest.insert(0, 'melody')
guest.insert(3, 'morgan')
guest.append('michelle')
print(guest)
print(f"{guest[0].title()} You're invited!")
print(f"{guest[1].title()} You're invited!")
print(f"{guest[2].title()} You're invited!")
print(f"{guest[3].title()} You're invited!")
print(f"{guest[4].title()} You're invited!")
print(f"{guest[5].title()} You're invited!")

#3.7
print("\n\tOopsie daisy, the table wont't arrive on time and I only have space for 2 peeps.")
oops = guest.pop()
print(f'Sorry {oops.title()} I can only invite 2 peeps.')
oops = guest.pop()
print(f'Sorry {oops.title()} I can only invite 2 peeps.')
oops = guest.pop()
print(f'Sorry {oops.title()} I can only invite 2 peeps.')
oops = guest.pop()
print(f'Sorry {oops.title()} I can only invite 2 peeps.')
print(f"{guest[0].title()} You're invited!")
print(f"{guest[1].title()} You're invited!")

guest.remove('melody')
del guest [0]
print(guest)

#3.8 Seeing the world
places = ['Japan', 'Thailand', 'Germany', 'Switzerland', 'New Zealand']
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3.9 Screenshhot attached as 'tryityourself len'

#3.10
random = ['Plants', 'Python', 'Gym', 'Neo', 'Jon']

print("\n\tLet's practice index shall we?:")
msg = f'I enjoy growing {random[0]}.'
print(msg)
msg = f"I'm currently learning {random[1]}."
print(msg)
msg = f'I go to the {random[-3]} with {random[3]} and {random[4]}.'
print(msg)

print('\n\tHow about adding more random things?:')

random.append('Ikea')
random.insert(1, 'Target')
print(random)

print("\n\tLet's delete 'Python'.")
del random[2]
print(random)

print("\n\tLet's pop and modify an element.")
out_of_stock = random.pop()
print(random)
msg =f'{out_of_stock} was popped because the furniture that I wanted is out of stock.'
print(msg)

print("\n\tLet's remove and modify an element.")
too_much = 'Plants'
random.remove(too_much)
print(random)
msg = f'I have too much {too_much}.'
print(msg)

print("\n\tNow we have everything we wanted, let's get them sorted")
print(f'This is how original list look: {random}')
print("To sort them temporarily:")
print(sorted(random))
print("To reverse them temporarily:")
print(sorted(random, reverse=True))
print("To reverse them permanately:")
random.reverse()
print(random)
print("To reverse them back to original:")
random.reverse()
print(random)
print("To sort them permanately:")
random.sort()
print(random)
print("To revert them permanately:")
random.sort(reverse=True)
print(random)

#3.11
random = ['Plants', 'Python', 'Gym', 'Neo', 'Jon']
print(random[5])



