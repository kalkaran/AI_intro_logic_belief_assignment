from src.logic import *
from src.parser import Parser

#example0 = '~(A & B) | ((C & D) | E)'
example0 = 'A'
example1 = 'A & ~(B)'
example2 = '~(A)'
example3 = 'A'
example4 = 'A => B'
example5 = 'A <=> B'
example6 = '(A <=> B) => (B <=> A) & A | B'

examples = [example0
        , example1
        , example2
        , example3
        , example4
        , example5
        , example6]


def printValidSyntax():
    for example in examples:
        # sentence = "(~(P) => (P | R))"
        # parser = Parser(sentence)
        parser = Parser(example)
        sentence = parser.parse()
        print(f"{example} is parsed as:", sentence)
        print(f" Sentence formula : {sentence.formula()}")
        print(f" CNF Form : {convert_to_cnf(sentence.formula())}")

        #print(sentence.evaluate(model))



"""
    p = Atom("P")
    q = Atom("A")
    r = Atom("R")
    model = {"B" : False, "A" : True, "C" : True  } # , "A" : True}
    parser = Parser('(A <=> B) => (B <=> A) & A | B & ~C')
    sentence = parser.parse() # Implies(Not(p), Or(q, r))
    # sentence = "(~(P) -> (P | R))"
    print(sentence.formula())
    print(convert_to_cnf(sentence.formula()))
    print(sentence.evaluate(model))
    """