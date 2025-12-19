from collections.abc import Iterable
from itertools import takewhile
from operator import eq
import random

# -----------------------------------------------------------------------------

def shuffle(seed:int=None, n:int=30) -> list[int]:
    r = random.Random(seed)
    draws = list(range(1, n+1))
    for i in range(n):
        random_index = r.randrange(n - i)
        t = draws[i + random_index]
        draws[i + random_index] = draws[i]
        draws[i] = t
    return draws

assert len(set(shuffle(None, 100))) == 100
assert shuffle(None, 100) != list(range(1,101))

# -----------------------------------------------------------------------------

def to_count(val) -> int:
    return len(val) if isinstance(val, Iterable) else val

assert to_count(1234) == 1234
assert to_count([1, 2, 3, 4]) == 4
assert to_count({1, 2, 3, 4}) == 4

# -----------------------------------------------------------------------------

def next_draw(sequence:list[int], discard:Iterable=set()) -> int:
    counts = [to_count(d) for d in discard]
    return [s for s in sequence if s not in counts][0]

assert next_draw([28, 14, 27]) == 28
assert next_draw([28, 14, 27], discard=[28]) == 14
assert next_draw([28, 14, 27], discard=[28, 14]) == 27
assert next_draw([28, 14, 27], discard=[14, 27]) == 28 # you are allowed to skip

# -----------------------------------------------------------------------------

def longest_common_prefix[T](a:Iterable[T], b:Iterable[T]) -> Iterable[T]:
    return [elem for elem, _ in takewhile(lambda ab: ab[0]==ab[1], zip(a, b))]

assert longest_common_prefix([1,2,3,4], [1,2,3,5]) == [1,2,3]

# -----------------------------------------------------------------------------

def instructions(sequence:Iterable[int], discarded:dict) -> str:
    counts = [to_count(d) for d in discarded.values()]
    prefix = longest_common_prefix(sequence, counts)
    p = len(prefix)
    if p < len(discarded):
        return f"You still need to discard {sequence[p] - counts[p]} item(s)"
    else:
        return f"Your next draw is {next_draw(sequence=sequence, discard=counts)}"

assert instructions([28, 14, 27], discarded={}) == f"Your next draw is 28"
assert instructions([28, 14, 27], discarded={1:28, 2:14}) == f"Your next draw is 27"
assert instructions([28, 14, 27], discarded={1:28, 2:14, 3:24}) == f"You still need to discard 3 item(s)"

# -----------------------------------------------------------------------------

def stats(sequence:Iterable[int], discarded:dict) -> str:
    counts = [to_count(d) for d in discarded.values()]
    prefix = longest_common_prefix(sequence, counts)
    complete = f"You have drawn and discarded {','.join(str(p) for p in prefix)}; for a total of {sum(prefix)}."
    incomplete = f"In addition, you have discarded {to_count(discarded[len(prefix)])} out of {sequence[len(prefix)]}." if len(prefix) < len(discarded) else ""
    return complete + incomplete

assert stats(sequence=[28, 14, 27], discarded={1:28, 2:14, 3:27}) == "You have drawn and discarded 28,14,27; for a total of 69."

# -----------------------------------------------------------------------------

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
print(stats(shuffle(seed=19810902), discarded=real_discarded_items))