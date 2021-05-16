
from src.logic import Atom, Not, And, Or, Implies, BiConditional, convert_to_cnf
import src.logic as logic
# from src.controller import Controller
from src.agent import Agent
import src.parser as P

def main() -> None:
    controller = Controller()
    controller.start_main_loop()

    p = Atom("P")
    q = Atom("Q")
    r = Atom("R")
    # model = {"B": False, "A": True, "C": True}  # , "A" : True}
    # parser = Parser('(A <=> B) => (B <=> A) & A | B & ~C')
    sentence = Implies(And(Not(p), q), And(p, Implies(r, q)))
    # sentence = And(And(p, And(p, p)), p)
    # query = And(p, q)
    # print(f"Before CNF: {sentence}")
    # cnf_sentence = convert_to_cnf(sentence)
    # print(f"After CNF conversion: {cnf_sentence}")
    #
    # cnf_split = logic.collect_conjuncts(cnf_sentence)
    #
    # print(f"Split cnf sentence in list: {cnf_split}")
    #
    # print(f"Atoms: {logic.collect_atoms(cnf_sentence)}")
    #
    # print("Model check", logic.model_checking(cnf_sentence, query))

    agent = Agent()
    agent.declare_new_belief_base("P & P")
    agent.print_belief_base()

    agent.add_new_belief_to_belief_base("(~(P) & Q))")
    agent.print_belief_base()

    # agent.check_satisfiability_of_sentence("P & R")
    # agent.print_belief_base()

    # print(sentence.evaluate(model))

    # print("------------------\n")
    # controller = Controller()
    # controller.startMainLoop()


if __name__ == "__main__":
    main()
