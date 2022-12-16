from ursina import *
from random import *
app = Ursina()



        
offset = 0
run = True
num_pipes = 5
x = 6

window.title = "Flappy bird game"
bg = Entity(model="quad",scale=(30, 15), texture="bg.png")
bird = Entity(model= "quad",texture="bird.png", scale=(2, 1), postition = (0, 0) )




class Pipe(Entity):
    def __init__(self, x, y, img):
        super().__init__()
        self.model = "quad"
        self.texture = img
        self.scale = (1, 5)
        self.x = x
        self.y = y 
        self.position = Vec2(x, y)
      


def input(key):
    if key == "w":
        bird.y +=  20 * time.dt
    
    if key == "s":
        bird.y -= 20 * time.dt
    
    
def update():
    global offset, run
    if run:
    #rolling bg
        offset += time.dt*.2
        setattr(bg, "texture_offset", (offset, 0))
        

pipe_up = Pipe(x=3, y=3, img="PipeDown.png")
pipr_down = Pipe(x=3, y=-3, img="PipeUp.png")




app.run()