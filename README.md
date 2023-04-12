# SWOL

------------------
S.W.O.L. is a very buggy esolang built on top of python. It stands for: Slow Weird One Line (for the language) or Script With One Line (for the file format (.swol)).

One perk is that SWOL scripts are written in only one line and you have to seperate everything (functions, strings etc...) with underscores.

Another thing is that SWOL is compiled differently by translating directly it's tokens to python.

-----------------
**To use this language:**
  1. Download python ([https://www.python.org/downloads/](https://www.python.org/downloads/))
  2. Download the repo
  3. Create a file that ends in .swol with any editor (eg. Notepad)
  4. Try a script like this: `a_=_I_(_"What's your name? "_)_;_P_(_"Hello, "_+_a_)`
  5. Run swol_file_compiler.py, set the mode to run, type the path to the file
  6. If everything worked, it sould print the python version and run the script

-----------------
**Coming soon...(?):**
  - [ ] A REPL (1)
  - [x] A module for translating SWOL to python


(1): read-eval-print-loop
