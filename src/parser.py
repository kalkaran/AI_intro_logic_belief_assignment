from typing import List
import pyparsing as p
from src.logic import Atom_local, And_local, Or_local, Implies_local, BiConditional_local, Not_local, Sentence
from typing import List
#from main import try_except
import functools


def try_except(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as ex:
            print(f.__name__)
            print(ex)
    return inner



class Parser:
    def __init__(self, input_string) -> None:
        self.input_string = input_string

        self.ATOM = p.Word(p.alphas)
        self.AND_TOKEN = p.Keyword("&")
        self.OR_TOKEN = p.Keyword("|")
        self.NOT_TOKEN = p.Keyword("~")
        self.IMPLIES_TOKEN = p.Keyword("=>")
        self.BICOND_TOKEN = p.Keyword("<=>")

        self.BIN_OP = 3
        self.UNARY_OP = 2

        self.expression = p.infixNotation(
            self.ATOM,
                [ (self.NOT_TOKEN, 1, p.opAssoc.RIGHT)
                , (self.AND_TOKEN, 2, p.opAssoc.LEFT)
                , (self.OR_TOKEN,  2, p.opAssoc.LEFT)
                , (self.IMPLIES_TOKEN, 2, p.opAssoc.RIGHT)
                , (self.BICOND_TOKEN, 2, p.opAssoc.RIGHT)
                ]
            )

        self.operators = { '&' : And_local
                         , '|' : Or_local
                         , '=>': Implies_local
                         , '<=>': BiConditional_local
                         , '~' : Not_local}

    @try_except
    def parse(self) -> Sentence:
        parsed_statement = self.expression.parseString(self.input_string)
        return self.build_ast(parsed_statement.asList()[0])

    @try_except
    def build_ast(self, expr: List) -> Sentence:
        """ This function builds an abstract syntax tree from the parsed input.

            Parameters:
                    expr (List): A ParseResult from pyparsing.parseString
                               converted to a list of lists.

            Returns:
                    ast (Sentence): The corresponding abstract syntax tree (ast) of the parsed
                                      input.
        """
        if not isinstance(expr, List):
            return Atom_local(expr)
        elif isinstance(expr, List):
            if len(expr) == self.BIN_OP:
                left_tree, op, right_tree = expr
                connective = self.operators[op]
                return connective(self.build_ast(left_tree), self.build_ast(right_tree))
            elif len(expr) == self.UNARY_OP:
                op, right_tree = expr
                connective = self.operators[op]
                return connective(self.build_ast(right_tree))









