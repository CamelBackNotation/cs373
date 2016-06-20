#!/usr/bin/env python3

#pylint: disable = bad-builtin, redefined-outer-name

# ----------
# Lambdas.py
# ----------

from functools import reduce

print("Lambdas.py")

def my_function (x, y) :
    return x + y

f1 = my_function

assert my_function(2, 3) == 5
assert           f1(2, 3) == 5

assert reduce(my_function, [2, 3, 4], 0) == 9
assert reduce(f1,          [2, 3, 4], 0) == 9


f2 = lambda x, y : x + y

assert (lambda x, y : x + y)(2, 3) == 5
assert f2(2, 3)                    == 5

assert reduce(lambda x, y : x + y, [2, 3, 4], 0) == 9
assert reduce(f2,                  [2, 3, 4], 0) == 9



def my_lambda () :
    return lambda x, y : x + y

f3 = my_lambda()

assert my_lambda()(2, 3) == 5
assert          f3(2, 3) == 5

assert reduce(my_lambda(), [2, 3, 4], 0) == 9
assert reduce(f3,          [2, 3, 4], 0) == 9



x = 2

f4 = lambda y : x + y

assert (lambda y : x + y)(3) == 5
assert                 f4(3) == 5

assert list(map(lambda y : x + y, [2, 3, 4])) == [4, 5, 6]
assert list(map(f4,               [2, 3, 4])) == [4, 5, 6]



def my_closure (x) :
    return lambda y : x + y

f5 = my_closure(2)

assert my_closure(2)(3) == 5
assert            f5(3) == 5

assert list(map(my_closure(2), [2, 3, 4])) == [4, 5, 6]
assert list(map(f5,            [2, 3, 4])) == [4, 5, 6]

print("Done.")
