

from lexer import Lexer




def main():
    filePath = "TestFiles/test1.txt"

    with open(filePath, 'r') as file:
        fileContent = (file.read()).replace("\n", '')
    
    _lexer = Lexer(fileContent)


if __name__ == "__main__":
    main()