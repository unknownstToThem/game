import os

def clear_screen():
    temp = None
    
    if os.name == "nt":
        temp = os.system("cls")
    elif os.name == "posix":
        temp = os.system("clear")
    
    del temp
