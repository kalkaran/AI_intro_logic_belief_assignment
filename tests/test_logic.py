from src.logic import Atom, And, Or, Not, Implies, BiConditional

# The tests in this module correspond to the truth table on page 246 Figure 7.8

# Run the tests using the 'pytest' command


def test_atom():
    p = Atom("P")
    model = {"P": True}
    assert p.evaluate(model)


def test_atom_negative():
    q = Atom("Q")
    model = {"Q": False}
    assert not q.evaluate(model)


def test_atom_negation():
    p = Not(Atom("P"))
    model = {"P": True}
    assert not p.evaluate(model)


def test_atom_negation_false():
    p = Not(Atom("P"))
    model = {"P": False}
    assert p.evaluate(model)


def test_and_sentence_case_1():
    p = Atom("P")
    q = Atom("Q")
    and_sentence = And(p, q)
    model = {"P": True, "Q": True}
    assert and_sentence.evaluate(model)


def test_and_sentence_case_2():
    p = Atom("P")
    q = Atom("Q")
    and_sentence = And(p, q)
    model = {"P": True, "Q": False}
    assert not and_sentence.evaluate(model)


def test_and_sentence_case_3():
    p = Atom("P")
    q = Atom("Q")
    and_sentence = And(p, q)
    model = {"P": False, "Q": True}
    assert not and_sentence.evaluate(model)


def test_and_sentence_case_4():
    p = Atom("P")
    q = Atom("Q")
    and_sentence = And(p, q)
    model = {"P": False, "Q": False}
    assert not and_sentence.evaluate(model)


def test_or_sentence_case_1():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = Or(p, q)
    model = {"P": True, "Q": True}
    assert or_sentence.evaluate(model)


def test_or_sentence_case_2():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = Or(p, q)
    model = {"P": True, "Q": False}
    assert or_sentence.evaluate(model)


def test_or_sentence_case_3():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = Or(p, q)
    model = {"P": False, "Q": True}
    assert or_sentence.evaluate(model)


def test_or_sentence_case_4():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = Or(p, q)
    model = {"P": False, "Q": False}
    assert not or_sentence.evaluate(model)


def test_implication_sentence_case_1():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = Implies(p, q)
    model = {"P": True, "Q": True}
    assert or_sentence.evaluate(model)


def test_implication_sentence_case_2():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = Implies(p, q)
    model = {"P": True, "Q": False}
    assert not or_sentence.evaluate(model)


def test_implication_sentence_case_3():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = Implies(p, q)
    model = {"P": False, "Q": True}
    assert or_sentence.evaluate(model)


def test_implication_sentence_case_4():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = Implies(p, q)
    model = {"P": False, "Q": False}
    assert or_sentence.evaluate(model)


def test_biconditional_sentence_case_1():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = BiConditional(p, q)
    model = {"P": True, "Q": True}
    assert or_sentence.evaluate(model)


def test_biconditional_sentence_case_2():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = BiConditional(p, q)
    model = {"P": True, "Q": False}
    assert not or_sentence.evaluate(model)


def test_biconditional_sentence_case_3():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = BiConditional(p, q)
    model = {"P": False, "Q": True}
    assert not or_sentence.evaluate(model)


def test_biconditional_sentence_case_4():
    p = Atom("P")
    q = Atom("Q")
    or_sentence = BiConditional(p, q)
    model = {"P": False, "Q": False}
    assert or_sentence.evaluate(model)
