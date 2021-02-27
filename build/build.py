import os


CURR_PATH = os.path.dirname(os.path.abspath(__file__))

target_path = os.path.join(CURR_PATH, "..", "src")
os.chdir(target_path)

cmd = "pyinstaller -F app.py"
os.system(cmd)

os.chdir(CURR_PATH)