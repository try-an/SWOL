# by Ryan Tahenni
# made in 4 days
#-------------------
# The concept is simple:
# First: we import the json files
#           - tokens.json defines the SWOL tokens and their translation into python
#           - python_keywords_and_functions.json is meant for scanning the script
#              made in SWOL for python functions beacause we dont want a swol script
#              containing python functions
#           - forbidden_python_functions.json is meant for scanning the final python
#              script for forbidden functions for a similar reason as python_keywords_and_functions.json:
#              we don't want our swol script executing extra python functions
# Second: with the tokens.json file, we "translate" our swol script to python
#           - Add swol token translation to final python script
#           - Resolve tokens that were not translated (see line 67 to 72)
#           - Scan if there are python keywords inside the swol script with python_keywords_and_functions.json
# Third: we do a final scan for forbidden functions with forbidden_python_functions.json
# Four: we execute or compile the script based on the "run_mode variable"


# import modules
from json import loads
from time import strftime


# choose mode
run_mode = input("Select mode: run/compile >> ")


# load json files
with open("tokens.json", "r") as list_of_tokens:
    TOKENS = loads(list_of_tokens.read())

with open("python_keywords_and_functions.json", "r") as py_tokens:
    FORBIDDEN_TOKENS = loads(py_tokens.read())

with open("forbidden_python_functions.json", "r") as forbid_functions:
    FORBIDDEN_FUNCTIONS = loads(forbid_functions.read())


# open script
script_path = input("Put the path to the script that you want to run or compile >> ")

with open(script_path, "r") as script_content:
    code_tokens = script_content.read().split("_")

python_code = []


# scan if the script has multiple lines
for token in code_tokens:
    if "\n" in token:
        has_multiple_lines = True
        break
    else:
        has_multiple_lines = False


# translate code from SWOL to python
def convert_swol_to_py_token(swol_token: str):
    return TOKENS.get(swol_token)

def get_index_of_current_python_token(python_token: str):
    return python_code.index(python_token)

def has_python_function_or_keyword(current_token: str):
    for element in FORBIDDEN_TOKENS:
        if element in current_token:
            return True
    return False

def scan_for_forbidden_functions(script: str):
    for element in FORBIDDEN_FUNCTIONS:
        if element in script:
            return True
        else:
            continue
    return False

def add_token_to_final_script(current_token: str, final_script: list):
    final_script.append(convert_swol_to_py_token(current_token))

def index_of_current_py_token(current_token: str):
    return get_index_of_current_python_token(convert_swol_to_py_token(current_token))

def build_py_code(swol_script: list, py_script: list):
    for token in swol_script:
        add_token_to_final_script(token, py_script)

        if py_script[index_of_current_py_token(token)] == None:
            if has_python_function_or_keyword(token):
                print(f"Error: Your script contains a python keyword of function at: '{token}'")
                return "".join(py_script)
            else:
                py_script[index_of_current_py_token(token)] = token

    return "".join(py_script)

python_code = build_py_code(code_tokens, python_code)


# execute or compile
print(python_code)
print("")

if scan_for_forbidden_functions(python_code) == False:
    if has_multiple_lines:
        print("Error: script must contain one line")
    else:
        if run_mode == "run":
            exec(python_code)
        elif run_mode == "compile":
            current_date = strftime("%d-%m-%Y-%H-%M-%S")
            with open(f"compiled/{current_date}.py", "x") as compiled_file:
                compiled_file.write(python_code)
        else:
            print("Error: Mode must be 'run' or 'compile'")
else:
    print("Error: Final script contains forbidden functions")
