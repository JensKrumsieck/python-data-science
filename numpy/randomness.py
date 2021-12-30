import numpy as np

from numpy.random import choice, randint

choices = [
    "A",
    "B",
    "C"
]

p = [
    .7,
    .1,
    .2
]

print(choice(choices, size=(100, 200), p=p))  # A 70%, B 10%, C 20%

print(randint(1, 42, size=(2, 2)))  # random 2x2 matrix
