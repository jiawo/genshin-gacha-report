import os
import shutil

VERSION = "v1.0.1"
CURR_PATH = os.path.dirname(os.path.abspath(__file__))

src_path = os.path.join(CURR_PATH, "..", "src")
temp_path = os.path.join(CURR_PATH, "temp", "src")

if os.path.isdir(temp_path):
    shutil.rmtree(temp_path)

shutil.copytree(src_path, temp_path)

os.chdir(temp_path)

cmd = "pyinstaller -F app.py -n gacha-report-%s.exe" % VERSION
os.system(cmd)

os.chdir(CURR_PATH)
