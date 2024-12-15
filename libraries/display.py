from libraries.map import GRID


def display_grid() -> None:
    """Displays the grid on the screen."""
    print("-" * 2 * len(GRID))
    for row in GRID[::-1]:
        print(" ".join("." if cell is None else str(cell) for cell in row), end="\n")
