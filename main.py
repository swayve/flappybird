from ursina import *
from random import *
app = Ursina()


offset = 0
run = True
n_frame = 0

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
    
    #Here we want to get the bird moving forward so we do that by the bird.x * frame.screen or some code like that so the bird goes forward by multiplying the frame time
    
def update():
    global offset, run, n_frame
    if run:
    #rolling bg
        n_frame += 1
        bird.x += 1 * time.dt
        offset += time.dt*.2
        setattr(bg, "texture_offset", (offset, 0))
        

pipe_up = Pipe(x=3, y=3, img="PipeDown.png")
pipr_down = Pipe(x=3, y=-3, img="PipeUp.png")




app.run()