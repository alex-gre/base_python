country = {'code': 'ru', 'name': 'Russian', 'population': 144}
#country = dict(code='ru', name='Russian')
#print(country['name'])

#print(country.items())
#print(country.keys())
#print(country.values())

for key, value in country.items():
    print(key, ' - ', value)


person = {
    'user1': {
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'age': 45,
    'address': ('г. Москва', 'ул. Ленина', '45'),
    'grades': {'math': 5, 'physics': 3},

    },
    'user2': {}
}

print(person['user1'])
