#using random library to create a random card selection
import random

suits = ['♣', '♦', '♥', '♠']
values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
#Prints out random card
print(random.choice(values) + random.choice(suits))