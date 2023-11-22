"""Start exploring the GolombRuler problem.

A Golomb ruler is a sequence of non-negative integers such that every difference of two integers is distinct.

"""

def dist(a: int, b: int) -> int:
    return abs(a - b)

def is_golomb_ruler(sequence: list[int]) -> bool:
    """Verify if a sequence of integers is a golomb ruler.

    In order for a sequence to be a golomb ruler, the differences between all items must be distinct
    """
    # first assert that all the elements are non-negative
    for el in sequence:
        if el < 0:
            return False

    differences = set()

    for (lhs_index, lhs) in enumerate(sequence):
        for rhs in sequence[(lhs_index + 1):]:

            difference = dist(lhs, rhs)
            # Check if the difference is distinct!
            if difference in differences:
                return False
            else:
                differences.add(difference)

    return True

class NotGolombRuler(Exception):
    """Indicates that the passed sequence does not satisfy the conditions of a Golomb Ruler."""


def generate_golomb_ruler_naive(order: int) -> list[int]:
    """Naively generate a new golomb ruler with `order` marks."""
    if order < 1: ValueError("order must be greater than 0")
    if order == 0: return [0]

    prev = generate_golomb_ruler_naive(order - 1)
    next = 2 ** order - 1
    prev.append(next)

    return prev

class GolombRuler:
    """A list of non-negative integers."""

    def __init__(self, sequence: list[int]):
        """Construct a new GolombRuler.

        Raises `NotGolombRuler` if the input sequence is malformed.
        """

        if not is_golomb_ruler(sequence):
            raise NotGolombRuler(f"Input sequence: {sequence} does not satisfy the GolombRuler conditions.")

        self.sequence = sequence

    def order(self) -> int:
        """Return the order (number of elements in the sequence) of this GolombRuler."""
        return len(self.sequence)



    def d_plus_e(self) -> str:
        """Return a string representation of the """
