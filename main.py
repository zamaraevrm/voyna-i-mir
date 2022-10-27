import random


def random_char(char: str):
    seq = 1
    rnd = random.randint(0, sum(seq.values()))
    total = 0

    for k, v in seq.items():
        total += v

        if rnd <= total:

            return k





