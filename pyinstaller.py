import os
import shutil

os.system('pyinstaller -F interpolation.py')
shutil.move('dist/interpolation.exe', 'interpolation.exe')
shutil.rmtree('build', ignore_errors=True)
shutil.rmtree('dist', ignore_errors=True)
os.remove('interpolation.spec')
