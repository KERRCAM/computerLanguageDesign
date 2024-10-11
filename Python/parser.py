# Local Imports
from ast import AST

# ---------------------------------------------------------------------------------------------------------------- #

class parser():
    
    # ------------------------------------------------------------------------------------------------------------ #
    
    def __init__(self, tokens):
        self.currToken = None
        self.tokens = tokens
        self.tokenPos = -1 
        self.tokenAdvance()
        
    # ------------------------------------------------------------------------------------------------------------ #
    
    def tokenAdvance(self):
        self.tokenPos += 1
        self.currToken = self.tokens[self.tokenPos] if self.tokenPos < len(self.tokens) else None
        
    # ------------------------------------------------------------------------------------------------------------ #
    
# ---------------------------------------------------------------------------------------------------------------- #