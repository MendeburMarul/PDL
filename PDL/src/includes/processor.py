class processor:
    def __init__(self, sdl, sdlext):
        self.processor = sdlext.TestEventProcessor()
        self.sdl = sdl
        self.sdlext = sdlext

    def run(self, window):
        self.processor.run(window)

        return 0
