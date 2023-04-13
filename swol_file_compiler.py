# command: "python swol_file_compiler.py [--compile] [--output OUTPUT] filepath"

import argparse
from SwolModule import SWOL
from time import strftime, sleep

parser = argparse.ArgumentParser(prog="SWOL File Compiler", description="Compile a SWOL script to python", epilog="Language made by Tryan09")
parser.add_argument("-c", "--compile", action="store_true", help="Compile the script to a python file")
parser.add_argument("filepath", help="File path to your script")
parser.add_argument("-o", "--output", help="File path to the output python file", required=False)
args = parser.parse_args()

print("SWOL by Tryan09\n")

is_compiled = args.compile
script_path = args.filepath

if args.output == None:
    current_date = strftime("%d-%m-%Y-%H-%M-%S")
    output_path = f"compiled/{current_date}.py"
elif args.output[-3:] == ".py":
    output_path = args.output
else:
    output_path = args.output + ".py"

swol = SWOL()

with open(script_path, "r") as script_content:
    swol_script = script_content.read()

python_code = swol.compile_to_py(swol_script)

print(python_code+"\n")

if is_compiled:
    with open(output_path, "x") as compiled_file:
        compiled_file.write(python_code)
else:
    exec(python_code)

sleep(0.5)
print("Program will end in 5 secs")
sleep(5)
