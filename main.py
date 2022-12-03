from ursina import *

def update():
    cube.x -= 0.1

game = Ursina()

cube = Entity(model="cube", color=color.green, scale=(1,4), position= (5,4))



game.run()
print("nigger")
