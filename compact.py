def compact(sequence):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    for item, previous in zip(sequence, [object(), *sequence]):
        if item != previous:
            deduped.append(item)
    return deduped


print(compact([1, 1, 2, 2, 3, 2]))
