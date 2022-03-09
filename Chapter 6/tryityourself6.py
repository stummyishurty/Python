#6.1
person = {
    'first_name': 'neo',
    'last_name': 'reyes',
    'age': '2',
    'city': 'sa',
    }

first = person['first_name'].title()
last = person['last_name'].title()
city = person['city'].upper()
print(f"{first} {last} is {person['age']}. He lives in {city}.")

#6.2
numbers = {
    'neo': '25',
    'jon': '16',
    'mel': '5',
    'morgan': '19',
    'mary': '8',
    }

print(f"Neo fav number is {numbers['neo']}")
print(f"Jon fav number is {numbers['jon']}")
print(f"Mel fav number is {numbers['mel']}")
print(f"Morgan fav number is {numbers['morgan']}")
print(f"Mary fav number is {numbers['mary']}")

numbers = {
    'neo': 25,
    'jon': 16,
    'mel': 5,
    'morgan': 19,
    'mary': 8,
    }

if numbers['neo'] == 25:
    favorite_number = 16

else: 
    favorite_number = 10

numbers['neo'] = numbers['neo'] + favorite_number

print(f"Neo's second favorite number is {numbers['neo']}")  

##6.3
glossary = {'list' : 'list are used to store multiple items in a single variable',
            'loop': 'loop iterates over an object until that object is complete',
            'range': 'to generate a series of numbers easily',
            'tuple': 'like a list, but with parentheses, and cannot be modify',
            'if statement': ' evaluates whether a condition is equal to true or false',
            }

item = 'list'
print(f"\n{item.title()} : {glossary[item]}")
item = 'loop'
print(f"\n{item.title()} : {glossary[item]}")
item = 'range'
print(f"\n{item.title()} : {glossary[item]}")
item = 'tuple'
print(f"\n{item.title()} : {glossary[item]}")
item = 'if statement'
print(f"\n{item.title()} : {glossary[item]}")

#6.3 = 6.4 clean version

for keys, values in glossary.items():
    print(f"\nGlossary: {keys.title()}")
    print(f"Meaning: {values}")

glossary = {'list' : 'list are used to store multiple items in a single variable',
            'loop': 'loop iterates over an object until that object is complete',
            'range': 'to generate a series of numbers easily',
            'tuple': 'like a list, but with parentheses, and cannot be modify',
            'if statement': ' evaluates whether a condition is equal to true or false',
            'dictionary': 'is a collection of key-value pairs',
            'floats': 'represents floating point numbers',
            'indent': 'the spaces at the beginning of a code line',
            'string': 'series of characters',
            }

for keys, values in glossary.items():
    print(f"\nGlossary: {keys.title()}")
    print(f"Meaning: {values}")

#6.5
rivers = {'volga': 'russia',
         'magdalena': 'columbia',
         'yangtze': 'china'
         }

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")

print(f"\nThese are the rivers:")
for river in rivers.keys():
    print(f"-{river.title()}")

print(f"\nThese are the countries:")
for river in rivers.values():
    print(f"-{river.title()}")

#6.6
favorite_languages = {'neo': 'python',
                      'jon': 'c',
                      'mel': 'ruby',
                      'morgan': 'python',
                     }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

peeps = ['neo', 'jon', 'mel', 'candice', 'mitchell' ,'cascade']
for peeps in peeps:
    if peeps in favorite_languages.keys():
        print(f"Thank you for taking the poll, {peeps.title()}.")

    else:
        print(f"{peeps.title()}, please take our poll.")


#6.7
people = []

person = {
        'first': 'neo',
        'last': 'reyes',
        'age': 20,
        'city': 'tampa',
        }
people.append(person)

person= {
        'first': 'mary',
        'last': 'gore',
        'age': 35,
        'city': 'dallas',
        }
people.append(person)

person = {
        'first': 'noob',
        'last': 'noob',
        'age': 19,
        'city': 'space',
        }
people.append(person)

for person in people:
    name = f"{person['first'].title()} {person['last'].title()}"
    age = person['age']
    city = person['city'].title()
    
    print(f"{name}, is {age} years old from {city}.")

#6.8
pets = []

pet = {
    'animal': 'dog',
    'name': 'tom',
    'owner': 'tim',
    'color':'white with black speckles',
    'snack': 'peanut butter',
}

pets.append(pet)

pet = {
    'animal': 'ferret',
    'name': 'fluffy',
    'owner': 'melissa',
    'color': 'white',
    'snacks': 'egg',

}

pets.append(pet)

pet = {
    'animal': 'bird',
    'name': 'birdperson',
    'owner': 'cat',
    'color': 'blue',
    'snacks': 'grains',
}

pets.append(pet)

for pet in pets:
    print(f"\nEverything I know about {pet['owner'].title()}'s pet:")
    for key, value in pet.items():
        print(f"{key}:{value}")

#6.9
favorite_places = {
    'rick': ['blips and chitz', 'planet squanch'],
    'neo': ['yogurtland', 'milkworld'],
    'mary': ['home', 'crawfishking'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(place.title())

#6.10
favorite_numbers = {
    'neo': 25,
    'jon': 16,
    'mel': 5,
    'morgan': 19,
    'mary': 8,
    }

for names, numbers in favorite_numbers.items():
    print(f"\n{names.title()}'s favorite number is {numbers}.")

#6.11
cities = {
    'Bangkok':{
    'country': 'Thailand',
    'population': '66558936',
    'food': 'tomyam',
    },

    'Singapore':{
    'country': 'Singapore',
    'population': '5886139',
    'food': 'laksa',
    },

    'London':{
    'country': 'UK',
    'population': '68497907',
    'food': 'fish and chips',
    }
}

for cities, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    food = city_info['food'].title()

    print(f"\n{cities} is in {country}.")
    print(f"There are {population} people in {cities}.")
    print(f"One of it's famous food is {food}.")

print("\nP.S. I create this list when I'm hungry:)")

#6.12
favorite_language = {'jen':['python', 'ruby'],
                     'phil':['c'],
                     'jacob':['go', 'ruby'],
                     'jack':['python', 'haskell'],
                     'gale': ['C++'],
                     'neo': ['python', 'html'],
                     'jon': ['javascript'],
                     }

favorite_language['melissa'] = ['pascal', 'html', 'Java']

if favorite_language['jen'] == ['python', 'ruby']:
    print("ok Jen")

for x, y in favorite_language.items():
    if len(y) == 1:
        print(f"\n{x.title()}'s favorite language is:")
        print(f"\t{language.title()}")

    else:
        print(f"\n{x.title()}'s favorite languages are:")
        for language in y:
            print(f"\t{language.title()}")



