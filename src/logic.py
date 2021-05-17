import functools
from abc import ABC
from typing import Dict, List

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

def eliminate_implications(sentence: Sentence) -> Sentence:
    """"""
    """
        This function has been implemented from the pseudocode given in
        Huth, M., & Ryan, M. (2004). Propositional logic. In
        Logic in Computer Science: Modelling and Reasoning about Systems (pp. 1-92).
        Cambridge: Cambridge University Press.
    """
    # print("Implication elimination:", sentence.__class__, type(sentence), isinstance(sentence, Implies))
    if isinstance(sentence, Atom):
        return sentence
    elif isinstance(sentence, Not):
        return Not(eliminate_implications(sentence.operand))
    elif isinstance(sentence, And):
        return And(eliminate_implications(sentence.left), eliminate_implications(sentence.right))
    elif isinstance(sentence, Or):
        return Or(eliminate_implications(sentence.left), eliminate_implications(sentence.right))
    elif isinstance(sentence, Implies):
        return Or(Not(eliminate_implications(sentence.left)), eliminate_implications(sentence.right))
    elif isinstance(sentence, BiConditional):
        return eliminate_implications(And(Or(Not(sentence.left), sentence.right), Or(Not(sentence.right), sentence.left)))
    else:
        raise ValueError("The given input is not a valid propositional sentence.")


def negative_normal_form(sentence: Sentence) -> Sentence:
    """"""
    """
        This function has been implemented from the pseudocode given in
        Huth, M., & Ryan, M. (2004). Propositional logic. In
        Logic in Computer Science: Modelling and Reasoning about Systems (pp. 1-92).
        Cambridge: Cambridge University Press.
    """
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
    """"""
    """
        This function has been implemented from the pseudocode given in
        Huth, M., & Ryan, M. (2004). Propositional logic. In
        Logic in Computer Science: Modelling and Reasoning about Systems (pp. 1-92).
        Cambridge: Cambridge University Press.
    """
    if isinstance(s1, And):
        return And(distribute(s1.left, s2), distribute(s1.right, s2))
    elif isinstance(s2, And):
        return And(distribute(s1, s2.left), distribute(s1, s2.right))
    else:
        return Or(s1, s2)



def cnf_converter(sentence: Sentence) -> Sentence:
    """"""
    """
        This function has been implemented from the pseudocode given in
        Huth, M., & Ryan, M. (2004). Propositional logic. In
        Logic in Computer Science: Modelling and Reasoning about Systems (pp. 1-92).
        Cambridge: Cambridge University Press.
    """
    if isinstance(sentence, Atom):
        return sentence
    elif isinstance(sentence, Not) and isinstance(sentence.operand, Atom):
        return sentence
    elif isinstance(sentence, And):
        return And(cnf_converter(sentence.left), cnf_converter(sentence.right))
    elif isinstance(sentence, Or):
        return distribute(cnf_converter(sentence.left), cnf_converter(sentence.right))
    else:
        raise ValueError("Invalid input sentence.")


def convert_to_cnf(sentence: Sentence) -> Sentence:
    imp_free = eliminate_implications(sentence)
    nnf = negative_normal_form(imp_free)
    return cnf_converter(nnf)


def collect_clauses(sentence: Sentence) -> list:
    # Todo: Add method for splitting a sentence into a list of beliefs

    """
     Split a sentence into a list of clauses/beliefs.
     - A sentence is divided by each "and"

    Parameters:
        sentence (Sentence): Takes a sentence which has been converted to CNF.

    #Returns:
        list(Sentence): It returns a list of all beliefs in the sentence, when divided by each "and"
    """
    if isinstance(sentence, And):
        return collect_clauses(sentence.left) + collect_clauses(sentence.right)
    else:
        return [sentence]


def remove_redundant_beliefs(belief_list: list):
    # Todo: Add method for removing redundant beliefs from a list of beliefs

    """
     Removes redundant beliefs from a list of beliefs.
     - When a sentence is split into a list of belief it can contain the same belief multiple times.
     - Given the sentence P & P its split into a list of beliefs [P, P] but the list should only contain P.

    Parameters:
        belief_list (list): Takes a list of Sentences representing the beliefs

    #Returns:
        list(Sentence): The returns a list where all redundant beliefs are removed
    """

    new_belief_list = list(set(belief_list))

    return new_belief_list


