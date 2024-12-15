from libraries.goblin import Goblin
from libraries.display import display_grid


if __name__ == "__main__":
    from time import sleep
    g1 = Goblin()
    g2 = Goblin(9, 9)
    while True:
        g1.act()
        g2.act()
        display_grid()
        sleep(1)
