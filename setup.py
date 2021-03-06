import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = "C:\\Users\\mukes\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\mukes\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("snake_game.py", base=base)]


cx_Freeze.setup(
    name = "snake game",
    options = {"build_exe": {"packages":["turtle","os","random","time"], "include_files":['tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
