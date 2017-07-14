#NumLang Library
#Part of the Python NumLang Interpreter
#
#By Adam Soutar

#Imports
import sys
import random
#End Imports

#Values
global pbMemory
pbMemory = []

global runSilent
runSilent = False

global scriptSilence
scriptSilence = False

global splitChar
splitChar = " "

global midSplitChar
midSplitChar = "|"

global pbSelector
pbSelector = 0

global startupPhrases
startupPhrases = ['Est. -1 years ago!', "It's like Assembly. But it's not Assembly!", "NumLang, a language with numbers. Damn, should've called it LangNumbs.", "Becoming self aware...", "Not Skynet!"]
#End Values

#Write to the console only if not running silent
def writeToDebug(debugStr):
    if (runSilent==False):
        print(debugStr)

#Expand memory array by given bytes
def pbExpandMemory(expArgs):
    for i in range(int(expArgs)):
        pbMemory.append(0)
    writeToDebug('Memory was expanded by ' + str(expArgs) + ' bytes.')

#Bump positive
def pbBump(pushArgs):
    pbMemory[int(pushArgs)] = pbMemory[int(pushArgs)] + 1
    writeToDebug("Bumped memory address " + pushArgs)

#Bump negative
def pbBumpDown(pushArgs):
    pbMemory[int(pushArgs)] = pbMemory[int(pushArgs)] - 1
    writeToDebug("Reverse bumped memory address " + pushArgs)

#Dump memory and selector
def pbDumpMem(args):
    writeToDebug("Memory dump:")
    writeToDebug(pbMemory)
    writeToDebug("Selector value:")
    writeToDebug(pbSelector)

#Show help file
def pbShowHelp(helpArgs):
    nLS = open('NumLangHelp.txt', 'r')
    writeToDebug(nLS.read())
    nLS.close()

#Explicitly sets a memory address
def pbMemSet(memArgs):
    memArray = memArgs.split(midSplitChar)
    pbMemory[int(memArray[0])] = int(memArray[1])
    writeToDebug('Memory address ' + str(memArray[0]) + ' set to ' + str(memArray[1]))

#Sets the selector to a memory address
def pbCopyFrom(copyArgs):
    global pbSelector
    pbSelector = pbMemory[int(copyArgs)]
    writeToDebug('Copied ' + str(pbMemory[int(copyArgs)]) + ' to selector from memory address ' + str(copyArgs))

#Sets a memory address to the value of the selector
def pbCopyTo(copyArgs):
    global pbSelector
    global pbMemory
    pbMemory[int(copyArgs)] = pbSelector
    writeToDebug('Copied selector (' + str(pbSelector) + ') to memory address ' + str(copyArgs))

#Add to selector
def pbAdd(addArgs):
    global pbSelector
    pbSelector = pbSelector + pbMemory[int(addArgs)]
    writeToDebug('Added value of memory address ' + str(addArgs) + ' (' + str(pbMemory[int(addArgs)]) + ') to the selector.')

#Print (if user hasn't silenced the program)
def pbOutput(outArgs):
    if (scriptSilence==False):
        print(outArgs)

#Set basic silent value - Not script silence
def pbSetSilent(silentArgs):
    global runSilent
    if (silentArgs=='true'):
        runSilent = True
    else:
        runSilent = False


#Subtract from selector
def pbSubtract(subArgs):
    global pbSelector
    pbSelector = pbSelector - pbMemory[int(subArgs)]
    writeToDebug('Subtracted value of memory address ' + str(subArgs) + ' (' + str(pbMemory[int(subArgs)]) + ') from the selector.')

#Process a command
def processCommand(commandIn):
    commandIn = str(commandIn.lower())
    if (commandIn!="quit"):
        #Input pre-check
        while (commandIn.find("%input%")!=-1):
            inTake = input("NumLang Input > ")
            commandIn = commandIn.replace('%input%', str(inTake), 1)
        commandIn = commandIn.replace('%selector%', str(pbSelector))
        #Split to get commands
        cmdSplit = commandIn.split(splitChar)
        cmdDo = cmdSplit[0]
        commandDictionary = {'bump' : pbBump, 'bumpdown' : pbBumpDown, 'expand' : pbExpandMemory, 'dump' : pbDumpMem, 'copyfrom' : pbCopyFrom, 'memset' : pbMemSet, 'copyto' : pbCopyTo, 'add' : pbAdd, 'subtract' : pbSubtract, 'out' : pbOutput, 'setsilent' : pbSetSilent, 'help' : pbShowHelp}
        #Execute command with or without arguments
        if (len(cmdSplit) > 1):
            commandDictionary[cmdDo] (cmdSplit[1])
        else:
            #Called without arguments
            commandDictionary[cmdDo] ('NOARGS')
    else:
        #Exit interpreter
        sys.exit(0)
    
def printLogo():
    print("""
         _   _ _    _ __  __ _               _   _  _____ 
        | \ | | |  | |  \/  | |        /\   | \ | |/ ____|
        |  \| | |  | | \  / | |       /  \  |  \| | |  __ 
        | . ` | |  | | |\/| | |      / /\ \ | . ` | | |_ |
        | |\  | |__| | |  | | |____ / ____ \| |\  | |__| |
        |_| \_|\____/|_|  |_|______/_/    \_\_| \_|\_____|
              NumLang Copyright 2017 Adam Soutar
        """)
    random.shuffle(startupPhrases)
    print(startupPhrases[0])
    print("")