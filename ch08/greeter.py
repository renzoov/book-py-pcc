def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('pepe')

print('\n' + '-' * 40 + '\n')

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        return f'{first_name} {middle_name} {last_name}'
    else:
        return f'{first_name} {last_name}'

musician = get_formatted_name('john', 'john')
print(musician)

musician = get_formatted_name('john', 'hamster', 'hammy')
print(musician)