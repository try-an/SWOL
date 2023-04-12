from SwolModule import SWOL

print("SWOL by Tryan09")

swol = SWOL()
running = True

while running:
    swol_code = input("Write some code to execute (type 'QUIT' to leave the repl) >> ")

    if swol_code == "QUIT":
        running = False
    else:
        # try-except block has to do with the compilation of the SWOL code
        try:
            code_to_execute = swol.compile_to_py(swol_code)
        except SyntaxError as syntax:
            print(syntax)
            continue
        except EOFError as eof:
            print(eof)
            continue
        # other try-exept has to do with the execution of the pyhon code
        try:
            exec(code_to_execute)
        except Exception as e:
            print(code_to_execute)
            print(e)
