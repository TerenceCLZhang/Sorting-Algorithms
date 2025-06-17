# Sorting Algorithm Visualizer

Visualises the following algorithms:

- Bogo Sort
- Bozo Sort
- Exchange Sort
- Bubble Sort
- Optimized Bubble Sort
- Odd Even Sort
- Comb Sort
- Cocktail Sort
- Gnome Sort
- Insertion Sort
- Binary Insertion Sort
- Shell Sort
- Selection Sort
- Heap Sort

## Visualizing

To visualise an algorithm, call the `visualize` function which will launch a Pygame-based graphical animation.

### Parameters:

| Parameter   | Type  | Default      | Description                                                                                                                         |
| ----------- | ----- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `algorithm` | `str` | _(required)_ | Name of the sorting algorithm to visualise. Must match a key in the `ALGORITHMS` dictionary (e.g., `"Bubble Sort"`, `"Heap Sort"`). |
| `n`         | `int` | `50`         | Number of elements in the array to sort. A unique random permutation of integers from 1 to `n` is generated.                        |
| `speed`     | `int` | `20`         | Animation speed in steps per second. A higher number means faster visualisation.                                                    |
| `width`     | `int` | `800`        | Width of the Pygame window in pixels.                                                                                               |
| `height`    | `int` | `600`        | Height of the Pygame window in pixels.                                                                                              |

**Example:**

```
visualize("Insertion Sort", n=100, speed=45, width=1440, height=900)
```

#### Shell Sort: Gap Sequences

When using Shell Sort, you can optionally specify a custom gap sequence using the sequence keyword. If no sequence is provided, the default is Shell’s original gap sequence (1959).

Supported Gap Sequences:

| Sequence Name                   | Keyword       | Year |
| ------------------------------- | ------------- | ---- |
| Shell                           | `shell`       | 1959 |
| Hibbard                         | `hibbard`     | 1961 |
| Papernov and Stasevich          | `papernov`    | 1965 |
| Knuth                           | `knuth`      | 1973 |
| Sedgewick (First sequence)      | `sedgewick82` | 1982 |
| Sedgewick (Second sequence)     | `sedgewick86` | 1986 |
| Tokuda                          | `tokuda`      | 1992 |
| Ciura                           | `ciura`       | 2001 |
| Lee                             | `lee`         | 2021 |
| Skean, Ehrenborg, and Jaromczyk | `skean`       | 2023 |

**Example:**

```
visualize("Shell Sort", sequence="ciura")
```

## Controls

| **Control Key** | **Action**            |
| --------------- | --------------------- |
| `+`             | Increase speed        |
| `-`             | Decrease speed        |
| `Space`         | Pause/Resume          |
| `r`             | Restart current array |
| `n`             | Generate new array    |
