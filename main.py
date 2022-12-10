from ursina import *
game = Ursina()

class Test_Cube(Entity):
    def __init__(self,):
        super().__init__(
            model = "cube",
            color = color.white,
            texture = "white_cube",
            rotation = Vec3(30, 30, 30)
        )



class Test_Button(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "cube",
            texture = "brick",
            color = color.blue,
            scale = (1, 1),
            position = (5, 0)
        )
    
    


def update():
    if held_keys["w"]:
        cube.y += 3.5 * time.dt 
    if held_keys["s"]:
        cube.y -= 3.5 * time.dt 
    if held_keys["a"]:
        cube.x -= 3.5 * time.dt 
    if held_keys["d"]:
        cube.x += 3.5 * time.dt 

#cube = Entity(model="quad", color=color.green, scale=(1,4), position= (5,0))
#minecraft_cube = Entity(model="cube", texture='minecraft_blok.png.png', scale=(1,1), position = (1,1), rotation = Vec3(30, 30, 30))
test_cube = Test_Button()
game.run()
