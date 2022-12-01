from ursina import *
game = Ursina()


def update():
    print("Update!")                    # Print Update every time this loop is executed
    if held_keys['t']:                  # If t is pressed
        print(held_keys['t'])           # Print the value




game.run()