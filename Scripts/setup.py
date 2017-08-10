from cx_Freeze import setup, Executable

import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\Arvind\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Arvind\\Anaconda3\\tcl\\tk8.6"

base = None


executables = [Executable("Crawler.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Crawler",
    options = options,
    version = "1",
    description = '<any description>',
    executables = [Executable("Crawler.py")]
)