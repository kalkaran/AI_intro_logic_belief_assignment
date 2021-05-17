from src.parser import Parser
from src.logic import *


class Agent:
    """
    Some of the code is this class can be refactored if we want to...
    as some of the steps are repeated in the methods.
    But for clarity its keep divided.

    Also it a bit redunted to parses the same string multiple times when preforming the different check.
    - The string could just be parses ones and than parsed around as an ast/Sentence.
    - It done this way in hope of reducing the links between the different methods.

    The Agent class contains methods for interaction with the belief base.
    - Create a new belief base
    - Adding a new belief to the belief base
    - Checking for satisfiability
    - Checking for entailment
    """

    """
        Uses for indicating if a belief base has been declared or not.
    """
    defined_belief_base = False

    """
    The belief base is propositional logic in symbolic form,
    which is converted into CNF form and saved as a list of clauses. 
    Given (P => Q & Z) converted to CNF (~P | Q & Z) and then into a list of clauses [~P | Q, Z]       
    """
    belief_base = BeliefBase()

    def print_belief_base(self):
        """
            Prints the current belief base.
        """
        print(f"Before: {self.belief_base}")

    def declare_new_belief_base(self, sentence: str):
        # Todo: Add method for declaring new belief base

        """
        Contains functionality for declaring a new belief base.

        Parameters:
            sentence (str): Takes a string input containing propositional logic in symbolic form.

        Step 1: The sentence is parsed and an abstract syntax tree is created.
        Step 2: The abstract syntax tree is converted to CNF
        Step 3: The abstract syntax tree containing the sentence is divided into a list of beliefs
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
        list_of_clauses = collect_conjuncts(CNF)
        print(f"List: {list_of_clauses}")

        # Step 4: Redundant beliefs in the list are removed.
        list_of_clauses_filtered = remove_redundant_beliefs(list_of_clauses)
        print(f"Filtered List: {list_of_clauses_filtered}")

        # Step 5: The belief base is declared and defined_belief_base is change to true.
        self.belief_base.add_belief(list_of_clauses_filtered)
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
        Step 5: The temp belief base where the negated sentence was added is check
                for logical entailment with the resolution method.
        Step 6: A revision of the belief base is preformed, if its required.
        Step 7: The belief base is updated in the agent.

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

        # Step 4: The negated sentence is added to a copy of the belief base
        # temp_belief_base = adds_sentence_to_belief_base(negation, self.belief_base)
        self.belief_base.add_belief(negation)
        print(f"Temp belief base: {self.belief_base}")

        # Step 5: Check for logical entailment of added belief with resolution.
        # action = check_for_entailment(temp_belief_base)

        # Step 6: Preform a revision of the belief base, if its required.
        revised_belief_base = revise_belief_base(action, self.belief_base, sentence)

        # Step 7: Update the belief base in the agent.
        self.belief_base = revised_belief_base

    def check_satisfiability_of_sentence(self, sentence: str):
        """
        Contains functionality for checking the satisfiability of a sentence

        Parameters:
            sentence (str): Takes a string input containing propositional logic in symbolic form.

        #Returns:
            valid(boolean): Returns true is the sentence is satisfiable

        Step 1: The sentence is parsed and an abstract syntax tree is created.
        Step 2: The abstract syntax tree is converted to CNF
        Step 3: The abstract syntax tree containing the sentence is divided into a list of beliefs
        Step 4: Redundant beliefs in the list are removed.
        Step 5: All atoms in the list of belief are found
        Step 6: All possible models is created based on the atoms in the belief list
        Step 7: The list of beliefs is evaluated based on all possible models.
        Step 8: If there exit a model for which the sentence is true, True is returned otherwise false.

        """

        # Step 1: The sentence is parsed and an abstract syntax tree is created.
        sentence = Parser(sentence).parse()
        print(f"Before: {sentence}")

        # Step 2: The abstract syntax tree is converted to CNF
        CNF = convert_to_cnf(sentence)
        print(f"After: {CNF}")

        # Step 3: The abstract syntax containing the sentence is divided into a list beliefs
        list_of_beliefs = collect_conjuncts(CNF)
        print(f"Negated: {list_of_beliefs}")

        # Step 4: Redundant beliefs in the list are removed.
        list_of_beliefs_filtered = remove_redundant_beliefs(list_of_beliefs)
        print(f"Filtered List: {list_of_beliefs_filtered}")

        # Step 5: All atoms in the list of belief are found.
        list_of_atoms = find_all_atoms_in_belief_base(list_of_beliefs_filtered)

        # Step 6: All possible models is created based on the atoms in the belief list
        list_of_models = collect_atoms(CNF)

        # Step 7 The list of beliefs is evaluated based on all possible models.
        exits_valid_combination_in_belief_base = model_checking(list_of_beliefs_filtered, list_of_models)

        # Step 8: If there exit a model for which the sentence is true, True is returned otherwise false.
        if exits_valid_combination_in_belief_base:
            return True
        else:
            return False


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

    def check_if_belief_is_entailed_by_belief_base(self, sentence: str):

        # Todo: Add method for checking if a belief is entailed by the belief_base

        """
        Contains functionality for checking if a belief is entailed by the belief_base

        Parameters:
            sentence (str): Takes a string input containing propositional logic in symbolic form.

        Step 1: The sentence is parsed and an abstract syntax tree is created.
        Step 2: The abstract syntax tree is converted to CNF
        Step 3: The sentence in the abstract syntax tree is negated
        Step 4: The negated sentence is added to a copy of the belief base
        Step 5: The temp belief base where the negated sentence was added is check
                for logical entailment with the resolution method.
        Step 6: Base on the type of action return for the logical entailment check True or False is returned.

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

        # Step 4: The negated sentence is added to a copy of the belief base
        temp_belief_base = adds_sentence_to_belief_base(negation, self.belief_base)
        print(f"Temp belief base: {temp_belief_base}")

        # Step 5: Check for logical entailment of added belief with resolution.
        action = check_for_entailment(temp_belief_base)

        # Step 6: Preform a revision of the belief base, if its required.
        if action is Action.revision:
            return True
        else:
            return False

































