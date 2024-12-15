from typing import Any, Iterable

from libraries.wall import Wall


class Map:
    """Map object that will contain all sorts of objects for interacting."""

    X_SIZE = 10
    Y_SIZE = 10

    def __init__(self):
        self.grid: list[list[Any]] = [[None for _ in range(self.X_SIZE)] for _ in range(self.Y_SIZE)]

    def get_object_in_position(self, x_axis: int, y_axis: int) -> Any | Wall:
        if x_axis < 0 or y_axis < 0:
            return Wall
        try:
            return self.grid[y_axis][x_axis]
        except IndexError:
            return Wall

    def add_object_in_position(self, object: Any, x_axis: int = 0, y_axis: int = 0) -> None:
        self.grid[y_axis][x_axis] = object

    def empty_position(self, x_axis: int, y_axis: int) -> None:
        self.grid[y_axis][x_axis] = None

    def validate_coordinates(self, coordinates: Iterable[tuple[int, int]]) -> list:
        """Check if coordinates given in a list are valid, return a list with validated coordinates."""
        validated_coordinates = []
        for coordinate in coordinates:
            x, y = coordinate
            if y > self.Y_SIZE - 1 or y < 0 or x > self.X_SIZE - 1 or x < 0:
                continue
            else:
                validated_coordinates.append(coordinate)

        return validated_coordinates


MAP = Map()
GRID = MAP.grid
