from src.parser import Parser
from src.logic import Atom, Not, And, Or, Implies, BiConditional, convert_to_cnf, split_cnf_into_list_clauses
from src.controller import Controller

def main() -> None:
    controller = Controller()
    #controller.start_main_loop()

    p = Atom("P")
    q = Atom("Q")
    r = Atom("R")
    # model = {"B": False, "A": True, "C": True}  # , "A" : True}
    # parser = Parser('(A <=> B) => (B <=> A) & A | B & ~C')
    sentence = Implies(And(Not(p), q), And(p, Implies(r, q)))
    sentence = And(And(p, And(p, p)),p)
    #sentence = And(p, q)
    print(f"Before: {sentence}")
    print(f"After: {convert_to_cnf(sentence)}")
    split_cnf_into_list_clauses(sentence)

    # print(sentence.evaluate(model))

    # print("------------------\n")
    # controller = Controller()
    # controller.startMainLoop()


if __name__ == "__main__":
    main()
