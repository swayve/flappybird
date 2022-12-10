from ursina import *
game = Ursina()

cube = Entity(model="quad", color=color.green, scale=(1,4), position= (5,0))

sans = Entity(model="quad", texture='minecraft_blok.png.png', scale=(1,1))

def update():
    if held_keys["w"]:
        cube.y += 3.5 * time.dt 
    if held_keys["s"]:
        cube.y -= 3.5 * time.dt 
    if held_keys["a"]:
        cube.x -= 3.5 * time.dt 
    if held_keys["d"]:
        cube.x += 3.5 * time.dt 


game.run()
