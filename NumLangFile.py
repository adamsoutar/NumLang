#NumLang File Interpreter
#Reads NumLang scripts and also adds JUMP support
#
#By Adam Soutar

#Imports
import NumLang
import sys
#End Imports

NumLang.printLogo()
print('')

#Variables and script reading
global numLangScriptPath
numLangScriptPath = str(input('Execute Script Path > '))

global numLangScriptText
nLS = open(numLangScriptPath, 'r')
numLangScriptText = nLS.read()
nLS.close()
#End variables

def executeNumLangScript(txtIn):
    scriptLineNum = 0
    scriptTerminated = False
    scriptLineArray = txtIn.split(';')
    while (scriptTerminated==False):
        if (scriptLineNum>len(scriptLineArray) - 1):
            break
        currentLine = scriptLineArray[scriptLineNum]
        currentLine = currentLine.replace('\n','')
        #If not comment
        if (currentLine!=''):
            if (currentLine[0]!='#'):
                #If not terminator
                if (currentLine.lower()!='terminate'):
                    if (currentLine.lower().find('jump')==-1):
                        if (currentLine.lower().find('module')==-1):
                            NumLang.processCommand(currentLine)
                        else:
                            nLS2 = open(currentLine.split(' ')[1], 'r')
                            numLangScriptText2 = nLS2.read()
                            nLS2.close()
                            executeNumLangScript(numLangScriptText2)
                    else:
                        #Jump structure
                        if (currentLine.lower().find('jumpifzero')==-1):
                            scriptLineNum = int(currentLine.split(' ')[1]) - 2
                        else:
                            if (int(NumLang.pbSelector)==0):
                                scriptLineNum = int(currentLine.split(' ')[1]) - 2
                else:
                    scriptTerminated = True
        scriptLineNum = scriptLineNum + 1

executeNumLangScript(numLangScriptText)

sys.exit(0)