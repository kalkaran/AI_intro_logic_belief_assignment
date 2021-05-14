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



    def resolve(c1, c2):
        c1_copy = Clause.copy(c1)
        c2_copy = Clause.copy(c2)

        # find and remove all complements
        for c1_symbol in c1_copy.positives:
            for c2_symbol in c2_copy.negatives:
                # if the symbols match, remove the symbols from c1 and c2
                if c1_symbol == c2_symbol and c1_symbol in c1_copy.positives:
                    c1_copy.del_positive_symbol(c1_symbol)
                    c2_copy.del_negative_symbol(c2_symbol)
        for c2_symbol in c2_copy.positives:
            for c1_symbol in c1_copy.negatives:
                # if the symbols match, remove the symbols from c1 and c2
                if c2_symbol == c1_symbol and c2_symbol in c2_copy.positives:
                    c1_copy.del_negative_symbol(c1_symbol)
                    c2_copy.del_positive_symbol(c2_symbol)

        # remove redundant symbols
        for c1_symbol in c1_copy.positives:
            for c2_symbol in c2_copy.positives:
                # if the symbols match, remove the symbol from c2
                if c1_symbol == c2_symbol and c1_symbol in c1_copy.positives:
                    c2_copy.del_positive_symbol(c2_symbol)
        for c1_symbol in c1_copy.negatives:
            for c2_symbol in c2_copy.negatives:
                # if the symbols match, remove the symbol from c2
                if c1_symbol == c2_symbol and c1_symbol in c1_copy.negatives:
                    c2_copy.del_negative_symbol(c2_symbol)

        resolvent = Clause.combine_clauses(c1_copy, c2_copy)

        # return the resolvent
        return resolvent


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