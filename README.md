# NumLang
A basic number-handling memory-based programming language using an interpreter written in Python. 

## What is NumLang?
NumLang (Number Language) is just a small test in Python. It has a small command set, but, in theory, it should be possible to replicate almost any processing algorithm on Earth, be it rather impracticle to do so.

## Uses
NumLang is great for education and teaching students about Assembly Language in a human-readable format. Due to its Python-based interpreter, it is cross-platform and even web compatible.

## Try it
To try out the basic language, there's a Repl.it link to an online version of the language:
https://repl.it/J07t/1

Be aware that this web build is very limited and misses the constructs like 'Jump' and 'Module' which make some algorithms and loops possible. For this functionality you have to write NumLang script.

## NumLang Script
NumLang scripts come in a '.nl' format and can be minified due to their lines only being separated by semicolons (;).
NumLang's file interpreter ignores the new line character.
```
#This is an example NumLang Script!
This is a multi-line comment because I haven't used a semicolon yet.;
#This is a one-line comment;
out SomeOutput;
expand 2;
bump 0;
bump 0;
memset 1|5;
copyfrom 1;
add 0;
out Result:%SELECTOR%;
terminate;
```

This program outputs '7' because it followed the following steps (which it outputs):
![A NumLang Program](http://overflo.me/numlang/NumLangScreenshot.png)

To stop NumLang from outputting its actions, you can use
`setsilent true;`

Here is the same demo with `setsilent true;` on the first line:
```
Execute Script Path > 'gitHubDemo.nl'
someoutput
result:7
```
## NumLang Embedded

NumLang is ridiculously easy to implement in Python, with more language support coming in the future.

For example, this is the actual script required for a working NumLang interpreter in Python:
```
import NumLang
while True:
    NumLang.processCommand(input('NumLang > '))
```
That's it! Three lines.

With this power, you can create Python scripts which perform complex NumLang operations, returning the results to Python. For example, say you want to perform a complex maths operation. Instead of creating a Python subroutine, try this:
Place your maths operation into `operation.nl`, then try this:

(Python Script - Not NumLang)
```
import NumLang
NumLang.pbExpandMemory('3')
NumLang.pbMemory[0] = 21
NumLang.pbMemory[1] = 46
NumLang.processCommand('module operation.nl')
print('Output: ' + str(NumLang.pbMemory[2]))
```
