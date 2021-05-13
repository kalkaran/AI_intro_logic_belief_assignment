from abc import ABC

from typing import Dict


class Sentence(ABC):
    def evaluate(self, model: Dict[str, bool]) -> bool:
        """ evaluates the truth of a sentence with respect to a particular model """
        pass

    def formula(self) -> str:
        """ returns a string representation of a given sentence"""
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
        return ((not self.left.evaluate(model)) or self.right.evaluate(model)) and (
                    (not self.right.evaluate(model)) or self.left.evaluate(model))

    def formula(self) -> str:
        return f"(~{self.left.formula()} | {self.right.formula()}) & (~{self.right.formula()} | {self.left.formula()})"

    def __repr__(self) -> str:
        return f"({self.left.__repr__()} <=> {self.right.__repr__()})"


def impl_free(sentence: Sentence) -> Sentence:
    if isinstance(sentence, Atom):
        return sentence
    elif isinstance(sentence, Not):
        return Not(impl_free(sentence.operand))
    elif isinstance(sentence, And):
        return And(impl_free(sentence.left), impl_free(sentence.right))
    elif isinstance(sentence, Or):
        return Or(impl_free(sentence.left), impl_free(sentence.right))
    elif isinstance(sentence, Implies):
        return Or(Not(impl_free(sentence.left)), impl_free(sentence.right))
    elif isinstance(sentence, BiConditional):
        return impl_free(And(Or(Not(sentence.left), sentence.right), Or(Not(sentence.right), sentence.left)))
    else:
        raise ValueError("The given input is not a valid propositional sentence.")


def negative_normal_form(sentence: Sentence) -> Sentence:
    if isinstance(sentence, Atom):
        return sentence
    elif isinstance(sentence, Not):
        if isinstance(sentence.operand, Not):
            return negative_normal_form(sentence.operand.operand)
        elif isinstance(sentence.operand, And):
            return Or(negative_normal_form(Not(sentence.operand.left)),
                      negative_normal_form(Not(sentence.operand.right)))
        elif isinstance(sentence.operand, Or):
            return And(negative_normal_form(Not(sentence.operand.left)),
                       negative_normal_form(Not(sentence.operand.right)))
        elif isinstance(sentence.operand, Atom):
            return sentence
    elif isinstance(sentence, And):
        return And(negative_normal_form(sentence.left), negative_normal_form(sentence.right))
    elif isinstance(sentence, Or):
        return Or(negative_normal_form(sentence.left), negative_normal_form(sentence.right))
    else:
        raise ValueError("The given input is not a valid propositional sentence.")


def distribute(s1: Sentence, s2: Sentence) -> Sentence:
    if isinstance(s1, And):
        return And(distribute(s1.left, s2), distribute(s1.right, s2))
    elif isinstance(s2, And):
        return And(distribute(s1, s2.left), distribute(s1, s2.right))
    else:
        return Or(s1, s2)


def cnf(sentence: Sentence) -> Sentence:
    if isinstance(sentence, Atom):
        return sentence
    elif isinstance(sentence, Not) and isinstance(sentence.operand, Atom):
        return sentence
    elif isinstance(sentence, And):
        return And(cnf(sentence.left), cnf(sentence.right))
    elif isinstance(sentence, Or):
        return distribute(cnf(sentence.left), cnf(sentence.right))
    else:
        raise ValueError("Invalid input sentence.")


def convert_to_cnf(sentence : Sentence) -> Sentence:
    imp_free = impl_free(sentence)
    nnf = negative_normal_form(imp_free)
    return cnf(nnf)


def split_cnf_into_list_clauses(sentence : Sentence) -> list:
    CNF_list = recursive_split(sentence)
    print(f"List: {CNF_list}")
    filtered_CNF_list = remove_redundant_clauses(CNF_list)
    print(f"List: {filtered_CNF_list}")

    return filtered_CNF_list




def recursive_split(sentence : Sentence, clause_list=None):
    # Creates list if list has not been passed as argument
    if clause_list is None:
        clause_list = []
    # Return the list if we need to replicate 0 more times
    if isinstance(sentence, Atom):
        return clause_list
    elif isinstance(sentence, Not):
        return Not(sentence.operand)
    elif isinstance(sentence, And):
        if not sub_tree_contains_and(sentence.left):
            clause_list.append(sentence.left)

        if not sub_tree_contains_and(sentence.right):
            clause_list.append(sentence.right)

        recursive_split(sentence.left, clause_list)
        recursive_split(sentence.right, clause_list)
    elif isinstance(sentence, Or):
        return Or(sentence.left, sentence.right)
    return clause_list


def sub_tree_contains_and(sentence : Sentence):
    if isinstance(sentence, Atom):
        return False
    elif isinstance(sentence, Not):
        return False
    elif isinstance(sentence, And):
        return True
    elif isinstance(sentence, Or):
        return False


def remove_redundant_clauses(clause_list):
    for belief in clause_list:
        print(type(belief))
        print(belief)
    return list(dict.fromkeys(clause_list))


class BeliefBase():
    pass
