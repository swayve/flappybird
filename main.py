from ursina import *
app = Ursina()


bg = Entity(model="quad",scale=(20, 10), texture="bg.png")

class PipeUp(Entity):
    def __init__(self):
        super().__init__()
        self.model = "quad"
        self.texture = "PipeUp.png"
        self.scale = (1,2)
        self.position = (4,1)

PipeUp()
app.run()