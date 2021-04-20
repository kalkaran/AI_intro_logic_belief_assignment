from logic import Atom, And, Or, Not

def main():
    p = Atom("P")
    q = Atom("Q")
    r = Atom("R")
    model = {"P" : False, "Q" : False , "R" : True}
    sentence = And(Not(p), Or(q, r))
    print(sentence)
    print(sentence.evaluate(model))

if __name__ == "__main__":
    main()
