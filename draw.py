import random
import collections.abc

def shuffle(seed=None, n=30):
    r = random.Random(seed)
    draws = list(range(1, n+1))
    for i in range(n):
        random_index = r.randrange(n - i)
        t = draws[i + random_index]
        draws[i + random_index] = draws[i]
        draws[i] = t
    return draws

def to_count(val):
    return len(val) if isinstance(val, collections.abc.Iterable) else val

def next_draw(seed, n=30, discard=set()):
    counts = [to_count(d) for d in discard]
    return [s for s in shuffle(seed, n) if s not in counts][0]

assert len(set(shuffle(None, 100))) == 100
first_three_for_seed_0 = [28, 14, 27]
assert next_draw(seed=0, n=31) == first_three_for_seed_0[0]
assert next_draw(seed=0, n=31, discard=first_three_for_seed_0[0:1]) == first_three_for_seed_0[1]
assert next_draw(seed=0, n=31, discard=first_three_for_seed_0[0:2]) == first_three_for_seed_0[2]
assert next_draw(seed=0, n=31, discard=first_three_for_seed_0[1:3]) == first_three_for_seed_0[0] # you are allowed to skip

def instructions(seed, discarded):
    if not discarded:
        return f"Your next draw is {next_draw(seed=seed)}"
    most_recent_day = max(discarded.keys())
    all_but_most_recent_day = {
        d: to_count(n)
        for d, n in discarded.items()
        if d != most_recent_day}
    next_draw_if_you_dont_count_most_recent_day = next_draw(
        seed=seed,
        discard=set(all_but_most_recent_day.values()))
    if next_draw_if_you_dont_count_most_recent_day != discarded[most_recent_day]:
        return f"You still need to discard {next_draw_if_you_dont_count_most_recent_day - to_count(discarded[most_recent_day])} item(s)"
    else:
        return f"Your next draw is {next_draw(seed=seed, discard=set(to_count(d) for d in discarded.values()))}"

assert instructions(seed=0, discarded={}) == f"Your next draw is {first_three_for_seed_0[0]}"
first_three_for_seed_0_missing_one = [first_three_for_seed_0[0], first_three_for_seed_0[1], first_three_for_seed_0[2] - 1]
assert instructions(seed=0, discarded=dict(enumerate(first_three_for_seed_0_missing_one))) == f"You still need to discard 1 item(s)"

real_discarded_items = {
        20251213: 10,
        20251214: 18,
        20251215: 9,
        20251216: 11,
        20251217: 27,
        20251218: {
            "bowl of very old mixed nuts",
            "stiffener for long-discarded front door screen",
            "an opened box of mushrooms that have turned",
            "an unopened box of mushrooms that have turned",
            "tub of moldy noosa",
            "my denim shorts",
            "unused app 1",
            "unused app 2",
            "unused app 3",
            "unused app 4",
            "unused app 5",
            "unused app 6",
            "unused app 7",
            "unused app 8",
            "unused app 9",
            "unused app 10",
            "unused app 11",
        },
    }
print(instructions(seed=19810902, discarded=real_discarded_items))