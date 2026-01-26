FILE_PATH = "file.txt"

def main():
    # f = open(FILE_PATH, "w")
    # print("Hello main!")
    # f = open(FILE_PATH, "w")
    # f.write("hello\n")
    # f.close
    f = open(FILE_PATH, "w")

    with f:
        f.write("hello world\n")
    
    # читаем файл
    # f = open(FILE_PATH, "r")
    # print(f.readlines())
    # f.close

    with open(FILE_PATH, "r") as f:
        print(f.readlines())

    with open(FILE_PATH, "a") as f:
        f.write("hello again\n")
        f.writelines(["cats\n", "dogs\n"])
    
    with open(FILE_PATH, "r") as f:
        for line in f:
            print(line, end="")
    print()

    
if __name__ == '__main__':
    main()