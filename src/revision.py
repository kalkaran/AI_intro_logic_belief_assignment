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
        self.belief = belief
        self.sentence = sentence
        self.cnf = convert_to_cnf(sentence.formula())

    def entails(self):
        pass

    def expand(self, expansion_belief):
        parser = Parser(expansion_belief)
        sentence = parser.parse()
        print(f"{expansion_belief} is parsed as:", sentence)
        print(f" Sentence formula : {sentence.formula()}")
        print(f" CNF Form : {convert_to_cnf(sentence.formula())}")
        expansion_cnf = convert_to_cnf(sentence.formula())
        expanded_cnf = self.cnf + " " + expansion_cnf
        print(f" EXPANDED CNF : {expanded_cnf}")
        #self.cnf = expanded_cnf


    def contract(self):
        pass

    def revise(self):
        pass