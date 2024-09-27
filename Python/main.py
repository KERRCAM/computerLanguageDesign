

from lexer import Lexer
import parser
import ast




def main():
    filePath = "testFiles/test1.txt"

    with open(filePath, 'r') as file:
        fileContent = file.read()
    
    _lexer = Lexer(fileContent)


if __name__ == "__main__":
    main()