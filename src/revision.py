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
        print(f" CNF Form : {convert_to_cnf(sentence)}")
        self.belief = belief
        self.sentence = sentence
        self.cnf = convert_to_cnf(sentence)


    #TODO test negative normal form.
    #TODO merge sentences - append sentences.
    def entails(self, sentence):
        """
        :param sentence:
        :return:
        """
        negated_sentence = negative_normal_form(sentence)
        #this sentence needs to be added.
        sum_sentence = negated_sentence + sentence
        #written as a list form.

        #Loop to check if things  - if it was list.
        for index1, atom1 in enumerate(sum_sentence):
            for index2, atom2 in enumerate(sum_sentence):
                # check if it's opposite.
                # Does not not resolve to positive.
                if atom1 == Not(atom2):
                    del sum_sentence[index1]
                    del sum_sentence[index1]

        if len(sum_sentence) == 0:
            return True
        else:
            return False


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