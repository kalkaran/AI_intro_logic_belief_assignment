
class Controller:

    def start_main_loop(self):
        while True:
            self.print_valid_actions()
            self.preform_action(int(input("Select actions: ")))

    def print_general_information(self):
        # Todo: Add method for general information display
        print("Displays general information")

    def print_syntax_information(self):
        # Todo: Add method for syntax display
        print("Displays syntax accepted as an input")

    def print_current_belief_base(self):
        # Todo: Add method for belief base display
        print("Displays the current belief base")

    def declare_new_belief_base(self):
        # Todo: Add method for declaring new belief base
        print("Declare new belief base")

    def use_predefined_belief_base(self):
        # Todo: Add method for using predefined belief base
        print("Belief base with predefined beliefs")

    def add_new_belief(self):
        # Todo: Add method for adding new belief to belief base
        print("New Belief added to belief base")

    def check_if_belief_is_entail_to_belief_base(self):
        # Todo: Add method for checking if belief is entail by the belief base
        print("Checking if belief is entail by the belief base")

    def print_valid_actions(self):
        print("\n--- List of actions ---")
        print("1: Print general information")
        print("2: Print syntax information")
        print("3: Print belief base")
        print("4: Declare new belief base")
        print("5: Use predefined belief base")
        print("6: Add new belief to belief base")
        print("7: Check if belief is entail by the belief base")

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
