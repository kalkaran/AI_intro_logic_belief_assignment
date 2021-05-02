from abc import ABC

import sympy
from sympy.logic.boolalg import to_cnf
from typing import Dict

class Sentence(ABC):
    def evaluate(self, model : Dict[str, bool]) -> bool:
        """ evaluates the truth of a sentence with respect to a particular model """
        pass

    def formula(self) -> str:
        """ returns a string representation of a given sentence """
        pass


class Atom(Sentence):
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def evaluate(self, model: Dict[str, bool]) -> bool:
        assert self.name in model, f"The {self.name} is not in model"

        return model.get(self.name)

    def formula(self) -> str:
        return self.name


class Not(Sentence):
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



class And(Sentence):
    def __init__(self, left: Sentence, right: Sentence) -> None:
        self.left = left
        self.right = right


    def evaluate(self, model: Dict[str, bool]) -> bool:
        return self.left.evaluate(model) and self.right.evaluate(model)

    def formula(self) -> str:
        return f"({self.left.formula()} & {self.right.formula()})"

    def __repr__(self) -> str:
        return f"({self.left.__repr__()} ∧ {self.right.__repr__()})"


class Or(Sentence):
    def __init__(self, left: Sentence, right: Sentence) -> None:
        self.left = left
        self.right = right

    def evaluate(self, model: Dict[str, bool]) -> bool:
        return self.left.evaluate(model) or self.right.evaluate(model)

    def formula(self) -> str:
        return f"({self.left.formula()} | {self.right.formula()})"

    def __repr__(self) -> str:
        return f"({self.left.__repr__()} ∨ {self.right.__repr__()})"


class Implies(Sentence):
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


class BiConditional(Sentence):
    def __init__(self, left: Sentence, right: Sentence) -> None:
        self.left = left
        self.right = right

    def evaluate(self, model: Dict[str, bool]) -> bool:
        return ((not self.left.evaluate(model)) or self.right.evaluate(model)) and ((not self.right.evaluate(model)) or self.left.evaluate(model))

    def formula(self) -> str:
        return f"(~{self.left.formula()} | {self.right.formula()}) & (~{self.right.formula()} | {self.left.formula()})"

    def __repr__(self) -> str:
        return f"({self.left.__repr__()} <=> {self.right.__repr__()})"


def convert_to_cnf(sentence : str) -> str:
    return to_cnf(sentence, True)
