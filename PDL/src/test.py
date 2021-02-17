def makeBeforeGameloop(sdl, sdlext):

    global wd
    wd = PDLwindow(sdl, sdlext, "deneme", (800, 600))
    wd = wd.createWindow()
    wd.show()

    global processor
    processor = processor(sdl, sdlext)
    processor.run(wd)

    return wd

def gameloop(sdl, sdlext, isRunning):
    wd = makeBeforeGameloop(sdl, sdlext)
    
    global pdoext
    pdoext = pdo.ext(sdl, sdlext)

    global running
    running = isRunning

    while running:
        events = pdoext.get_events()
        for event in events:

            if event.type == pdo.QUIT_EVENT:
                running = 0
                break
        
        wd.refresh()
    return isRunning