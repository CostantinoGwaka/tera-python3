from pathlib import Path
from time import ctime

path = Path("helloworld/list.py")
# path.exists()  # True
# path.rename("helloworld/new_list.py")
print(ctime(path.stat().st_mtime))  # list.py


with open("helloworld/list.py", "r") as file:
    print(file.read())

# print(path.read_text())
