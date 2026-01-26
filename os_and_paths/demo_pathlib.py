# import pathlib
from pathlib import Path

# pathlib.Path


def demo_cwd():
    cwd = Path.cwd()
    print("cwd:", cwd)

    print("file:", Path(__file__))
    print("file:", __file__)
    print(str(__file__))
    print(repr(__file__))
    print("file:", repr(Path(__file__)))

    print(list(cwd.iterdir()))
    for path in cwd.iterdir():
        print(path.name, path.is_dir(), path.is_file)



def demo_home():
    print(Path.home())
    home = Path.home()

    for path in home.iterdir():
        print(path.name)


def demo_check_existence():
    users = Path("/Users")
    print(users)
    print("users?", users.exists())

    cats = Path("/Cats")
    print(cats)
    print("casts exists?", cats.exists)
    cats.unlink(missing_ok=True)


def demo_file_path():
    print("__file__", __file__)
    current_file = Path(__file__)
    print(current_file)
    print(repr(current_file))
    base_dir = current_file.parent
    print(base_dir.parents)
    print(repr(base_dir))


def demo_build_path():
    current_file = Path(__file__)
    base_dir = current_file.parent

    folder_name = "pictures"
    file_name = "cats.jpg"

    casts_filepath = base_dir / folder_name / file_name
    print(casts_filepath)
    print(repr(casts_filepath))
    print("exists?", casts_filepath.exists())
    
    cats_pic_filepath = base_dir.joinpath(folder_name, file_name)
    print(cats_pic_filepath)
    print(repr(cats_pic_filepath))
    print("eq?", casts_filepath == cats_pic_filepath)

    print("suffix", casts_filepath.suffix)
    print("name", casts_filepath.name)
    print("stem", casts_filepath.stem)
    print("anchor", casts_filepath.anchor)


def demo_files():
    filename = "file.txt"

    file = Path(filename)
    print(file)
    print(repr(file))

    file = file.resolve()
    print(file)
    print(repr(file))

    file.unlink(missing_ok=True)

    file.write_text("Hello\n") # перезаписывает файл
    print(file.read_text())


def main():
    # demo_cwd()
    # demo_home()
    # demo_check_existence()
    # demo_file_path()
    # emo_build_path()
    demo_files()

    
if __name__ == '__main__':
    main()