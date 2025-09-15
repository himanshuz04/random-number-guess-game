import numpy as np
from numpy import random

x=random.randint(1,100)
while x> 0:
    user_input = int(input("Enter your guess :"))
    if user_input < x:
        print("Your guess is low")
    elif user_input > x:
        print("Your guess is high")
    elif user_input== x:
        print("You guessed it right")
        break
