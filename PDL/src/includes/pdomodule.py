
class pdo:

    QUIT_EVENT = 256

    class ext:
        def __init__(self, sdl, sdlext):
            self.sdl = sdl
            self.sdlext = sdlext

        def get_events(self):
            return self.sdlext.get_events()

        def color(self, colorRGB):
            return self.sdlext.Color(255, 255, 255)

        def World(self):
            return self.sdl.ext.World()
