from pathlib import Path

''' 1. Создание новой директории my_folder '''
home = Path.home()
my_folder = home / "my_folder"

if not my_folder.exists():
    my_folder.mkdir()

''' 2. Добавление файлов в директорию '''
file1 = my_folder / "file1.txt"
file1.touch()
(my_folder / "file2.txt").touch()
my_folder.joinpath("image.png").touch()

''' 3. Создание нового каталога внутри my_folder '''
(my_folder / "images").mkdir(exist_ok=True)

''' 4. Перемещение файла изображения в созданный каталог '''
for f in my_folder.glob('*.png'):
    path_destination = Path(my_folder / "images") / f.name
    f.replace(path_destination)
