from src.logic import *
from src.parser import Parser


class revisor:
    """
    initialize with a belief, and it will parse it ready expansion/contraction.
    """
    def __init__(self, belief):
        parser = Parser(belief)
        sentence = parser.parse()
        print(f"{belief} is parsed as:", sentence)
        print(f" Sentence formula : {sentence.formula()}")
        print(f" CNF Form : {convert_to_cnf(sentence.formula())}")
        pass

    def entails(self):
        pass

    def expand(self, expansion_belief):
        parser = Parser(expansion_belief)
        sentence = parser.parse()
        print(f"{expansion_belief} is parsed as:", sentence)
        print(f" Sentence formula : {sentence.formula()}")
        print(f" CNF Form : {convert_to_cnf(sentence.formula())}")



