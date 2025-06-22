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

## Controls

| **Control Key** | **Action**            |
| --------------- | --------------------- |
| `+`             | Increase speed        |
| `-`             | Decrease speed        |
| `Space`         | Pause/Resume          |
| `r`             | Restart current array |
| `n`             | Generate new array    |
| `Escape`        | Exit visualization    |
