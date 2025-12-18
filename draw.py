import random

def shuffle(seed=None, n=30):
    r = random.Random(seed)
    draws = list(range(1, n+1))
    for i in range(n):
        random_index = r.randrange(n - i)
        t = draws[i + random_index]
        draws[i + random_index] = draws[i]
        draws[i] = t
    return draws

def next_draw(seed, n=30, discard=set()):
    return [s for s in shuffle(seed, n) if s not in discard][0]

assert len(set(shuffle(None, 100))) == 100
assert next_draw(seed=0, n=31) == 28
assert next_draw(seed=0, n=31, discard={28}) == 14
assert next_draw(seed=0, n=31, discard={28, 14}) == 27
assert next_draw(seed=0, n=31, discard={14}) == 28 # you are allowed to skip

print(f"Your next draw is {next_draw(seed=19810902, discard=set({
        20251213: 10,
        20251214: 18,
        20251215: 9,
        20251216: 11,
        20251217: 27,
    }.values()))}")