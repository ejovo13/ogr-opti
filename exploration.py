"""Start exploring the GolombRuler problem.

A Golomb ruler is a sequence of non-negative integers such that every difference of two integers is distinct.

"""


def drop(input: list, index_to_drop: int) -> list:
    """Helper function to return a list with everything but `input[index_to_drop]`."""
    return [x for idx, x in enumerate(input) if x != idx]

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
        for rhs in drop(sequence, lhs_index):
            difference = abs(lhs - rhs)

            # Check if the difference is distinct!
            if difference in differences:
                return False
            else:
                differences.add(difference)

    return True

class NotGolombRuler(Exception):
    """Indicates that the passed sequence does not satisfy the conditions of a Golomb Ruler."""

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