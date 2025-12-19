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

def next_draw(sequence, discard=set()):
    counts = [to_count(d) for d in discard]
    return [s for s in sequence if s not in counts][0]

assert len(set(shuffle(None, 100))) == 100
assert next_draw([28, 14, 27]) == 28
assert next_draw([28, 14, 27], discard=[28]) == 14
assert next_draw([28, 14, 27], discard=[28, 14]) == 27
assert next_draw([28, 14, 27], discard=[14, 27]) == 28 # you are allowed to skip

def instructions(sequence, discarded):
    if not discarded:
        return f"Your next draw is {next_draw(sequence)}"
    most_recent_day = max(discarded.keys())
    all_but_most_recent_day = {
        d: to_count(n)
        for d, n in discarded.items()
        if d != most_recent_day}
    next_draw_if_you_dont_count_most_recent_day = next_draw(
        sequence=sequence,
        discard=set(all_but_most_recent_day.values()))
    if next_draw_if_you_dont_count_most_recent_day != to_count(discarded[most_recent_day]):
        return f"You still need to discard {next_draw_if_you_dont_count_most_recent_day - to_count(discarded[most_recent_day])} item(s)"
    else:
        return f"Your next draw is {next_draw(sequence=sequence, discard=set(to_count(d) for d in discarded.values()))}"

assert instructions([28, 14, 27], discarded={}) == f"Your next draw is 28"
assert instructions([28, 14, 27], discarded={1:28, 2:14}) == f"Your next draw is 27"
assert instructions([28, 14, 27], discarded={1:28, 2:14, 3:24}) == f"You still need to discard 3 item(s)"

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
print(instructions(shuffle(seed=19810902), discarded=real_discarded_items))