# import modules
from SwolModule import SWOL
from time import strftime, sleep

print("SWOL by Tryan09")

# choose mode
run_mode = input("Select mode: run/compile >> ")

# getting swol file path
script_path = input("Put the path to the script that you want to run or compile >> ")

swol = SWOL()

with open(script_path, "r") as script_content:
    swol_script = script_content.read()

python_code = swol.compile_to_py(swol_script)

# execute or compile
print(python_code+"\n")

if run_mode == "run":
    exec(python_code)
elif run_mode == "compile":
    current_date = strftime("%d-%m-%Y-%H-%M-%S")
    with open(f"compiled/{current_date}.py", "x") as compiled_file:
        compiled_file.write(python_code)
else:
    raise NameError("Mode must be 'run' or 'compile'")

sleep(0.5)
print("Program will end in 5 secs")
sleep(5)
