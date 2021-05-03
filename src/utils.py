from src.parser import *

example0 = '~(A & B) | ((C & D) | E)'
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
        parser = Parser(example)
        print(f"{example} is parsed as:", parser.parse())
