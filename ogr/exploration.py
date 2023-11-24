"""Start exploring the GolombRuler problem.

A Golomb ruler is a sequence of non-negative integers such that every difference of two integers is distinct.

"""

from __future__ import annotations

from .exceptions import *

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

def compute_distances(sequence: list[int]) -> set[int]:
    """Compute the pairwise distances of `sequence` and return the results in a set."""
    distances = set()

    for (lhs_index, lhs) in enumerate(sequence):
        for rhs in sequence[(lhs_index + 1):]:
            distances.add(dist(lhs, rhs))

    return distances

def generate_golomb_ruler_naive(order: int) -> list[int]:
    """Naively generate a new golomb ruler with `order` marks."""
    if order < 1: ValueError("order must be greater than 0")
    if order == 1: return [0]

    prev = generate_golomb_ruler_naive(order - 1)
    next = 2 ** (order - 1) - 1
    prev.append(next)

    return prev

def generate_golomb_ruler_improved(order: int) -> list[int]:
    """Generate a golomb ruler with order `order` using an improved algorithm.

    This algorithm runs in O(n^4)
    """
    if order < 1: ValueError("order must be greater than 0")
    if order == 1: return [0]
    if order == 2: return [0, 1]
    if order == 3: return [0, 1, 3]

    prev = generate_golomb_ruler_improved(order - 1)


    # Compute the differences
    distances = compute_distances(prev) # O(n^2)
    candidate_upper_bound = 2 * prev[-1] + 1 # Guarantees that we will accept at least one candidate

    def should_accept_candidate(candidate: int) -> bool:
        """Utility function used to check if a candidate should be accepted.

        Allows us to skip to the next loop on a false input (otherwise we only break from an inner loop)

        Runs in O(n)
        """
        for i in range(order - 1):
            if dist(candidate, prev[i]) in distances:
                return False

        return True

    for c in range(prev[-1], candidate_upper_bound + 1):
        # O(n) check to make sure that c != x_i for all i in 1..n
        # we could turn previous into a set to speed up this but that wouldn't
        # change asymptotic complexity
        if c in prev:
            continue

        if should_accept_candidate(c):
            prev.append(c)
            return sorted(prev)

    raise Exception("Implementation Error!!!")


class GolombRuler:
    """A list of non-negative integers."""

    def __init__(self, sequence: list[int], assert_golomb_property = True):
        """Construct a new GolombRuler.

        Raises `NotGolombRuler` if the input sequence is malformed.
        """
        if assert_golomb_property:
            if not is_golomb_ruler(sequence):
                raise NotGolombRuler(f"Input sequence: {sequence} does not satisfy the GolombRuler conditions.")

        self.sequence = sequence

    def order(self) -> int:
        """Return the order (number of elements in the sequence) of this GolombRuler."""
        return len(self.sequence)



    def d_plus_e(self) -> str:
        """Return a string representation of the """


    # ---------------------------------------------------------------------------- #
    #               Functions dealing with upper triangular matrices               #
    # ---------------------------------------------------------------------------- #
    def triu_size(self) -> int:
        """Compute the amount of space needed for a 1-dimensional matrix that encodes the distances between all pairs of marks."""
        n = self.order()
        return n * (n - 1) // 2

    def triu_elements_before_row(self, row_index: int) -> int:
        """Compute the number of elements before our 0-based indexing row.

        Consider the following upper triangular matrix containing the distances between marks in a 3-order golomb ruler:
        ```
        i: 0    |   -     d_12    d_13    |
        i: 1    |   -      -      d_23    |
        i: 2    |   -      -        -     |
        ```

        `triu_elements_before_row` computes the number of elements before a certain row. For example,
        we expect `triu_elements_before_row(1)` -> 2 and `triu_elements_before_row(2)` -> 3

        This function is used to compute the appropriate index for an array encoding the distances between marks.
        """
        n = self.order()
        i = row_index + 1
        return -half(i * i) + half(i * (2 * n + 1)) - n

    def triu_linear_index(self, row_index: int, col_index: int) -> int:
        """Compute the linear index for a upper triangular coordinate."""
        return self.triu_elements_before_row(row_index) + col_index

    def triu_distances(self) -> list[int]:
        """Compute the distances between every mark of this ruler, storing the results in a 1-d list."""
        distances: list[int] = [0 for _ in range(self.triu_size())]
        idx = 0

        for (lhs_idx, lhs) in enumerate(self.sequence):
            for rhs in self.sequence[(lhs_idx + 1):]:
                distances[idx] = dist(lhs, rhs)
                idx += 1

        return distances

    @staticmethod
    def from_distances(distances: list[int], order: int) -> GolombRuler:
        """Construct a new GolombRuler given a list of distances.

        Used to read the output of the linear programming formulation.
        """
        # Assume that the first mark is 0.
        marks = [0]
        marks.extend(distances[:(order - 1)])
        return GolombRuler(marks)

def half(a: int) -> int:
    return a // 2

def div(a: int, b: int) -> int:
    return a // b


if __name__ == '__main__':
    ruler = GolombRuler([0, 1, 3])

    print(ruler.triu_distances())

    ruler = GolombRuler(generate_golomb_ruler_improved(5))
    print(ruler.triu_distances())

    ruler_copy = GolombRuler.from_distances(ruler.triu_distances(), ruler.order())
    print(ruler_copy.sequence)
