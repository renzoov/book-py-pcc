def build_person(first_name, last_name):
    person = {'first_name': first_name, 'last_name': last_name}
    return person

musician = build_person('John', 'Doe')
print(musician)

print('\n' + '-' * 40 + '\n')
def build_person(first_name, last_name, age=None):
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('John', 'Doe', age=27)
print(musician)