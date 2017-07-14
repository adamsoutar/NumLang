#Python 'NumLang'
#A real time interpreter for NumLang - An assembly-like language
#
#By adam Soutar

#Imports
import NumLang
#End Imports

NumLang.printLogo()

print('')
print('Info:')
print("""This is a NumLang console. 
You cannot execute multiple commands at once, although memory is persistent. 
For constructs such as Jump, SubTerminate and Module, you need to create a .nl script
 and run it with the NumLang file interpreter.""")

while True:
    NumLang.processCommand(input('NumLang > '))