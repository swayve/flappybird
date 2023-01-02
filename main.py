from ursina import *
from random import *
app = Ursina()


offset = 0
run = True
num = 0
x = 6

window.title = "Flappy bird game"
bg = Entity(model="quad",scale=(30, 15), texture="bg.png")
bird = Entity(model= "quad",texture="bird.png", scale=(2, 1), postition = (-4, 0) )




class Pipe(Entity):
    def __init__(self, x, y, img):
        super().__init__()
        self.model = "quad"
        self.texture = img
        self.scale = (1, 5)
        self.x = x
        self.y = y 
        self.position = Vec2(x, y)
        self.collider = "box"
        
        


def input(key):
     
    if key == "w":
        bird.y +=  20 * time.dt
    
    if key == "s":
        bird.y -= 20 * time.dt
    
    #Here we want to get the bird moving forward so we do that by the bird.x * frame.screen or some code like that so the bird goes forward by multiplying the frame time
    

        
        
pipe_down = [None] * num
pipe_down = Pipe(x, -4, "PipeUp.png")
pipe_up = [None] * num
pipe_up = Pipe(x, -4+9, "PipeDown.png")

for m in range(1, num):
    x += 4
    y = -7 + randint(0, 50) / 10
    pipe_down[m] = Pipe(x, y, "PipeUp.png")
    pipe_up[m] = Pipe(x, y+5, "PipeDown.png")
    

def update():
    global offset, run
    if run:
    #rolling bg
        bird.x += 1 * time.dt 

        offset += time.dt*.2
        setattr(bg, "texture_offset", (offset, 0))
        for m in range(num):
            pipe_up[m].x -= time.dt * 1.8
            pipe_down[m].x -= time.dt * 1.8
        

        


app.run()