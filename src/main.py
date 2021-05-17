
from src.logic import Atom, Not, And, Or, Implies, BiConditional, convert_to_cnf
import src.logic as logic
from src.controller import Controller
from src.agent import Agent
import src.parser as P

def main() -> None:
    controller = Controller()
    controller.start_main_loop()

    print("------------------\n")
    controller = Controller()
    controller.startMainLoop()


if __name__ == "__main__":
    main()
