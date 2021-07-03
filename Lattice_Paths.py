DIM = 20
grid = [[1] * (DIM+1) for _ in range(DIM+1)]
for i in range(1, DIM+1):
    for j in range(1, DIM+1):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

for row in grid:
    print(" ".join(map(str, row)))

print(grid[-1][-1])