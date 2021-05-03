from src.logic import *
from utils import *
from src.parser import Parser
import functools

class Controller:

    def __init__(self):
        self.model ={"B" : True, "A" : True, "C" : True }
        self.sentence = None
        self.beliefBase = None

    def declareNewBeliefBase(self):
        # Test string (A <=> B) => (B <=> A) & A | B & ~C
        belief_base_input = str(input("Declare new belief base: "))

        # Validate input string
        parser = Parser(belief_base_input)
        self.sentence = parser.parse()
        self.beliefBase = BeliefBase(convert_to_cnf(self.sentence.formula()))

        self.printCurrentBeliefBase()

    def declareRandowBeliefBase(self):
        # Test string (A <=> B) => (B <=> A) & A | B & ~C
        parser = Parser('(A <=> B) => (B <=> A) & A | B & ~C')
        self.sentence = parser.parse()
        self.printCurrentBeliefBase()

    def startMainLoop(self):
        while(True):
            self.printValidActions()
            self.preformAction(int(input("Select actions: ")))

    def addNewBeliefToBeliefBase(self):
        if self.sentence is None:
            print("Current belief base is None.")
        else:
            tempBelief = input()
            print(tempBelief)

            # Implement stuff

    def check_satisfiability(self):
        print(is_satisfiable(self.sentence.formula()))

    def printFormula(self):
        print("\nCurrent belief base: "+str(self.sentence.formula()))

    def printCNF(self):
        print(convert_to_cnf(self.sentence.formula()))


    def printEvaluation(self):
        print(self.sentence.evaluate(self.model))



    def printGeneralInformation(self):
        print("This contain the general information")
        # Declare syntax in print statement.

    def printSyntaxInformation(self):
        print("The following syntax is accepted as an input")
        printValidSyntax()

        # Declare syntax in print statement.

    def printCurrentBeliefBase(self):
        #WIllIAM -  At the current state, I don´t know the correct syntax for the belief base.
        if self.sentence is None:
            print("Current belief base is None.")
        else:
            self.beliefBase.print_belief_base()



    def printValidActions(self):
        print("\n--- List of actions ---")
        print("1: Print general information")
        print("2: Print syntax information")
        print("3: Print belief base")
        print("4: Create new belief base")
        print("5: Add new random belief base")
        print("6: Add new belief to belief base")
        print("7: Check satisfiability of belief base ")


    def preformAction(self, i):
        print("\n--- Actions information ---\n")
        switcher={
                1 : self.printGeneralInformation,
                2 : self.printSyntaxInformation,
                3 : self.printCurrentBeliefBase,
                4 : self.declareNewBeliefBase,
                5 : self.declareRandowBeliefBase,
                6 : self.addNewBeliefToBeliefBase,
                7: self.check_satisfiability,
                }
        switcher.get(i, lambda : print("Invalid input"))()




def main():
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
    print("------------------\n")
    controller = Controller()
    controller.startMainLoop()



if __name__ == "__main__":
    main()
