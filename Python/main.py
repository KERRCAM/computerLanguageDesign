# Local Imports
from lexer import Lexer
from parser import Parser

# ---------------------------------------------------------------------------------------------------------------- #

def main():
    filePath = "testFiles/test1.txt"

    with open(filePath, 'r') as file:
        fileContent = (file.read()).replace("\n", '')
    #print(fileContent)

    lexer = Lexer(fileContent)
    parser = Parser(lexer.tokens)

# ---------------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------------------------- #