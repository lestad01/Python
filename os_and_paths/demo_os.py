# расширение .py 
# имя файла становится именем модуля
# print(int)
# print(type)
# print(isinstance)
import os

## верхний регистр это константа и не меняем ее в ручную
IS_WINDOWS = "nt" in os.name
BASE_DIR = os.path.dirname(__file__)

def demo_paths():
    print(__file__)  ## определение директории где файл находится
    print("base_dir", BASE_DIR)
    print("is_windows?", IS_WINDOWS)
    print("os path sep:", os.path.sep) ## показывает символ, который используется в ос для разделения компонентов пути
    print("sep on windows: \\" ) ## \ первый слеш это экранирование самого слеша

    print()

    folder_name = "pictures"
    file_name = "cat.jpg"

    print(os.path.sep.join((BASE_DIR, folder_name, file_name)))

    # print(os.name)

def demo_cwd():
    print("base dir:", BASE_DIR)
    # get current working directory рабочая директория
    cwd = os.getcwd()
    print("cwd:", cwd)


def demo_list_dir():
    print(os.listdir("."))

    if os.path.isdir("myvenv"):
        print(os.listdir("myvenv"))

    if os.path.isdir("qwerty"):
        print(os.listdir("qwerty"))

    # if os.path.isfile("demo_os.py"):
    if os.path.isfile(__file__):
        print("this file exists!")

    filename = "file.txt"
    # f = open(filename, "w")
    # f.write("text")
    # f.close()

    # unlink - удалить ссылку / файл
    if os.path.isfile(filename):
        os.unlink(filename) # or os.remove(filename) тоже самое
        print("deleted file", filename)

    print(os.listdir("."))
    # with всегда закрывает файл. Не нужно самим прописывать close
    # 2 аргумент ключ w - открываем файл на запись wright на дополнение ключ a
    with open(filename, "a") as f:
        f.write("hello\n")
        f.writelines(["world\n", "fizz\n", "buzz\n"])
    
    print(os.listdir("."))

    with open(filename) as f:
        print(f.readlines())

def main():
    print("Hello main!")
    # demo_paths()
    # demo_cwd()
    demo_list_dir()

if __name__ == '__main__':
    main()

# модуль OS - нужен чтобы мы могли работать с опер системой
# import добавляет в область видимости в пространство имен
