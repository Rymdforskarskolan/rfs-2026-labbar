def detect_anomalies(grid):
    # Lista för att hålla koll på befintliga anomalier
    anoms = []

    for i, row in enumerate(arr):
        for j, cell in enumerate(row):
            # any() är True om minst ett uttryck i dess argument är True
            if any(
                [
                    # Om koordinaten är giltig och minst 1.5 ggr större än cell till v.
                    j != 0 and row[j - 1] * 1.5 < cell,
                    # Om koordinaten är giltig och minst 1.5 ggr större än cell till h.
                    j < len(row) - 1 and row[j + 1] * 1.5 < cell,
                    # Om koordinaten är giltig och minst 1.5 ggr större än cell nedan.
                    i != 0 and arr[i - 1][j] * 1.5 < cell,
                    # Om koordinaten är giltig och minst 1.5 ggr större än cell ovan.
                    i < len(arr) - 1 and arr[i + 1][j] * 1.5 < cell,
                ]
            ):
                anoms.append(((i, j), cell))

    return anoms


arr = [
    [12.5, 8.7, 12.4, 4.5, 12.9],
    [9.1, 7.2, 5.2, 3.5, 15.3],
    [10.2, 5.7, 4.0, 17.3, 9.4],
    [11.3, 2.1, 1.3, 8.9, 10.6],
    [13.8, 3.4, 9.2, 22.5, 13.3],
]

anoms = detect_anomalies(arr)

for i, anom in enumerate(anoms):
    # printa som (row, col): value
    print(f"{anom[0]}: {anom[1]}, ", end="")
