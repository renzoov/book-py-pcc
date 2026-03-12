import pizza
from pizza import make_pizza as mp
import pizza as p
from pizza import *

pizza.make_pizza(16, 'mushrooms')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n' + '-' * 40 + '\n')

mp(16, 'mushrooms')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n' + '-' * 40 + '\n')

p.make_pizza(16, 'mushrooms')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print('\n' + '-' * 40 + '\n')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')