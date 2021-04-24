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


example = '(A & B) V ((C & D) V E)'
example1 = 'A & B'
example2 = 'A'
term = Word(alphas)


AND = Keyword("&")
OR = Keyword("V")
# NOT = Keyword("¬")

expression = infixNotation(term, [
    (AND, 2, opAssoc.LEFT),
    (OR, 2, opAssoc.LEFT),
    # (NOT, 1, opAssoc.RIGHT),
    ])

parsed_statement = expression.parseString(example)


class Parser:

    def build_ast(self, expr):
        if not isinstance(expr, List):
            return Atom(expr)
        elif isinstance(expr, List):
            left_tree, op, right_tree = expr
            if op == '&':
                conjunction = And(self.build_ast(left_tree), self.build_ast(right_tree))
                return conjunction

            if op == 'V':
                disjunction = Or(self.build_ast(left_tree), self.build_ast(right_tree))
                return disjunction

    def print_exp(self):
        print("FINAL ANSWER")
        pprint(self.parsed_expression)


p = Parser()
result = p.build_ast([['A', '&', 'B'], 'V', ['A', 'V', 'B']])
result1 = p.build_ast([['A', 'V', 'B'], 'V', [['C', '&', 'D'], 'V', 'E']])
result2 = p.build_ast(parsed_statement.asList()[0])


print(result)
print(result1)
print(result2)