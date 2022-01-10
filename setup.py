import cx_Freeze
import sys
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [cx_Freeze.Executable('main.py',base=base, icon='attendance.ico')]

cx_Freeze.setup(
    name='Odoo Attendance Manager',
    options={'build_exe':{'packages':['PySide6','requests','zk'],'include_files':['attendance.ico']}},
    version='1.0.0',
    description='Odoo Attendance Manager \nby butirpadi \nCopyright : 2021',
    executables = executables
)