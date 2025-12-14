import random

def shuffle(seed=None, n=31):
    r = random.Random(seed)
    draws = list(range(1, n+1))
    for i in range(n):
        random_index = r.randrange(n - i)
        t = draws[i + random_index]
        draws[i + random_index] = draws[i]
        draws[i] = t
    return draws

def next_draw(seed, n=31, discard=set()):
    draws = shuffle(seed, n)
    discarded = len(discard)
    if discard != set(draws[0:discarded]):
        return Exception(f'All discarded values must be from the beginning of the draw.')
    return draws[discarded]
    

assert len(set(shuffle(None, 100))) == 100
assert next_draw(0, 31) == 28
assert next_draw(0, 31, {28}) == 14
assert next_draw(0, 31, {28, 14}) == 27

print(f"Your next draw is {next_draw(seed=19810902, discard={10})}")