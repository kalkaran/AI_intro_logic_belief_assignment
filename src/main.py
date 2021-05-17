
from src.logic import Atom, Not, And, Or, Implies, BiConditional, convert_to_cnf
import src.logic as logic
# from src.controller import Controller
from src.agent import Agent
import src.parser as P

def main() -> None:
    controller = Controller()
    controller.start_main_loop()

    p = Atom("P")
    q = Atom("Q")
    r = Atom("R")
    # model = {"B": False, "A": True, "C": True}  # , "A" : True}
    # parser = Parser('(A <=> B) => (B <=> A) & A | B & ~C')
    sentence = Implies(And(Not(p), q), And(p, Implies(r, q)))
    # sentence = And(And(p, And(p, p)), p)
    # query = And(p, q)
    # print(f"Before CNF: {sentence}")
    # cnf_sentence = convert_to_cnf(sentence)
    # print(f"After CNF conversion: {cnf_sentence}")
    #
    # cnf_split = logic.collect_conjuncts(cnf_sentence)
    #
    # print(f"Split cnf sentence in list: {cnf_split}")
    #
    # print(f"Atoms: {logic.collect_atoms(cnf_sentence)}")
    #
    # print("Model check", logic.model_checking(cnf_sentence, query))

    agent = Agent()
    agent.declare_new_belief_base("P & P")
    agent.print_belief_base()

    agent.add_new_belief_to_belief_base("(~(P) & Q))")
    agent.print_belief_base()

    # agent.check_satisfiability_of_sentence("P & R")
    # agent.print_belief_base()

    # print(sentence.evaluate(model))

    # print("------------------\n")
    # controller = Controller()
    # controller.startMainLoop()


if __name__ == "__main__":
    main()

# def pl_resolution(kb, alpha):
#     """
#     [Figure 7.12]
#     Propositional-logic resolution: say if alpha follows from KB.
#     >>> pl_resolution(horn_clauses_KB, A)
#     # True
#     # """
#     clauses = kb.clauses + conjuncts(to_cnf(~alpha))
#     new = set()
#     while True:
#         n = len(clauses)
#         pairs = [(clauses[i], clauses[j])
#                  for i in range(n) for j in range(i + 1, n)]
#         for (ci, cj) in pairs:
#             resolvents = pl_resolve(ci, cj)
#             if False in resolvents:
#                 return True
#             new = new.union(set(resolvents))
#         if new.issubset(set(clauses)):
#             return False
#         for c in new:
#             if c not in clauses:
#                 clauses.append(c)
#
#
# def pl_resolve(ci, cj):
#     """Return all clauses that can be obtained by resolving clauses ci and cj."""
#     clauses = []
#     for di in disjuncts(ci):
#         for dj in disjuncts(cj):
#             if di == ~dj or ~di == dj:
#                 clauses.append(associate('|', unique(remove_all(di, disjuncts(ci)) + remove_all(dj, disjuncts(cj)))))
#     # return clauses


# def dpll_satisfiable(s):
#     """Check satisfiability of a propositional sentence.
#     This differs from the book code in two ways: (1) it returns a model
#     rather than True when it succeeds; this is more useful. (2) The
#     function find_pure_symbol is passed a list of unknown clauses, rather
#     than a list of all clauses and the model; this is more efficient.
#     >>> dpll_satisfiable(A&~B)
#     {A: True, B: False}
#     >>> dpll_satisfiable(P&~P)
#     False
#     """
#     clauses = conjuncts(to_cnf(s))
#     symbols = prop_symbols(s)
#     return dpll(clauses, symbols, {})
#
# def dpll(clauses, symbols, model):
#     "See if the clauses are true in a partial model."
#     unknown_clauses = [] ## clauses with an unknown truth value
#     for c in clauses:
#         val =  pl_true(c, model)
#         if val == False:
#             return False
#         if val != True:
#             unknown_clauses.append(c)
#     if not unknown_clauses:
#         return model
#     P, value = find_pure_symbol(symbols, unknown_clauses)
#     if P:
#         return dpll(clauses, removeall(P, symbols), extend(model, P, value))
#     P, value = find_unit_clause(clauses, model)
#     if P:
#         return dpll(clauses, removeall(P, symbols), extend(model, P, value))
#     P = symbols.pop()
#     return (dpll(clauses, symbols, extend(model, P, True)) or
#             dpll(clauses, symbols, extend(model, P, False)))
#
# def find_pure_symbol(symbols, unknown_clauses):
#     """Find a symbol and its value if it appears only as a positive literal
#     (or only as a negative) in clauses.
#     >>> find_pure_symbol([A, B, C], [A|~B,~B|~C,C|A])
#     (A, True)
#     """
#     for s in symbols:
#         found_pos, found_neg = False, False
#         for c in unknown_clauses:
#             if not found_pos and s in disjuncts(c): found_pos = True
#             if not found_neg and ~s in disjuncts(c): found_neg = True
#         if found_pos != found_neg: return s, found_pos
#     return None, None
#
# def find_unit_clause(clauses, model):
#     """A unit clause has only 1 variable that is not bound in the model.
#     >>> find_unit_clause([A|B|C, B|~C, A|~B], {A:True})
#     (B, False)
#     """
#     for clause in clauses:
#         num_not_in_model = 0
#         for literal in disjuncts(clause):
#             sym = literal_symbol(literal)
#             if sym not in model:
#                 num_not_in_model += 1
#                 P, value = sym, (literal.op != '~')
#         if num_not_in_model == 1:
#             return P, value
#     return None, None

# def unit_clause_assign(clause, model):
#     """Return a single variable/value pair that makes clause true in
#     the model, if possible.
#     >>> unit_clause_assign(A|B|C, {A:True})
#     (None, None)
#     >>> unit_clause_assign(B|~C, {A:True})
#     (None, None)
#     >>> unit_clause_assign(~A|~B, {A:True})
#     (B, False)
#     """
#     P, value = None, None
#     for literal in disjuncts(clause):
#         sym, positive = inspect_literal(literal)
#         if sym in model:
#             if model[sym] == positive:
#                 return None, None  # clause already True
#         elif P:
#             return None, None  # more than 1 unbound variable
#         else:
#             P, value = sym, positive
#     return P, value
#
#
# def inspect_literal(literal):
#     """The symbol in this literal, and the value it should take to
#     make the literal true.
#     >>> inspect_literal(P)
#     (P, True)
#     >>> inspect_literal(~P)
#     (P, False)
#     """
#     if literal.op == '~':
#         return literal.args[0], False
#     else:
#         return literal, True