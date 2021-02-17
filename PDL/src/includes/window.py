class PDLwindow:

    def __init__(self, sdl, sdlext, title, size):

        self.sdlext = sdlext
        self.sdl = sdl
        self.title = title
        self.size = size
        self.window = None

    def initWindow(self):
        self.sdlext.init()

    def createWindow(self):
        self.window = self.sdlext.Window(self.title, size=self.size)

        return self.window
