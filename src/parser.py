from pyparsing import *


example = '(A & B) V ((C & D) V E)'

term = Word(alphas)
AND = Keyword("&")
OR = Keyword("V")

expression = infixNotation(term, [(AND, 2, opAssoc.LEFT), (OR, 2, opAssoc.LEFT), ])
parsed_statement = expression.parseString(example)

print(parsed_statement)

