from ursina import *
app = Ursina()
window.title = "Flappy bird game"
window.fullscreen = False
bg = Entity(model="quad",scale=(30, 15), texture="bg.png")

class PipeUp(Entity):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.model = "quad"
        self.texture = "Pipedown.png"
        self.scale = (1, 4)
        self.position = Vec2(pos_x,pos_y)

class PipeDown(Entity):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.model = "quad"
        self.texture = "PipeUp.png"
        self.scale = (1, 4)
        self.position = Vec2(pos_x,pos_y)

PipeUp(-5, 3)
PipeDown(-5, -3)

app.run()