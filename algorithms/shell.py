import math
from misc import finished_animation


def shell_gaps(n):
    gaps = []
    curr = n // 2
    while curr > 0:
        gaps.append(curr)
        curr //= 2
    return gaps


def hibbard_gaps(n):
    gaps = []
    i = 1
    while (gap := 2 ** i - 1) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def papernov_stasevich_gaps(n):
    gaps = [1]
    i = 1
    while (gap := 2 ** i + 1) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def knuth_gaps(n):
    gaps = []
    i = 1
    while (gap := (3 ** i - 1) // 2) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def sedgewick_1982_gaps(n):
    gaps = [1]
    i = 1
    while (gap := 4 ** i + 3 * 2 ** (i - 1) + 1) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def sedgewick_1986_gaps(n):
    gaps = [1]
    i = 1
    while (gap := 9 * (2 ** i - 2 ** (i / 2)) + 1 if i % 2 == 0 else 8 * 2 ** i - 6 * 2 ** ((i + 1) / 2) + 1) < n:
        gaps.append(int(gap))
        i += 1
    return gaps[::-1]


def tokuda_gaps(n):
    gaps = []
    i = 1
    while (gap := math.ceil((1 / 5) * (9 * (9 / 4) ** (i - 1) - 4))) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def ciura_gaps(n):
    return [701, 301, 132, 57, 23, 10, 4, 1]


def lee_gaps(n):
    GAMMA = 2.243609061420001
    gaps = []
    i = 1
    while (gap := math.ceil((GAMMA ** i - 1) / (GAMMA - 1))) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def skean_ehrenborg_jaromczyk_gaps(n):
    gaps = [1, 4]
    i = 1
    while (gap := math.floor(4.0816 * 8.5714 ** (i / 2.2449))) < n:
        gaps.append(gap)
        i += 1
    return gaps[::-1]


def shell_sort(arr, sequence="shell"):
    SEQUENCES = {
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

    if sequence not in SEQUENCES:
        raise ValueError(
            f"Invalid partition scheme '{sequence}'. Supported schemes are: {', '.join(SEQUENCES.keys())}.")

    n = len(arr)
    gaps = SEQUENCES[sequence](n)

    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                yield arr, [i, j - gap], []
                j -= gap

            if arr[j] != temp:
                arr[j] = temp
                yield arr, [i, j], []

    yield from finished_animation(arr)
