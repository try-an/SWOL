# command: python swol_file_compiler.py [-c] filepath

import argparse
from SwolModule import SWOL
from time import strftime, sleep

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--compile", action="store_true", help="Compile the script to a python file (will be stored in the compiled directory)")
parser.add_argument("filepath", help="File path to your script")
args = parser.parse_args()

print("SWOL by Tryan09\n")

is_compiled = args.compile
script_path = args.filepath

swol = SWOL()

with open(script_path, "r") as script_content:
    swol_script = script_content.read()

python_code = swol.compile_to_py(swol_script)

print(python_code+"\n")

if is_compiled:
    current_date = strftime("%d-%m-%Y-%H-%M-%S")
    with open(f"compiled/{current_date}.py", "x") as compiled_file:
        compiled_file.write(python_code)
else:
    exec(python_code)

sleep(0.5)
print("Program will end in 5 secs")
sleep(5)
