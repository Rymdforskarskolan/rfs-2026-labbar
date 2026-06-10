arr = [
    [12.5, 8.7, 12.4, 4.5, 12.9],
    [9.1, 7.2, 5.2, 3.5, 15.3],
    [10.2, 5.7, 4.0, 17.3, 9.4],
    [11.3, 2.1, 1.3, 8.9, 10.6],
    [13.8, 3.4, 9.2, 22.5, 13.3],
]

anoms = []

for i, row in enumerate(arr):
    for j, cell in enumerate(row):
        if any(
            [
                j != 0 and row[j - 1] * 1.5 < cell,
                j < len(row) - 1 and row[j + 1] * 1.5 < cell,
                i != 0 and arr[i - 1][j] * 1.5 < cell,
                i < len(arr) - 1 and arr[i + 1][j] * 1.5 < cell,
            ]
        ):
            anoms.append(((i, j), cell))

for i, anom in enumerate(anoms):
    print(f"{anom[0]}: {anom[1]}, ", end="")
