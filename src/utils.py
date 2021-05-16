from logic import *
from parser import Parser

example0 = '~(A & B) | ((C & D))'
example0 = '~(A & B) | ((C & D) | E)'  # <- this doesn't work @Ayman looks like only 4 letters allowed :/
example0 = '~(A & B) | ((C & D) | A)'
example1 = 'A & ~(B)'
example2 = '~(A)'
example3 = 'A & A & A'
example4 = 'A => B'
example5 = 'A <=> B'
example6 = '(A <=> B) => (B <=> A) & A | B'

examples = [example0
    , example1
    , example2
    , example3
    , example4
    , example5
    , example6]


def printValidSyntax():
    for example in examples:
        # sentence = "(~(P) => (P | R))"
        # parser = Parser(sentence)
        parser = Parser(example)
        sentence = parser.parse()

        print(f"{example} is parsed as:", sentence)
        print(f" Sentence formula : {sentence.formula()}")
        print(f" CNF Form : {convert_to_cnf(sentence.formula())}")

        # print(sentence.evaluate(model))


printValidSyntax()

"""
    p = Atom("P")
    q = Atom("A")
    r = Atom("R")
    model = {"B" : False, "A" : True, "C" : True  } # , "A" : True}
    parser = Parser('(A <=> B) => (B <=> A) & A | B & ~C')
    sentence = parser.parse() # Implies(Not(p), Or(q, r))
    # sentence = "(~(P) -> (P | R))"
    print(sentence.formula())
    print(convert_to_cnf(sentence.formula()))
    print(sentence.evaluate(model))
    """

class validator:

    @staticmethod
    def syntax_is_valid(sentence:str):
        # Todo: Add method for checking if a user input is valid syntax
        """
        Check if a user input containing propositional logic in symbolic form is valid or not
        based on the syntax used in the program.

        Parameters:
            sentence (str): A string containing propositional logic in symbolic form.

        Returns:
            boolean: True/False
            - If the input is valid base on the syntax used in the program true is returned otherwise false.
        """
        return True



class display_utils:

    @staticmethod
    def print_entailment_valid():
        # Todo: Add method for displaying if a belief is entailed by the belief base
        """
        Displays if a belief is entailed by the belief base
        """
        print("The belief is entailed by the belief base")

    @staticmethod
    def print_entailment_invalid():
        # Todo: Add method for displaying if a belief is not entailed by the belief base
        """
        Displays if a belief is entailed not by the belief base
        """
        print("The belief is not entailed by the belief base")

    @staticmethod
    def print_general_information():
        # Todo: Add method for general information display
        """
        Displays the general information needed for running the program
        """
        print("Displays general information")

    @staticmethod
    def print_syntax_information():
        # Todo: Add method for syntax display
        """
        Displays the syntax information needed for running the program
        """
        print("Displays syntax accepted as an input")

    @staticmethod
    def print_invalid_input_information():
        """
        Displays a message for the result of an invalid input
        """
        print("The current input isn´t valid syntax")

    @staticmethod
    def print_valid_input_information():
        # Todo: Add method for syntax display
        """
        Display a message for the result of a valid input
        """
        print("The current input is valid syntax and was accepted")

    @staticmethod
    def print_belief_base_not_defined():
        # Todo: Add method for display of undefined belief base in the agent.
        """
        Display a message used if the agent has an undefined belief base
        """
        print("The agent does not contain a belief base")

    @staticmethod
    def print_successful_declaration_of_belief_base():
        # Todo: Add method for successful declaration of belief base
        """
        Display a message used if the agent has a defined belief base
        """
        print("A belief base has been declared")

    @staticmethod
    def print_successful_addition_of_belief():
        # Todo: Add method for successful addition of belief to belief base
        """
        Display a message for a successful declaration of belief base
        """
        print("The belief was successful added to the belief base")

    @staticmethod
    def print_unsatisfiability_information():
        # Todo: Add method for displaying if an input sentence is unsatisfiability
        """
        Display a message if an input sentence is unsatisfiability
        """
        print("The input is unsatisfiability and can´t be accepted ")
