from typing import List
from pyparsing import *
from logic import Atom, And, Or
from typing import List
from pprint import pprint

# example = '(A & B) V ((C & D) V E)'
# term = Word(alphas)
# AND = Keyword("&")
# OR = Keyword("V")
# expression = infixNotation(term, [(AND, 2, opAssoc.LEFT), (OR, 2, opAssoc.LEFT), ])
# parsed_statement = expression.parseString(example)
# print(parsed_statement)


example = '(A V B) V ((C & D) V E)'
example1 = 'A & B'
example2 = 'A'
term = Word(alphas)

bin_op = term + oneOf('& V ') + term
unary_op = oneOf("!") + term

AND = Keyword("&")
OR = Keyword("V")

expression = infixNotation(term, [
    (AND, 2, opAssoc.LEFT),
    (OR, 2, opAssoc.LEFT),
    ])

parsed_statement = expression.parseString(example)
#pprint(parsed_statement)
print("Parsed statement: ", parsed_statement)
for x in parsed_statement[0]:
    print(x)


# [
#   [
#       ['A', 'V', 'B'],
#             'V',
#       [
#           ['C', '&', 'D'],
#               'V',
#           'E'
#       ]
#   ]
# ]

# operator_map = {""}

#  [['A', '&', 'B'], 'V', 'B']

class Parser:

    def __init__(self) -> None:
        self.parsed_expression = []

    #expr [['A', '&', 'B'], 'V', 'B']
    # expr[0] ['A', '&', 'B']


    # [['A', 'V', 'B']]
    def build_ast(self, exprs):
        print("build_ast")
        for expr in exprs:
            print("expr", expr)
        # expr[0] = ['A', 'V', 'B']
            if not isinstance(expr, List):
                self.parsed_expression.append(Atom(expr)) # <-
            elif isinstance(expr, List):
                left_tree, op, right_tree = expr
                print(left_tree, op, right_tree)
                if op == '&':
                    print("AND")
                    conjunction = And(self.build_ast(left_tree), self.build_ast(right_tree))
                    self.parsed_expression.append("AND")
                    #return self.build_ast(rest)

                if op == 'V':
                    print("OR")
                    disjunction = Or(self.build_ast(left_tree), self.build_ast(right_tree))
                    self.parsed_expression.append("OR")
                    #return self.build_ast(rest)

    def print_exp(self):
        print("FINAL ANSWER")
        pprint(self.parsed_expression)


p = Parser()
p.build_ast([['A', '&', 'B'], 'V', 'B'])
p.print_exp()