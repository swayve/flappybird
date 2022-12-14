from ursina import *
from random import *
app = Ursina()
def update():
    global offset, run
    if run:
        #rolling bg
        offset += time.dt*.2
        setattr(bg, "texture_offset", (offset, 0))

window.title = "Flappy bird game"
window.fullscreen = False
bg = Entity(model="quad",scale=(30, 15), texture="bg.png")
bird = Animation("Bird.png", collider="box", scale= (1.3, .8), y=1.5)



class Pipe(Entity):
    def __init__(self, x, y, img):
        super().__init__()
        self.model = "quad"
        self.texture = img
        self.scale = (1, 7)
        self.x = x
        self.y = y 
        self.position = Vec2(x, y)
        self.collider = "box"
        self.score_tag = True

def input(key):
    if key == "up arrow":
        bird.y += .25

        
 



offset = 0
run = True
num_pipes = 5
x = 6

pipe_bottom = [None]*num_pipes
pipe_bottom[0] = Pipe(x, -4, "PipeUp.png")
pipe_top = [None]*num_pipes
pipe_top[0]=Pipe(x, -4+9, "PipeDown.png")

for m in range(1, num_pipes):
    x+= 4
    y =- 7 + randint(0, 50)/10
    pipe_bottom[m] = Pipe(x, y, "PipeUp.png")
    pipe_top[m]= Pipe(x, y + 9, "PipeDown.png")





app.run()