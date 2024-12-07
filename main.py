from typing import Any, Literal

class Wall:
    """Non empty class to represent a wall."""

class Map:
    """Map object that will contain all sorts of objects for interacting."""
    grid: list[list[Any]] = [
        [None, None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None, None,],
    ]

    def get_object_in_position(self, x_axis: int, y_axis: int) -> Any | Wall:
        if x_axis < 0 or y_axis < 0:
            return Wall
        try:
            return self.grid[y_axis][x_axis]
        except IndexError:
            return Wall
    
    def add_object_in_position(self, object: Any, x_axis: int = 0, y_axis: int = 0) -> None :
        self.grid[y_axis][x_axis] = object

    def empty_position(self, x_axis: int, y_axis: int) -> None:
        self.grid[y_axis][x_axis] = None

    
MAP = Map()
GRID = MAP.grid

class Goblin:
    """Goblin object."""
    map = MAP
    def __init__(self, x_axis: int = 0, y_axis: int = 0) -> None:
        """Initializing a goblin."""
        self.health = 100
        self.attack = 10
        self.gold = 5
        self.x_axis, self.y_axis = x_axis, y_axis
        self.add_self_to_coordinates()

    def add_self_to_coordinates(self) -> None:
        """Use our own coordinates to insert ourselves in the map."""
        return self.map.add_object_in_position(self, self.x_axis, self.y_axis)
        
    def remove_self_from_coordinates(self) -> None:
        """Remove object located on our own coordinates."""
        return self.map.empty_position(self.x_axis, self.y_axis)

    def move(self, direction: Literal["up", "down", "left", "right"]) -> None:
        """Logic for movement within the grid."""
        match direction:
            case "up":
                new_y = self.y_axis + 1
                object_in_new_position = self.map.get_object_in_position(self.x_axis, new_y)
                if object_in_new_position is None:
                    self.remove_self_from_coordinates()
                    self.y_axis = new_y
                    self.add_self_to_coordinates()
            case "down":
                new_y = self.y_axis - 1
                object_in_new_position = self.map.get_object_in_position(self.x_axis, new_y)
                if object_in_new_position is None:
                    self.remove_self_from_coordinates()
                    self.y_axis = new_y
                    self.add_self_to_coordinates()
            case "left":
                new_x = self.x_axis - 1
                object_in_new_position = self.map.get_object_in_position(new_x, self.y_axis)
                if object_in_new_position is None:
                    self.remove_self_from_coordinates()
                    self.x_axis = new_x
                    self.add_self_to_coordinates()
            case "right":
                new_x = self.x_axis + 1
                object_in_new_position = self.map.get_object_in_position(new_x, self.y_axis)
                if object_in_new_position is None:
                    self.remove_self_from_coordinates()
                    self.x_axis = new_x
                    self.add_self_to_coordinates()
            case _:
                raise ValueError("Invalid direction.")
        print((self.x_axis, self.y_axis))
    
    def __str__(self):
        """Basic representation of a goblin on screen."""
        return "G"
            
def display_grid():
    """Displays the grid on the screen."""
    print("-" * 2 * len(GRID))
    for row in GRID[::-1]:
        print(" ".join("." if cell is None else str(cell) for cell in row), end="\n")
            
if __name__ == "__main__":
    g = Goblin()
    while True:
        display_grid()
        player_input = input()
        match player_input:
            case "w":
                g.move("up")
            case "s":
                g.move("down")
            case "d":
                g.move("right")
            case "a": 
                g.move("left")
            case "q":
                break
    
