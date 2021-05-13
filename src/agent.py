
class Agent:
    """
        Uses for indicating if a belief base has been declared or not.
    """
    defined_belief_base = False

    """
    The belief set is propositional logic in symbolic form,
    which is converted into CNF form and saved as a list of clauses. 
    Given (P => Q & Z) converted to CNF (~P | Q & Z) into list of clauses [~P | Q, Z]       
    """
    belief_base = []

    def print_belief_base(self):
        for belief in self.belief_base:
            print(belief)

    def declare_new_belief_base(self, input:str):
        # Todo: Add method for parsing new belief base

        """
        Takes a string input containing propositional logic in symbolic form,
        parses it as an abstract syntax tree, which in than converted to CNF form.

        The CNF is divided into a set of clauses and saved as the belief base.

        The syntax is valid if
        - The syntax does not contain any errors when parsed
        - The the belief base is satisfiable: Contain a model for which a
          combination of values makes it true.

        If the syntax is valid the belief base is set, the boolean value defined_belief_base
        is change to true and returned. If not defined_belief_base is than returned and nothing happens.
        """

        # Implement code here.
        print("Declare new belief base")



    def add_new_belief_to_belief_base(self):
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


















