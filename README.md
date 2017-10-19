# random-robots-txt
Generates a random robots.txt deny list to throw script kiddies off the scent.

## Requirements

#### OS   
OSX or Ubuntu

#### SOFTWARE   
Python 3.6+   
Check that /usr/share/dict/words exists for your os and `shuf` or `gshuf` commands work.   
If not, in ubuntu install `sudo apt install wamerican coreutils` or in OSX `brew install coreutils`

## CONFIG   
Change the global variable `numberofwords` in each .py file to the number of deny paths to generate in the robots.txt file.

## RUN   
To run on OSX, simply `python3 gen-robots-osx.py` or `python3.6 gen-robots-osx.py` if you have multiple pythons installed.

