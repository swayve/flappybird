from ursina import *
game = Ursina()

cube = Entity(model="quad", color=color.green, scale=(1,4), position= (5,0))
sans_texture = load_texture('minecraft_blok.png.png')
sans = Entity(model="quad", texture=sans_texture, scale=(1,1))

def update():
    if held_keys["w"]:
        cube.y += 1 * time.dt 
    if held_keys["s"]:
        cube.y -= 1 * time.dt 
    if held_keys["a"]:
        cube.x -= 1 * time.dt 
    if held_keys["d"]:
        cube.x += 1 * time.dt 


game.run()
