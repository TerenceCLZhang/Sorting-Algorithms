# Sorting Algorithm Visualizer

Visualises the following algorithms:

| Sorting Algorithm    | Call Name   | Best Case  | Average Case | Worst Case |
| -------------------- | ----------- | ---------- | ------------ | ---------- |
| Bozo Sort            | `bozo`      | Ω(n)       | Θ((n·n)!)    | O(∞)       |
| Bogo Sort            | `bogo`      | Ω(n)       | Θ((n·n)!)    | O(∞)       |
| Stooge Sort          | `stooge`    | Ω(n^2.71)  | Θ(n^2.71)    | O(n^2.71)  |
| Exchange Sort        | `exchange`  | Ω(n²)      | Θ(n²)        | O(n²)      |
| Bubble Sort          | `bubble`    | Ω(n)       | Θ(n²)        | O(n²)      |
| Odd Even Sort        | `oddeven`   | Ω(n)       | Θ(n²)        | O(n²)      |
| Pancake Sort         | `pancake`   | Ω(n)       | Θ(n²)        | O(n²)      |
| Comb Sort            | `comb`      | Ω(n log n) | Θ(n²/2^p)    | O(n²)      |
| Cocktail Shaker Sort | `cocktail`  | Ω(n)       | Θ(n²)        | O(n²)      |
| Gnome Sort           | `gnome`     | Ω(n)       | Θ(n²)        | O(n²)      |
| Insertion Sort       | `insertion` | Ω(n)       | Θ(n²)        | O(n²)      |
| Selection Sort       | `selection` | Ω(n²)      | Θ(n²)        | O(n²)      |
| Shell Sort           | `shell`     | Ω(n log n) | Θ(n(log n)²) | O(n²)      |
| Quick Sort           | `quick`     | Ω(n log n) | Θ(n log n)   | O(n²)      |
| Radix Sort           | `radix`     | Ω(nk)      | Θ(nk)        | O(nk)      |
| Heap Sort            | `heap`      | Ω(n log n) | Θ(n log n)   | O(n log n) |

## Visualizing

To visualise an algorithm, call the `visualize` function which will launch a Pygame-based graphical animation.

### Parameters:

| Parameter   | Type  | Default      | Description                                                                                                              |
| ----------- | ----- | ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `algorithm` | `str` | _(required)_ | Name of the sorting algorithm to visualise. Must match a one of the "Call Names" in the above table.                     |
| `n`         | `int` | `100`        | Number of elements in the array to sort. A unique random permutation of integers from 1 to `n` (inclusive) is generated. |
| `speed`     | `int` | `50`         | Animation speed in steps per second. A higher number means faster visualisation.                                         |
| `width`     | `int` | `800`        | Width of the Pygame window in pixels.                                                                                    |
| `height`    | `int` | `600`        | Height of the Pygame window in pixels.                                                                                   |

**Example:**

```py
visualize("insertion", n=100, speed=45, width=1440, height=900)
```

#### Shell Sort: Gap Sequences

When using Shell Sort, you can optionally specify a custom gap sequence using the `sequence` keyword. If no sequence is provided, the default is Shell’s original gap sequence.

Supported Gap Sequences:

| Sequence Name                   | Keyword       |
| ------------------------------- | ------------- |
| Shell                           | `shell`       |
| Hibbard                         | `hibbard`     |
| Papernov and Stasevich          | `papernov`    |
| Knuth                           | `knuth`       |
| Sedgewick (First sequence)      | `sedgewick82` |
| Sedgewick (Second sequence)     | `sedgewick86` |
| Tokuda                          | `tokuda`      |
| Ciura                           | `ciura`       |
| Lee                             | `lee`         |
| Skean, Ehrenborg, and Jaromczyk | `skean`       |

**Example:**

```py
visualize("shell", sequence="ciura")
```

#### Quick Sort: Partition Schemes

When using Quick Sort, you can optionally specify a custom partitioning scheme scheme using the `scheme` keyword. If no sequence is provided, the default is the Hoare partitioning sequence.

Supported Partition Schemes:

| Partition Scheme    | Keyword  |
| ------------------- | -------- |
| Hoare               | `hoare`  |
| Lomuto              | `lomuto` |
| Dutch National Flag | `dutch`  |

**Example:**

```py
visualize("quick", sequence="lomuto")
```

## Controls

| **Control Key** | **Action**            |
| --------------- | --------------------- |
| `+`             | Increase speed        |
| `-`             | Decrease speed        |
| `Space`         | Pause/Resume          |
| `r`             | Restart current array |
| `n`             | Generate new array    |
| `Escape`        | Exit visualization    |
