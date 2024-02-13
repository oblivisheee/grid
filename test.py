from grid import grid

grid_test = grid.Grid("example", (3,3,3))
grid_test.genesis()
for x in range(3):
    for y in range(3):
        for z in range(3):
            grid_test.add("test", "test",)

print(grid_test.get())