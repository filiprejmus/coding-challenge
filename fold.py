from typing import Callable, Sequence, TypeVar

A = TypeVar('A')
B = TypeVar('B')


def fold(sequence: Sequence[A], startingValue: B, func: Callable[[A, B], B]) -> B:
    """
    Apply Fold on a sequence.

    Keyword arguments:
    sequence -- sequence of generic type A
    startingValue -- starting value of type B
    func -- function that performs the fold
    """
    
    
    for val in sequence:
        startingValue = func(startingValue, val)
    return startingValue