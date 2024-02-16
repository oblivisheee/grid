from typing import Tuple

def auto_coordinates(grid) -> Tuple[int, int, int]:
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            for z in range(grid.shape[2]):
                if grid[x, y, z] is None:
                    return (x, y, z)
    return (grid.shape[0]-1, grid.shape[1]-1, grid.shape[2]-1)
