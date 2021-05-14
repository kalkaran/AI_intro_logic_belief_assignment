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

    def declare_new_belief_base(self, sentence:str):
        # Todo: Add method for parsing new belief base

        """
        Contains functionality for adding a new belief to the belief base.

        Parameters:
            sentence (str): Takes a string input containing propositional logic in symbolic form.

        Step 1: The sentence is parsed and an abstract syntax tree is created.
        Step 2: The abstract syntax tree is converted to CNF
        Step 3: The abstract syntax containing the sentence is divided into a list of clauses of beliefs
        Step 4: Redundant beliefs in the list are removed.
        Step 5: The belief base is declared and defined_belief_base is change to true.
        """

        # Step 1: The sentence is parsed and an abstract syntax tree is created.
        sentence = Parser(sentence).parse()
        print(f"Before: {sentence}")

        # Step 2: The abstract syntax tree is converted to CNF
        CNF = convert_to_cnf(sentence)
        print(f"After: {CNF}")

        # Step 3: The abstract syntax containing the sentence is divided into a list of clauses
        list_of_clauses = split_cnf_into_list_clauses(CNF)
        print(f"List: {list_of_clauses}")

        # Step 4: Redundant beliefs in the list are removed.
        list_of_clauses_filtered = remove_redundant_clauses(CNF)
        print(f"Filtered List: {list_of_clauses_filtered}")

        # Step 5: The belief base is declared and defined_belief_base is change to true.
        self.belief_base = list_of_clauses_filtered
        self.defined_belief_base = True


    def add_new_belief_to_belief_base(self, input:str):
        # Todo: Add method for adding new belief to belief base

        """
        Takes a string input containing propositional logic in symbolic form,
        parses it as an abstract syntax tree, which in than converted to CNF form.

        The syntax is valid if
        - The syntax does not contain any errors when parsed
        - The belief itself must be satisfiable: Contain a model for which a
          combination of values makes it true. A belief containing Not P and P
          isn´t valid.

        If the syntax is valid logical entailment is check with resolution
        - The negation of the belief is added to the belief set
        - If the resolution results in an empty clause, it indicates that
          the belief is entailed by the belief base and Revision must be preformed.
        - If the resolution not results in an empty clause, it indicates that
          the belief is not entailed by the belief base and it can just be added
          to the belief base.


        If the syntax is valid the belief base is set and true is return,
        if false is return and nothing happens.
        """

        # Implement code here.
        print("Added new belief to belief base")

    def check_satisfiability_of_sentence(self, sentence:str):

        # Todo: Add method for checking satisfiability of sentence

        return True





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


    def check_if_belief_is_entail_by_belief_base(self, input:str):

        # Implement code here.
        print("Checks is belief is entail by belief_base")
















