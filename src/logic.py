from abc import ABC
from action import *
from typing import Dict


# import src.parser as P


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

    def belief_list(self) -> str:
        return f"(~{self.left.formula()} | {self.right.formula()}) & (~{self.right.formula()} | {self.left.formula()})"

    def __repr__(self) -> str:
        return f"({self.left.__repr__()} <=> {self.right.__repr__()})"


################ Static Methods Below ####################

def impl_free(sentence: Sentence) -> Sentence:
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



def cnf(sentence: Sentence) -> Sentence:
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
        return And(cnf(sentence.left), cnf(sentence.right))
    elif isinstance(sentence, Or):
        return distribute(cnf(sentence.left), cnf(sentence.right))
    else:
        raise ValueError("Invalid input sentence.")


def convert_to_cnf(sentence: Sentence) -> Sentence:
    imp_free = impl_free(sentence)
    nnf = negative_normal_form(imp_free)
    return cnf(nnf)


def negate_sentence(sentence: Sentence) -> Sentence:
    """
     Negates a sentence

    Parameters:
        sentence (Sentence): Takes a sentence which has been converted to CNF.

    #Returns:
        negation (Sentence): Returns the negation of the sentence
    """

    return Not(sentence)


def adds_sentence_to_belief_base(sentence: Sentence, belief_base: list) -> list:
    # Todo: Add method for adding a sentence/belief to a belief base

    """
     Adds s sentence/belief to a belief base.

    Parameters:
        sentence (Sentence): Takes a sentence which has been converted to CNF.
        belief_base (List): Takes a list of beliefs.
    #Returns:
        list(Sentence): The returns a list of all beliefs, where the sentence has been added.
    """

    new_belief_base = belief_base.append(sentence)
    return new_belief_base


def collect_conjuncts(sentence: Sentence) -> list:
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
        return collect_conjuncts(sentence.left) + collect_conjuncts(sentence.right)
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
    # Todo: Add method for creating all possible models based on a list of atoms.

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

    Parameters:
        atom_list (list): Takes a list of atoms.

    #Returns:
        list(Models): The returns a list of Models
        :param sentence:
    """
    list_of_atoms = []

    if isinstance(sentence, Atom):
        return {sentence.name}
    elif isinstance(sentence, Not):
        return set.union(collect_atoms(sentence.operand))
    else:
        return set.union(collect_atoms(sentence.left), collect_atoms(sentence.right))


def check_all(belief_sentence: Sentence, sentence: Sentence, atoms, model):
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

        return check_all(belief_sentence, sentence, current_atoms, true_model) \
               and check_all(belief_sentence, sentence, current_atoms, false_model)


def model_checking(belief: Sentence, query: Sentence) -> bool:
    # Todo: Add method for preforming model checking

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
    return check_all(belief, query, atoms, dict())


def find_all_atoms_in_belief_base(belief_list: list):
    # Todo: Add method for removing redundant beliefs from a list of beliefs

    """
     Loops through the belief list, finds all atoms and adds them to a list

    Parameters:
        belief_list (list): Takes a list of sentences representing the belief base

    #Returns:
        list(Atom): It returns a list of all atoms in the belief list.
    """
    list_of_atoms = []

    # --- Implement code here---

    # ---------------------------

    return list_of_atoms


def check_for_entailment(belief_base: list):
    # Todo: Add a method for checking for entailment in a belief base

    """
     Checking for entailment in a belief base.
     - It done by preforming resolution on the belief base.
     - When preforming resolution it checks if two clauses can be resolved to an empty clause,
      when added the negation of a belief to the belief base.
      If this is true, it indicating that the belief is entailed by the belief base.
    - If the belief is entailed by the belief base, revision of the belief base must be preformed.
    - If the belief is not entailed by the belief base, it can just be added to the belief base.

    Parameters:
        belief_base(list): Takes a belief base, where a negated belief has been added to it.

    #Returns:
        action: Return an action based on the result of the check.
    """

    # --- Implement code here---

    # ---------------------------

    return Action.revision


def revise_belief_base(belief_base: list, action: Action, belief: Sentence):
    # Todo: Add a method for revision of a belief base.

    """
     Preforms a revision of a belief base.
     - The revision of a belief base is done with the intend to keeps as must information as possible.
     - Different techniques can be used, but their all build on the idea of reminder set
     - Look at Maxichoice Contraction,  Full-Meet Contraction and Partial-Meet Contraction
     - If the belief is not entailed by the belief base, it can just be added to the belief base.

    Parameters:
        belief_base(list): The current belief base.
        action (Action): An action base on the entailment check of the belief base,
                        where a negated belief was added to it.
        belief (Sentence): The belief that should be added to the belief base.

    #Returns:
        list : Returns a revised list of beliefs as the new belief base.
    """

    revised_belief_base = belief_base

    # --- Implement code here---

    # ---------------------------

    return revised_belief_base


class BeliefBase():
    pass
