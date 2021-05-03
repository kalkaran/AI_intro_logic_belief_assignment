from abc import ABC
from sympy.logic.boolalg import Not, And, Or
import sympy
from sympy.logic.boolalg import to_cnf
from sympy.core.symbol import Symbol
from sympy.logic.inference import satisfiable
from typing import Dict

class Sentence(ABC):
    def evaluate(self, model : Dict[str, bool]) -> bool:
        """ evaluates the truth of a sentence with respect to a particular model """
        pass

    def formula(self) -> str:
        """ returns a string representation of a given sentence """
        pass

class BeliefBase():

    beliefs = None

    def __init__(self, CNF:Symbol):
        self.beliefs = CNF

    def print_belief_base(self):
        print(self.beliefs)

    def add_belief(self, belief):

        print("Negation of belief")
        negation_of_belief = Not(belief)
        print(negation_of_belief)
        temp_belief_base = And(self.beliefs, negation_of_belief)
        print("Temp_belief_base")
        print(temp_belief_base)
        satisfiability = satisfiable(temp_belief_base)

        if(satisfiability is not False):
            self.beliefs = And(self.beliefs, belief)
        else:
            print("Not allowed")




class Atom_local(Sentence):
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def evaluate(self, model: Dict[str, bool]) -> bool:
        assert self.name in model, f"The {self.name} is not in model"

        return model.get(self.name)

    def formula(self) -> str:
        return self.name


class Not_local(Sentence):
    def __init__(self, operand: Sentence) -> None:
        assert isinstance(
            operand, Sentence), f"{operand} is not of type Sentence"
        self.operand = operand

    def __repr__(self) -> str:
        return f"¬({self.operand.__repr__()})"

    def evaluate(self, model: Dict[str, bool]) -> bool:
        return not self.operand.evaluate(model)

    def formula(self) -> str:
        return f"~({self.operand.formula()})"



class And_local(Sentence):
    def __init__(self, left: Sentence, right: Sentence) -> None:
        self.left = left
        self.right = right


    def evaluate(self, model: Dict[str, bool]) -> bool:
        return self.left.evaluate(model) and self.right.evaluate(model)

    def formula(self) -> str:
        return f"({self.left.formula()} & {self.right.formula()})"

    def __repr__(self) -> str:
        return f"({self.left.__repr__()} ∧ {self.right.__repr__()})"


class Or_local(Sentence):
    def __init__(self, left: Sentence, right: Sentence) -> None:
        self.left = left
        self.right = right

    def evaluate(self, model: Dict[str, bool]) -> bool:
        return self.left.evaluate(model) or self.right.evaluate(model)

    def formula(self) -> str:
        return f"({self.left.formula()} | {self.right.formula()})"

    def __repr__(self) -> str:
        return f"({self.left.__repr__()} ∨ {self.right.__repr__()})"


class Implies_local(Sentence):
    def __init__(self, left: Sentence, right: Sentence) -> None:
        self.left = left
        self.right = right

    def evaluate(self, model: Dict[str, bool]) -> bool:
        # P => Q is equivalent to ¬P ∨ Q. See page 249 Figure 7.11
        return (not self.left.evaluate(model)) or self.right.evaluate(model)

    def formula(self) -> str:
        return f"(~{self.left.formula()} | {self.right.formula()})"

    def __repr__(self) -> str:
        return f"({self.left.__repr__()} => {self.right.__repr__()})"


class BiConditional_local(Sentence):
    def __init__(self, left: Sentence, right: Sentence) -> None:
        self.left = left
        self.right = right

    def evaluate(self, model: Dict[str, bool]) -> bool:
        return ((not self.left.evaluate(model)) or self.right.evaluate(model)) and ((not self.right.evaluate(model)) or self.left.evaluate(model))

    def formula(self) -> str:
        return f"(~{self.left.formula()} | {self.right.formula()}) & (~{self.right.formula()} | {self.left.formula()})"

    def __repr__(self) -> str:
        return f"({self.left.__repr__()} <=> {self.right.__repr__()})"


def convert_to_cnf(sentence : str) -> Symbol:
    return to_cnf(sentence, False)

def is_satisfiable(sentence : str) -> bool:
    return satisfiable(sentence)
