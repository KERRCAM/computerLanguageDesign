

from lexer import Lexer




def main():
    filePath = "testFiles/test1.txt"

    with open(filePath, 'r') as file:
        fileContent = (file.read()).replace("\n", '')
    print(fileContent)
    _lexer = Lexer(fileContent)


if __name__ == "__main__":
    main()