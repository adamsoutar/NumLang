#A NumLang looping program
Counts down from the number the user enters before quitting;
setsilent true;
expand 2;
memset 0|%INPUT%;
#Loop;
copyfrom 0;
out %SELECTOR%;
bumpdown 0;
copyfrom 0;
jumpIfZero 12;
jump 5;
out Done;
terminate;