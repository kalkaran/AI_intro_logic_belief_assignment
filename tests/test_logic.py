from src.logic import Atom_local, And_local, Or_local, Not_local, Implies_local, BiConditional_local

# The tests in this module correspond to the truth table on page 246 Figure 7.8

# Run the tests using the 'pytest' command


def test_atom():
    p = Atom_local("P")
    model = {"P": True}
    assert p.evaluate(model)


def test_atom_negative():
    q = Atom_local("Q")
    model = {"Q": False}
    assert not q.evaluate(model)


def test_atom_negation():
    p = Not_local(Atom_local("P"))
    model = {"P": True}
    assert not p.evaluate(model)


def test_atom_negation():
    p = Not_local(Atom_local("P"))
    model = {"P": False}
    assert p.evaluate(model)


def test_and_sentence_case_1():
    p = Atom_local("P")
    q = Atom_local("Q")
    and_sentence = And_local(p, q)
    model = {"P": True, "Q": True}
    assert and_sentence.evaluate(model)


def test_and_sentence_case_2():
    p = Atom_local("P")
    q = Atom_local("Q")
    and_sentence = And_local(p, q)
    model = {"P": True, "Q": False}
    assert not and_sentence.evaluate(model)


def test_and_sentence_case_3():
    p = Atom_local("P")
    q = Atom_local("Q")
    and_sentence = And_local(p, q)
    model = {"P": False, "Q": True}
    assert not and_sentence.evaluate(model)


def test_and_sentence_case_4():
    p = Atom_local("P")
    q = Atom_local("Q")
    and_sentence = And_local(p, q)
    model = {"P": False, "Q": False}
    assert not and_sentence.evaluate(model)


def test_or_sentence_case_1():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = Or_local(p, q)
    model = {"P": True, "Q": True}
    assert or_sentence.evaluate(model)


def test_or_sentence_case_2():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = Or_local(p, q)
    model = {"P": True, "Q": False}
    assert or_sentence.evaluate(model)


def test_or_sentence_case_3():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = Or_local(p, q)
    model = {"P": False, "Q": True}
    assert or_sentence.evaluate(model)


def test_or_sentence_case_4():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = Or_local(p, q)
    model = {"P": False, "Q": False}
    assert not or_sentence.evaluate(model)


def test_implication_sentence_case_1():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = Implies_local(p, q)
    model = {"P": True, "Q": True}
    assert or_sentence.evaluate(model)


def test_implication_sentence_case_2():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = Implies_local(p, q)
    model = {"P": True, "Q": False}
    assert not or_sentence.evaluate(model)


def test_implication_sentence_case_3():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = Implies_local(p, q)
    model = {"P": False, "Q": True}
    assert or_sentence.evaluate(model)


def test_implication_sentence_case_4():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = Implies_local(p, q)
    model = {"P": False, "Q": False}
    assert or_sentence.evaluate(model)


def test_biconditional_sentence_case_1():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = BiConditional_local(p, q)
    model = {"P": True, "Q": True}
    assert or_sentence.evaluate(model)


def test_biconditional_sentence_case_2():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = BiConditional_local(p, q)
    model = {"P": True, "Q": False}
    assert not or_sentence.evaluate(model)


def test_biconditional_sentence_case_3():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = BiConditional_local(p, q)
    model = {"P": False, "Q": True}
    assert not or_sentence.evaluate(model)


def test_biconditional_sentence_case_4():
    p = Atom_local("P")
    q = Atom_local("Q")
    or_sentence = BiConditional_local(p, q)
    model = {"P": False, "Q": False}
    assert or_sentence.evaluate(model)
