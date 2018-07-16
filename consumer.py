import random

from tasks import add, mul


def rand_int():
    return random.randint(1, 65535)


for i in range(1, 10000):
    add.delay(rand_int(), rand_int())
    mul.delay(rand_int(), rand_int())
