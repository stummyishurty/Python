#4.1
pizza = ['cheese', 'stuffed', 'vegie']
for pizza in pizza:
	print(f'I like {pizza.title()} pizza')
print("\nI really love pizza!")

#4.2
animal = ['dog', 'cat', 'ferret']
for animal in animal:
	print(f'{animal.title()} is a great companion.')
print("\nThey are like tiny human trapped in a fuzzy coat.")

#4.3
for value in range(1, 21):
	print(value)

#4.4
numbers = list(range(1, 3))
print(numbers)

#4.5
numbers = [1, 3]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4.6
odd_numbers = list(range(1, 21, 2))
for numbers in odd_numbers:
	print(numbers)

#4.7
multiple = list(range(3, 31, 3))
for number in multiple:
    print(number)

#4.8
cubes = []
for x in range(1, 11):
	cubes.append(x ** 3)
print(cubes)

#4.9
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

#4.10
animal = ['dog', 'cat', 'ferret', 'parrot', 'trash panda']
print(animal[:3])
print(animal[1:4])
print(animal[-3:])

#4.11
pizza = ['cheese', 'stuffed', 'veggie']
friends_fav = pizza[:]

pizza.append('sausage')
friends_fav.append('hawaiian')

print("My fav pizzas are:")
print(pizza)

print("\nMy friend's fav pizzas are:")
print(friends_fav)

#4.12
pizza = ['cheese', 'stuffed', 'veggie']
for x in pizza[:2]:
	print(f'{x.title()} are my favorite pizzas')

for x in pizza[3:]:
	print(f"{x.title()} are my friend's favorite pizzas.")

#4.13
food = (cream, orange, fish, chicken, veggie, okra)
for simple in food:
	print(simple)

food[0] = food[cheese]

print("Modified food:")
food = (pudding, brisket, fish, chicken, veggie, okra)
for simple in food:
	print(simple)

food = ('pudding', 'brisket', 'fish', 'chicken', 'veggie', 'okra')
print("Modified food:")
for simple in food:
	print(simple)

#4.14 Style Guide for Python Code
plants = [
    'alocasia', 'monstera', 'brazil',
    'brandti', 'soh', 'scindapsus',
    ]
for x in plants:
    print(f'{x.title()} are my favorite indoor plants.')
    print(len(f'{x.title()} are my favorite indoor plants.'))

number = (1, )
print(number) 

fav = [
    'target', 'pLants', 'coffee',
    'tea', 'python', 'gym',  
    ]
for x in fav[0:2]:
    print(x)
