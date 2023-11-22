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
    """Generate a golomb ruler with order `order` using an improved algorithm."""
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
            # return sorted(prev)

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
