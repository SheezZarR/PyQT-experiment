"""File contains all the basic combinatorial formulas."""
import math


def permutations(n: int) -> int:
    """Calculates permutations."""
    return math.factorial(n)


def permutations_duplicates(n: int, ks: list) -> int:
    """Calculates permutations with duplicates."""
    product = math.factorial(n)

    for i in range(len(ks)):
        product /= math.factorial(ks[i])

    return product


def partial_permutation(n: int, k: int) -> int:
    """Calculates partial permutation."""
    product = 1

    for i in range(k, n):
        product *= i

    return product


def partial_permutation_dubplicates(n: int, k: int) -> int:
    """Calculates partial permutation with duplicates."""
    return n**k


def combinations(n: int, k: int) -> int:
    """Calculates combinations."""
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))


def combinations_duplicates(n: int, k: int) -> int:
    """Calculates combinations with duplicates."""
    return math.factorial(n+k-1) // (math.factorial(k) * math.factorial(n-1))