def collect_atoms(sentence: Sentence):
    """
    """
    if isinstance(sentence, Atom):
        return {sentence.name}
    elif isinstance(sentence, Not):
        return collect_atoms(sentence.operand)
    elif isinstance(sentence, And) or isinstance(sentence, Or) \
            or isinstance(sentence, Implies) or isinstance(sentence, BiConditional):
        return set.union(collect_atoms(sentence.left), collect_atoms(sentence.right))


def tt_check_all(belief_sentence: Sentence, sentence: Sentence, atoms, model):
    """
     Creates a list of models based on the atoms that exits in the belief base.

     Given that the belief base contains P, Q and R then all possible models in the belief base is.
     - The number of models is always 2^(Number of atoms in the belief base)

     model = {"P": True, "Q": True, "R": True}
     model = {"P": False, "Q": False, "R": False}

     model = {"P": True, "Q": True, "R": False}
     model = {"P": True, "Q": False, "R": True}
     model = {"P": False, "Q": True, "R": True}

     model = {"P": True, "Q": False, "R": False}
     model = {"P": False, "Q": False, "R": True}
     model = {"P": False, "Q": True, "R": False}

    :param belief_sentence:
    :param sentence:
    :param atoms:
    :param model:
    :return:
    """
    if not atoms:
        if belief_sentence.evaluate(model):
            return sentence.evaluate(model)
        return True

    else:
        current_atoms = atoms.copy()
        atom = current_atoms.pop()

        true_model = model.copy()
        true_in_model = {atom: True}
        true_model.update(true_in_model)

        print(f"True model: {true_model}")
        false_model = model.copy()
        false_in_model = {atom: False}
        false_model.update(false_in_model)

        return tt_check_all(belief_sentence, sentence, current_atoms, true_model) \
               and tt_check_all(belief_sentence, sentence, current_atoms, false_model)


def tt_entails(belief: Sentence, query: Sentence) -> bool:
    """
    Check if there exits a model for which the belief list is true.
    - Loops through the models and check if the model makes the belief list true.

    If the belief list contains [P, Q] then the model = {"P": True, "Q": True}
    will result in the belief base being true.

    Parameters:
        belief (list): Takes a list of beliefs
        query: ...
    #Returns:
        valid(boolean): The returns a list of Models
    """

    atoms = set.union(collect_atoms(query), collect_atoms(belief))
    return tt_check_all(belief, query, atoms, dict())

def collect_disjuncts(sentence: Sentence) -> List:
    """
    >>> collect_disjuncts(Or(Atom("p"), Or(Atom("q"), And(Atom("q"), Atom("r")))))
    [p, q, (q ∧ r)]
    """
    if isinstance(sentence, Or):
        return collect_disjuncts(sentence.left) + collect_disjuncts(sentence.right)
    else:
        return [sentence]


def associate(connective, sentences):
    """
    >>> associate(And, [Atom("p"), Atom("q"), Atom("r")])
    ((p ∧ q) ∧ r)
    >>> associate(Or, [Atom("p"), Atom("q"), Atom("r")])
    ((p ∨ q) ∨ r)
    """
    return functools.reduce(lambda left, right: connective(left, right), sentences)


class BeliefBase(object):
    def __init__(self):
        self.beliefs = []

    def add_belief(self, sentence: Sentence) -> None:
        if tt_entails(self.belief_base_as_conjuncts(), sentence):
            self.beliefs.append(sentence)

    def belief_base_as_conjuncts(self):
        return associate(And, self.beliefs)

    def delete_belief(self, sentence_to_delete: Sentence):
        if sentence_to_delete in self.beliefs:
            self.beliefs.remove(sentence_to_delete)

    def reset_belief_base(self):
        self.beliefs.clear()

    def __str__(self):
        return "{" + ", ".join(self.beliefs) + "}"

if __name__ == "__main__":
    import doctest

    doctest.testmod()
