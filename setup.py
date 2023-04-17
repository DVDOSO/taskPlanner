from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Task Planner Beta Release.py", base=base)]

packages = ["idna", "tkinter", "sqlite3"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<Task Planner>",
    options = options,
    version = "<1.1>",
    description = '<Task Planner>',
    executables = executables
)
