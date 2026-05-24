from pathlib import Path
from sys import argv

dir_name = argv[1]

target_dir = Path.cwd() / dir_name
target_dir.mkdir(exist_ok=True)

for txt_file in Path.cwd().glob('*.txt'):
    destination = target_dir / txt_file.name
    txt_file.replace(destination)
