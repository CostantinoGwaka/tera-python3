from pathlib import Path


print(Path(r"/usr/local/bin/python3").exists())  # True
Path(r"/usr/local/bin/python3").is_file()  # True
Path(r"/usr/local/bin/python3").is_dir()  # False

print(Path.home())  # /home/username
print(Path.cwd())  # /current/working/directory
print(Path.name)  #
print(Path.stem)
print(Path.suffix)
print(Path.parent)
# print(Path.with_name("/Users/costantinogwaka"))
print(Path.absolute())
print(Path.with_suffix(".txt"))
