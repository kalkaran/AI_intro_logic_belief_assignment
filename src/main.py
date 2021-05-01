from logic import Atom, And, Or, Not, Implies, convert_to_cnf

import parser

def main():
    p = Atom("P")
    q = Atom("A")
    r = Atom("R")
    model = {"B" : False, "A" : True } # , "A" : True}
    sentence = parser.Parser('(A <=> B) => (B <=> A) & A | B').parse() # Implies(Not(p), Or(q, r))
    # sentence = "(~(P) -> (P | R))"
    print(sentence.formula())
    print(convert_to_cnf(sentence.formula()))
    print(sentence.evaluate(model))

if __name__ == "__main__":
    main()
