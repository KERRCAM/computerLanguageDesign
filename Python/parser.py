# Local Imports
from ast import AST, AST_Node

# ---------------------------------------------------------------------------------------------------------------- #

class Parser():

    # ------------------------------------------------------------------------------------------------------------ #

    def __init__(self, tokens):
        self.currToken = None
        self.tokens = tokens
        self.tokenPos = -1
        self.tokenAdvance()
        self.consumeTokens()

    # ------------------------------------------------------------------------------------------------------------ #

    def tokenAdvance(self):
        self.tokenPos += 1
        self.currToken = self.tokens[self.tokenPos] if self.tokenPos < len(self.tokens) else None

    # ------------------------------------------------------------------------------------------------------------ #

    def consumeTokens(self):
        if self.currToken.type == "TOKEN_KEYWORD":
            self.consumeDefinition()

        elif self.currToken.type == "TOKEN_ID":
            self.consumeExpression()

        else:
            print ("ERROR -> INVALID SYNTAX\nNo recognised definition or expression")

    # ------------------------------------------------------------------------------------------------------------ #

    def consumeDefinition(self):
        pass

    # ------------------------------------------------------------------------------------------------------------ #

    def consumeExpression(self):
        pass

    # ------------------------------------------------------------------------------------------------------------ #

    def consumeFunction(self):
        pass

# ---------------------------------------------------------------------------------------------------------------- #