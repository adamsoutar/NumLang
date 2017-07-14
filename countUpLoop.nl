#Count up loop
This script counts from 0 to the user's input, then exits;
setsilent true;
expand 3;
memset 0|%INPUT%;
copyfrom 0;
copyto 1;
#Loop;
copyfrom 2;
bumpdown 1;
bump 2;
copyfrom 1;
out %SELECTOR%;
jumpIfZero 15;
jump 7;
terminate;