# by Tryan09
# -------------------
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

class SWOL:
    """# SWOL compiler

        -----

        ## Description:

            SWOL is an esoteric programming language that (in my (the creator's) opinion) is probably the most readable esolang out there

            Everything (functions, strings etc..) is seperated by underscores

            However, everything is written in only one line. Yes, ONE. LINE.

        ## How to use it:

            1 - Create an instance of the SWOL class: eg. `swol = SwolModule.SWOL()`

            2 - Write a script: eg. `hello_world = 'P_(_"Hello World"_)'`

            3 - Call the function `swol.compile_to_py(hello_world)`

                (Please note that just calling the function like this `swol.compile_to_py(hello_world)` will not do anything notable,
                
                so store it in a variable or use the `exec()` or `eval()` function)"""
    
    def __init__(self):
        self.TOKENS = {';': '\n',
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

        self.FORBIDDEN_TOKENS = ['as', 'assert', 'abs', 'aiter', 'all', 'any', 'anext', 'ascii',
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

        self.FORBIDDEN_FUNCTIONS = ['as', 'assert', 'abs', 'aiter', 'all', 'any', 'anext', 'ascii',
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

    def compile_to_py(self, SWOL_script: str):
        code_tokens = SWOL_script.split("_")

        has_multiple_lines = self.__code_has_multiple_lines(code_tokens)
        if has_multiple_lines:
            raise EOFError("Script must contain one line")

        python_code = self.__translate_to_python(code_tokens)

        has_forbidden_functions = self.__code_has_forbidden_functions(python_code)
        if has_forbidden_functions:
            raise SyntaxError("Final script contains forbidden functions")

        return python_code

    def __code_has_multiple_lines(self, tokens: list):
        for token in tokens:
            if "\n" in token:
                return True
            else:
                continue
        return False
    
    def __code_has_forbidden_functions(self, python_code):
        for element in self.FORBIDDEN_FUNCTIONS:
            if element in python_code:
                return True
            else:
                continue
        return False

    def __code_has_python_func_or_keyword(self, token):
        for element in self.FORBIDDEN_TOKENS:
            if element in token:
                return True
            else:
                continue
        return False

    def __translate_to_python(self, tokens: list[str]):
        translated_code = []
        for token in tokens:

            direct_translation = self.TOKENS.get(token)
            has_python_function_or_keyword = self.__code_has_python_func_or_keyword(token)

            if has_python_function_or_keyword:
                raise SyntaxError(f"Your script contains a python keyword of function at: '{token}'")
            
            if direct_translation is None:
                translated_code.append(token)
            else:
                translated_code.append(direct_translation)

        return "".join(translated_code)

if __name__ == "__main__":
    __swol = SWOL()

    __hello_world = __swol.compile_to_py('P_(_"Hello World"_)')
    __greatest_common_divisor = __swol.compile_to_py('P_(_"GCD"_)_;_a_=_i_(_I_(_"a = "_)_)_;_b_=_i_(_I_(_"b = "_)_)_;_W_b_!=_0_:_;_}_IF_a_>_b_:_;_}_}_a_=_a_-_b_;_}_ELS_:_;_}_}_b_=_b_-_a_;_P_(_a_)_;')

    print(f"{__hello_world}\n\n{__greatest_common_divisor}")
