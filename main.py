from ursina import *
app = Ursina()


bg = Entity(model="quad",scale=(20, 10), texture="46888871-624a3900-ce7f-11e8-808e-99fd90c8a3f4.png" )

class PipeUp(Entity):
    def __init__(self):
        super().__init__()
        self.model = "quad"
        Vec2(1, 1)
        self.scale = (1,4)
        self.texture = "pipe_up.png"
        self.postion = (-.5, -.5)
        self.collider = "quad"

PipeUp()
app.run()