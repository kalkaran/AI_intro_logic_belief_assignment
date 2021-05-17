from src.utils import *
from src.agent import *


class Controller:
    """
    The controller class handles the flow of the program
    - It creates the agent: The agent class contains methods for creating and revising the belief base
    - It contains methods for displaying general information and valid syntax examples.
    - It contains method for creating a new belief base, adding new belief to the belief base
      and checking for entailment of a belief in the belief base.
    """

    def __init__(self):
        self.agent = Agent()

    def start_main_loop(self):
        while True:
            self.print_valid_actions()
            self.preform_action(int(input("Select actions: ")))

    def print_general_information(self):
        """
        Displays the general information needed for running the program.

        Calls a print_general_information method in display_utils class, which prints the general
        information needed for running the program
        """
        display_utils.print_general_information()

    def print_syntax_information(self):
        """
        Displays the syntax information needed for running the program.

        Calls a print_syntax_information method in display_utils class, which prints the syntax
        information needed for running the program.
        """
        display_utils.print_syntax_information()

    def print_current_belief_base(self):
        """
        Display the current belief base.

        Calls a print_belief_base in agent class which prints the belief base
        """
        self.agent.print_belief_base()

    def declare_new_belief_base(self):
        """
        Contains functionality which makes the the user able to declare a new belief base.

        Step 1: The user inputs a sentence containing propositional logic in symbolic form
        Step 2: The syntax of the sentence is validated.
        Step 3: The satisfiability of the sentence is validated.
        Step 4: A new belief base is declared.

        If step 2 and 3 returns false a new belief base isn´t declared and the user must try again.
        """
        # Step 1
        sentence = input("Belief base: ")

        # Step 2
        if not validator.syntax_is_valid(sentence):
            display_utils.print_invalid_input_information()
            return

        # Step 3
        if not self.agent.check_satisfiability_of_sentence(sentence):
            display_utils.print_unsatisfiability_information()
            return

        # Step 4
        self.agent.declare_new_belief_base(sentence)
        display_utils.print_successful_declaration_of_belief_base()

    def use_predefined_belief_base(self):
        """
        Contains functionality which makes the the user able to use a predefined belief base

        Calls a use_predefined_belief_base method in agent class.
        The belief base is set as predefined list of beliefs in CNF form.
        """
        self.agent.use_predefined_belief_base()
        display_utils.print_successful_declaration_of_belief_base()

    def add_new_belief(self):
        """
        Contains functionality which makes the the user able to add a new belief to the belief base.

        Step 1: Checks if agent has a defined belief base.
        Step 2: The user inputs a sentence containing propositional logic in symbolic form
        Step 3: The syntax of the sentence is validated.
        Step 4: The satisfiability of the sentence is validated.
        Step 5: A new belief base is declared.

        If step 1, 2 and 3 returns false a new belief isn´t added to the belief base and the user must try again.
        """
        # Step 1
        if self.agent.defined_belief_base:
            display_utils.print_belief_base_not_defined()
            return

        # Step 2
        sentence = input("Belief: ")

        # Step 3
        if not validator.syntax_is_valid(sentence):
            display_utils.print_invalid_input_information()
            return

        # Step 4
        if not self.agent.check_satisfiability_of_sentence(sentence):
            display_utils.print_unsatisfiability_information()
            return

        # Step 5
        self.agent.add_new_belief_to_belief_base(sentence)
        display_utils.print_successful_addition_of_belief()

    def check_if_belief_is_entail_to_belief_base(self):
        """
        Contains functionality which makes the the user able to check the entailment of a belief in the belief base.

        Step 1: Checks if agent has a defined belief base.
        Step 2: The user inputs a sentence containing propositional logic in symbolic form
        Step 3: The syntax of the sentence is validated.
        Step 4: The satisfiability of the sentence is validated.
        Step 5: Checks the entailment of a belief in the belief base.

        If step 1, 2 and 3 returns false the entailment of the belief isn´t check and the user must try again.
        """
        # Step 1
        if self.agent.defined_belief_base:
            display_utils.print_belief_base_not_defined()
            return

        # Step 2
        sentence = input("Belief: ")

        # Step 3
        if not validator.syntax_is_valid(sentence):
            display_utils.print_invalid_input_information()
            return

        # Step 4
        if not self.agent.check_satisfiability_of_sentence(sentence):
            display_utils.print_unsatisfiability_information()
            return

        # Step 5
        if self.agent.check_if_belief_is_entailed_by_belief_base(sentence):
            display_utils.print_entailment_valid()
        else:
            display_utils.print_entailment_invalid()

    def print_valid_actions(self):
        print("\n--- List of actions ---")
        print("1: Print general information")
        print("2: Print syntax information")
        print("3: Print belief base")
        print("4: Declare new belief base")
        print("5: Use predefined belief base")
        print("6: Add new belief to belief base")
        print("7: Check if belief is entailed by the belief base")

    def preform_action(self, i):
        print("\n--- Actions information ---\n")
        switcher = {
            1: self.print_general_information,
            2: self.print_syntax_information,
            3: self.print_current_belief_base,
            4: self.declare_new_belief_base,
            5: self.use_predefined_belief_base,
            6: self.add_new_belief,
            7: self.check_if_belief_is_entail_to_belief_base,
        }
        switcher.get(i, lambda: print("Invalid input"))()
