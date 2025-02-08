# Local Imports
from token import Token

# ---------------------------------------------------------------------------------------------------------------- #

class Lexer():

    singleCharTokens = {
                '=' : "TOKEN_EQUALS",
                ';' : "TOKEN_SEMI",
                '(' : "TOKEN_LPAREN",
                ')' : "TOKEN_RPAREN",
                '{' : "TOKEN_LBRACE",
                '}' : "TOKEN_RBRACE",
                ',' : "TOKEN_COMMA",
                '+' : "TOKEN_PLUS",
                '-' : "TOKEN_MINUS",
                '*' : "TOKEN_STAR",
                '/' : "TOKEN_FSLASH",
                '^' : "TOKEN_POWER",
            }

    keywords = [
        "print",
        "int",
    ]

    # ------------------------------------------------------------------------------------------------------------ #

    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.currChar = None
        self.lexerAdvance()
        self.tokens = self.getTokens()

    # ------------------------------------------------------------------------------------------------------------ #

    def lexerAdvance(self):
        self.pos += 1
        self.currChar = self.text[self.pos] if self.pos < len(self.text) else None

    # ------------------------------------------------------------------------------------------------------------ #

    def getTokens(self):
        tokens = []

        while self.currChar != None:

            if self.currChar == ' ':
                self.lexerAdvance()

            elif (self.currChar).isalnum():
                tokens.append(self.getID())

            elif self.currChar == '"' or self.currChar == "'":
                tokens.append(self.getString())

            elif self.currChar in self.singleCharTokens:
                tokens.append(Token(self.singleCharTokens[self.currChar], self.currChar))
                self.lexerAdvance()

        # LEXER TEST PRINT
        for token in tokens:
            print (token.type + ' : ' + token.value)


        return tokens

    # ------------------------------------------------------------------------------------------------------------ #

    def getID(self):
        idValue = ""
        while (self.currChar).isalnum():
            idValue += self.currChar
            self.lexerAdvance()
        idToken = Token("TOKEN_KEYWORD", idValue) if idValue in self.keywords else  Token("TOKEN_ID", idValue)
        return idToken

    # ------------------------------------------------------------------------------------------------------------ #

    def getString(self):
        quoteType = self.currChar
        stringValue = ""
        while self.currChar != quoteType:
            stringValue += self.currChar
            self.lexerAdvance()
        stringValue += self.currChar
        self.lexerAdvance()
        stringToken = Token("TOKEN_STRING", stringValue)
        return stringToken

    # ------------------------------------------------------------------------------------------------------------ #

# ---------------------------------------------------------------------------------------------------------------- #