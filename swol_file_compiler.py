# by Tryan09
#-------------------
# The concept is really simple:
# First: load the dicts and the lists
#           - TOKENS defines the SWOL tokens and their translation into python
#           - FORBIDDEN_TOKENS is meant for scanning the script
#              made in SWOL for python functions beacause we dont want a swol script
#              containing python functions
#           - FORBIDDEN_FUNCTIONS is meant for scanning the final python
#              script for forbidden functions for a similar reason as FORBIDDEN_TOKENS:
#              we don't want our swol script executing extra python functions
# Second: with the TOKENS dict, we "translate" our swol script to python
#           - Add swol token translation to final python script
#           - Resolve tokens that were not translated (see line 152 to 166)
#           - Scan if there are python keywords inside the swol script with FORBIDDEN_TOKENS
# Third: we do a final scan for forbidden functions with FORBIDDEN_FUNCTIONS
# Four: we execute or compile the script based on the "run_mode variable"


# import modules
from time import strftime, sleep

print("SWOL by Tryan09")

# choose mode
run_mode = input("Select mode: run/compile >> ")


# load dicts and lists
TOKENS = {';': '\n',
        ':': ':',
        '}': '    ',
        '"': '"',

        '=': '=',
        '+': '+',
        '-': '-',
        '*': '*',
        '^': '**',
        '/': '/',
        '%': '%',
        '#': '//',
        '(': '(',
        ')': ')',
        
        'I': 'input',
        'P': 'print',
        
        'i': 'int',
        'fl': 'float',
        's': 'str',
        'bl': 'bool',
        
        'F': 'def ',
        'ret': 'return ',
        
        'R': 'for i in range',
        'W': 'while ',
        
        'IF': 'if ',
        'ELF': 'elif ',
        'ELS': 'else',
        '<': '<',
        '>': '>',
        '==': '==',
        '!=': '!=',
        '<=': '<=',
        '>=': '>=',
          
        'IN': ' in ',
          
        'AN': ' and ',
        'NO': ' not ',
        'OR': ' or ',
          
        'TR': 'True',
        'FA': 'False',
        
        'a': 'var_a',
        'b': 'var_b',
        'c': 'var_c',
        'd': 'var_d',
        'e': 'var_e',
        'f': 'var_f',
        'g': 'var_g'}

FORBIDDEN_TOKENS = ['as', 'assert', 'abs', 'aiter', 'all', 'any', 'anext', 'ascii',
                    'break', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes',
                    'class', 'continue', 'callable', 'chr', 'classmethod', 'compile', 'complex',
                    'def', 'del', 'delattr', 'dict', 'dir', 'divmod',
                    'elif', 'else', 'except', 'enumerate', 'eval', 'exec',
                    'False', 'finally', 'for', 'from', 'filter', 'float', 'format', 'frozenset',
                    'global', 'getattr', 'globals',
                    'hasattr', 'hash', 'help', 'hex',
                    'if', 'import', 'is', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter',
                    'lambda', 'len', 'list', 'locals',
                    'map', 'max', 'memoryview', 'min',
                    'None', 'nonlocal', 'not', 'next',
                    'object', 'oct', 'open', 'ord',
                    'pass', 'pow', 'print', 'property',
                    'raise', 'return', 'range', 'repr', 'reversed', 'round',
                    'set', 'setattr', 'sleep', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super',
                    'True', 'try', 'tuple', 'type',
                    'vars',
                    'while', 'with',
                    'yield',
                    'zip']

FORBIDDEN_FUNCTIONS = ['as', 'assert', 'abs', 'aiter', 'all', 'any', 'anext', 'ascii',
                       'break', 'bin', 'breakpoint', 'bytearray', 'bytes',
                       'class', 'continue', 'callable', 'chr', 'classmethod', 'compile', 'complex',
                       'del', 'delattr', 'dict', 'dir', 'divmod',
                       'except', 'enumerate', 'eval', 'exec',
                       'finally', 'from', 'filter', 'format', 'frozenset',
                       'global', 'getattr', 'globals',
                       'hasattr', 'hash', 'help', 'hex',
                       'import', 'is', 'id', 'isinstance', 'issubclass', 'iter',
                       'lambda', 'len', 'list', 'loads', 'locals',
                       'map', 'max', 'memoryview', 'min',
                       'None', 'nonlocal', 'next',
                       'object', 'oct', 'open', 'ord',
                       'pass', 'pow', 'property',
                       'raise', 'repr', 'reversed', 'round',
                       'set', 'setattr', 'sleep', 'slice', 'sorted', 'staticmethod', 'strftime', 'sum', 'super',
                       'try', 'tuple', 'type',
                       'vars',
                       'with',
                       'yield',
                       'zip']


# open script
script_path = input("Put the path to the script that you want to run or compile >> ")

with open(script_path, "r") as script_content:
    code_tokens = script_content.read().split("_")

python_code = []


# scan if the SWOL script has multiple lines
for token in code_tokens:
    if "\n" in token:
        has_multiple_lines = True
        break
    else:
        has_multiple_lines = False

# translate code from SWOL to python
for token in code_tokens:
    python_code.append(TOKENS.get(token))

    if python_code[python_code.index(TOKENS.get(token))] == None:

        for element in FORBIDDEN_TOKENS:
            if element in token:
                has_python_function_or_keyword = True
                break
            else:
                has_python_function_or_keyword = False

        if has_python_function_or_keyword:
            raise SyntaxError(f"Your script contains a python keyword of function at: '{token}'")
        else:
            python_code[python_code.index(TOKENS.get(token))] = token

python_code = "".join(python_code)


# scan if the script contains forbidden functions
for element in FORBIDDEN_FUNCTIONS:
    if element in python_code:
        has_forbidden_functions = True
        break
    else:
        has_forbidden_functions = False


# execute or compile
print(python_code+"\n")

if has_forbidden_functions == False:
    if has_multiple_lines:
        raise EOFError("Script must contain one line")
    else:
        if run_mode == "run":
            exec(python_code)
        elif run_mode == "compile":
            current_date = strftime("%d-%m-%Y-%H-%M-%S")
            with open(f"compiled/{current_date}.py", "x") as compiled_file:
                compiled_file.write(python_code)
        else:
            raise NameError("Mode must be 'run' or 'compile'")
else:
    raise SyntaxError("Final script contains forbidden functions")

sleep(0.5)
print("Program will end in 5 secs")
sleep(5)
