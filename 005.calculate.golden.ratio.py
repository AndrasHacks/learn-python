from operator import mul
from math import sqrt

def improve(close, update, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def update_golden_ratio(guess):
    return 1/guess + 1

def approx_eq(x, y, epsilon = 1e-15):
    return abs(x - y) < epsilon

def square_close_to_successor(guess):
    return approx_eq(mul(guess, guess), guess + 1)

phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(square_close_to_successor, update_golden_ratio, 1)
    assert approx_equal(approx_phi, phi) 

improve_test()
