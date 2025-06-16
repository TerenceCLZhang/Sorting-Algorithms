import math

def shell_gaps(n):
    """
    Generates Shell's gap sequence (1959)
    Worst Time Complexity: O(n^2)
    """
    gaps = []
    curr = n // 2
    while curr > 0:
        gaps.append(curr)
        curr //= 2
    return gaps


def hibbard_gaps(n):
    """
    Generates Hibbard's gap sequence (1961)
    Worst Time Complexity: O(n^(3/2))
    """
    gaps = []
    i = 1
    while (gap := 2 ** i - 1) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]



def papernov_stasevich_gaps(n):
    """
    Generates Papernov & Stasevich's gap sequence (1965)
    Worst Time Complexity: O(n^(3/2))
    """
    gaps = [1]
    i = 1
    while (gap := 2 ** i + 1) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def knuth_gaps(n):
    """
    Generates Knuth's gap sequence (1973)
    Worst Time Complexity: O(n^(3/2))
    """
    gaps = []
    i = 1
    while (gap := (3 ** i - 1) // 2) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def sedgewick_1982_gaps(n):
    """
    Generates Sedgewick's gap sequence (1982)
    Worst Time Complexity: O(n^(4/3))
    """
    gaps = [1]
    i = 1
    while (gap := 4 ** i + 3 * 2 ** (i - 1) + 1) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def sedgewick_1986_gaps(n):
    """
    Generates Sedgewick's gap sequence (1986)
    Worst Time Complexity: O(n^(4/3))
    """
    gaps = [1]
    i = 1
    while (gap := 9 * (2 ** i - 2 ** (i / 2)) + 1 if i % 2 == 0 else 8 * 2 ** i - 6 * 2 ** ((i + 1) / 2) + 1) < n:
        gaps.append(int(gap))
        i += 1
    return gaps[::-1]


def tokuda_gaps(n):
    """
    Generates Tokuda's gap sequence (1992)
    Worst Time Complexity: O(?)
    """
    gaps = []
    i = 1
    while (gap := math.ceil((1 / 5) * (9 * (9 / 4) ** (i - 1) - 4))) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def ciura_gaps(n):
    """
    Returns Ciura's gap sequence (2001)
    Worst Time Complexity: O(?)
    """
    return [701, 301, 132, 57, 23, 10, 4, 1]


def lee_gaps(n):
    """
    Returns Lee's gap sequence (2021)
    Worst Time Complexity: O(?)
    """
    GAMMA = 2.243609061420001
    gaps = []
    i = 1
    while (gap := math.ceil((GAMMA ** i - 1) / (GAMMA - 1))) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def skean_ehrenborg_jaromczyk_gaps(n):
    """
    Returns Skean, Ehrenborg and Jaromczyk's gap sequence (2023)
    Worst Time Complexity: O(?)
    """
    gaps = [1, 4]
    i = 1
    while (gap := math.floor(4.0816 * 8.5714 ** (i / 2.2449))) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


sequences = {
    "shell": shell_gaps,
    "hibbard": hibbard_gaps,
    "papernov": papernov_stasevich_gaps,
    "knuth": knuth_gaps,
    "sedgewick82": sedgewick_1982_gaps,
    "sedgewick86": sedgewick_1986_gaps,
    "tokuda": tokuda_gaps,
    "ciura": ciura_gaps,
    "lee": lee_gaps,
    "skean": skean_ehrenborg_jaromczyk_gaps
}