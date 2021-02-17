import sys
import os

from includes import *

try:
    import sdl2
except ImportError as identifier:
    print('Error in importing Simple DirectMedia Layer, here is an error info about it: '+str(identifier))

try:
    import sdl2.ext
except ImportError as identifier:
    print('Error in importing Simple DirectMedia Layer Extensions, here is an error: '+str(identifier))


argv = sys.argv
executedFile = None
isCommandHasFile = None
fileData = None


def argType(arg):
    isDirExitsts = os.path.isfile(arg)

    if arg == "src/main.py":
        return "mainFile"

    elif arg == "-i" or arg == "-file":
        return "file or directory idenitiyfier"

    elif isDirExitsts:
        return "file or directory"
    elif arg == "-m":
        return "Module Idenitifier"

    elif arg == "-c":
        return "compile"

    elif arg == "python3" or arg == "python":
        return "pythonExecute"

    else:
        return "IDK"


def generateArgv2(passedArgv):

    generatedArgList = []

    for arg in passedArgv:
        typeOfArg = argType(arg)

        if not typeOfArg == "IDK":
            generatedArgList.append([arg, typeOfArg])
        else:
            generatedArgList.append([arg, "maybeFile"])

    return generatedArgList


realArgs = generateArgv2(argv)


print(argv)

print(realArgs)

for i in range(len(realArgs)):
    _list = realArgs[i]

    arg = realArgs[i][0]
    typeOfArg = realArgs[i][1]

    if typeOfArg == "file or directory":


            executedFile = arg

            isCommandHasFile = 1

    if typeOfArg == "file or directory idenitiyfier":

            executedFile = realArgs[i + 1][0]

            isCommandHasFile = 1

    if typeOfArg == "maybeFile":

            if realArgs[i - 1][1] == "file or directory idenitiyfier":

                executedFile = arg

                isCommandHasFile = 1

                realArgs[i] = [arg, "file or directory"]

    if arg == "-c":

        pass

    if arg == "-m":

        pass


if isCommandHasFile:

    fileData = open(executedFile, "r+").read()

elif not isCommandHasFile:

    raise Exception("Command does not have a file inside on it.")
global running
class main:

    global sdl, sdlext

    def __init__(self, realArgs, argv, fileData, isCommandHasFile, sdlext, sdl):
        self.realArgs = realArgs
        self.argv = argv
        self.fileData = fileData
        self.isCommandHasFile = isCommandHasFile
        self.sdlext = sdlext
        self.sdl = sdl
        self.curError = ""

    def __str__(self):
        return "str return sucsessfuly"

    def setup(self):

        running = 0

        exec(self.fileData, globals())

    def run(self):
        try:

            global running

            running = 1

            gameloop(self.sdl, self.sdlext, running)

        except Exception as err:

            print("error at runtime: "+str(err))

    def getsdl(self):
        return self.sdl

    def getsdlext(self):
        return self.sdlext

if not fileData == None:

    sdlext = sdl2.ext
    sdl = sdl2

    mainCodeClass = main(realArgs, argv, fileData, isCommandHasFile, sdlext, sdl)

    mainCodeClass.setup()
    mainCodeClass.run()
