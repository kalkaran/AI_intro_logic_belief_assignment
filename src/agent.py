from src.parser import Parser
from src.logic import *


class Agent:
    """
        Uses for indicating if a belief base has been declared or not.
    """
    defined_belief_base = False

    """
    The belief base is propositional logic in symbolic form,
    which is converted into CNF form and saved as a list of clauses. 
    Given (P => Q & Z) converted to CNF (~P | Q & Z) into list of clauses [~P | Q, Z]       
    """
    belief_base = []

    def print_belief_base(self):
        """
            Prints the current belief base.
        """
        print(f"Before: {self.belief_base}")

    def declare_new_belief_base(self, sentence: str):
        # Todo: Add method for parsing new belief base

        """
        Contains functionality for declaring a new belief base.

        Parameters:
            sentence (str): Takes a string input containing propositional logic in symbolic form.

        Step 1: The sentence is parsed and an abstract syntax tree is created.
        Step 2: The abstract syntax tree is converted to CNF
        Step 3: The abstract syntax tree containing the sentence is divided into a list beliefs
        Step 4: Redundant beliefs in the list are removed.
        Step 5: The belief base is declared and defined_belief_base is change to true.
        """

        # Step 1: The sentence is parsed and an abstract syntax tree is created.
        sentence = Parser(sentence).parse()
        print(f"Before: {sentence}")

        # Step 2: The abstract syntax tree is converted to CNF
        CNF = convert_to_cnf(sentence)
        print(f"After: {CNF}")

        # Step 3: The abstract syntax containing the sentence is divided into a list beliefs
        list_of_clauses = split_sentence_into_list_of_beliefs(CNF)
        print(f"List: {list_of_clauses}")

        # Step 4: Redundant beliefs in the list are removed.
        list_of_clauses_filtered = remove_redundant_beliefs(list_of_clauses)
        print(f"Filtered List: {list_of_clauses_filtered}")

        # Step 5: The belief base is declared and defined_belief_base is change to true.
        self.belief_base = list_of_clauses_filtered
        self.defined_belief_base = True

    def add_new_belief_to_belief_base(self, sentence: str):
        # Todo: Add method for adding new belief to belief base

        """
        Contains functionality for adding a new belief to the belief base.

        Parameters:
            sentence (str): Takes a string input containing propositional logic in symbolic form.

        Step 1: The sentence is parsed and an abstract syntax tree is created.
        Step 2: The abstract syntax tree is converted to CNF
        Step 3: The sentence in the abstract syntax tree is negated
        Step 4: The negated sentence is added to a copy of the belief base
        Step 5: Check for logical entailment of added belief with resolution.
        Step 6: Preform a revision of the belief base, if its required.
        Step 7: Update the belief base in the agent.

        """

        # Step 1: The sentence is parsed and an abstract syntax tree is created.
        sentence = Parser(sentence).parse()
        print(f"Before: {sentence}")

        # Step 2: The abstract syntax tree is converted to CNF
        CNF = convert_to_cnf(sentence)
        print(f"After: {CNF}")

        # Step 3: The sentence in the abstract syntax tree is negated
        negation = negate_sentence(CNF)
        print(f"Negated: {negation}")

        # Step 4: Redundant beliefs in the list are removed.
        temp_belief_base = adds_sentence_to_belief_base(negation, self.belief_base)
        print(f"Filtered List: {temp_belief_base}")





    def check_satisfiability_of_sentence(self, sentence: str):

        """
        Contains functionality for checking the satisfiability of a sentence

        Parameters:
            sentence (str): Takes a string input containing propositional logic in symbolic form.

        #Returns:
            valid(boolean): Returns true is the sentence is satisfiable

        Step 1: The sentence is parsed and an abstract syntax tree is created.
        Step 2: The abstract syntax tree is converted to CNF
        Step 3: The abstract syntax tree containing the sentence is divided into a list beliefs
        Step 4: Redundant beliefs in the list are removed.
        Step 5: All atoms in the list of belief is found
        Step 6: The list of beliefs is evaluated based on all possible models.
        Step 7: If there exit a model of which the sentence is true, True is returned otherwise false.

        """

        # Step 1: The sentence is parsed and an abstract syntax tree is created.
        sentence = Parser(sentence).parse()
        print(f"Before: {sentence}")

        # Step 2: The abstract syntax tree is converted to CNF
        CNF = convert_to_cnf(sentence)
        print(f"After: {CNF}")

        # Step 3: The abstract syntax containing the sentence is divided into a list beliefs
        list_of_beliefs = split_sentence_into_list_of_beliefs(CNF)
        print(f"Negated: {list_of_beliefs}")

        # Step 4: Redundant beliefs in the list are removed.
        list_of_clauses_filtered = remove_redundant_beliefs(CNF)
        print(f"Filtered List: {list_of_clauses_filtered}")

        # Step 5: The belief base is declared and defined_belief_base is change to true.
        self.belief_base = list_of_clauses_filtered
        self.defined_belief_base = True

    def use_predefined_belief_base(self):
        # Todo: Add method for using predefined belief base

        """
        A predefined list of belief is declared as the belief base.
        The predefined list of belief is propositional logic in symbolic form,
        which is converted to CNF form and saved as list of clauses as the belief base.

        The boolean value defined_belief_base is change to true and returned.
        """

        # Implement code here.
        print("Belief base with predefined beliefs")

    def check_if_belief_is_entail_by_belief_base(self, input: str):
        # Implement code here.
        print("Checks is belief is entail by belief_base")
