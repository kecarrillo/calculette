from fuzzer_calc import EXPR_GRAMMAR
import random
import re

# a = EXPR_GRAMMAR["<digit>"]
#
# print(a)

re.compile(r'(<[^<> ]*>)')


def simple_grammar_fuzzer(expr_gr, max_digit=100, nb_operator=1):
    list_number = []
    for n in range(0, nb_operator+1):
        nbr = random.choices(expr_gr["<digit>"], k=max_digit)
        list_number.append(nbr)
    list_operator = random.choices(expr_gr["<OPERATOR>"], k=nb_operator)
    lists = list_number[0]
    for l in range(0, nb_operator-1):
        lists += list_operator[l] + list_number[l+1]
    result = ''.join(lists)
    return result


# res = simple_grammar_fuzzer(EXPR_GRAMMAR, 2, 1)
# print(res)


def simple_grammar_review(expr_gr, max_digit=100, nb_operator=1):
    results = random.choices(expr_gr["<digit>"], k=max_digit)
    for i in range(0, nb_operator):
        operator = random.choices(expr_gr["<OPERATOR>"], k=1)
        nb = random.choices(expr_gr["<digit>"], k=max_digit)
        results += operator +nb
    results = ''.join(results)
    return results


a = simple_grammar_review(EXPR_GRAMMAR, 0, 10)
print(a)

def less_simple_grammar_review(exp_re, max_digit=100, nb_operator=1):

    pass
