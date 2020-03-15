from fuzzer_calc import EXPR_GRAMMAR as expr_gr
from runner import runner
import random


# def simple_grammar_fuzzer(expr_gr, max_digit=100, nb_operator=1):
#     list_number = []
#     for n in range(0, nb_operator + 1):
#         nbr = random.choices(expr_gr["<digit>"], k=max_digit)
#         list_number.append(nbr)
#     list_operator = random.choices(expr_gr["<OPERATOR>"], k=nb_operator)
#     lists = list_number[0]
#     for l in range(0, nb_operator - 1):
#         lists += list_operator[l] + list_number[l + 1]
#     result = ''.join(lists)
#     res, err = runner(result)
#     print(res + "\n", err)
#


def simple_grammar_review(expr_gr, max_digit=100, nb_operator=1):
    results = random.choices(expr_gr["<digit>"], k=max_digit)
    for i in range(0, nb_operator):
        operator = random.choices(expr_gr["<OPERATOR>"], k=1)
        nb = random.choices(expr_gr["<digit>"], k=max_digit)
        results += operator + nb
    results = ''.join(results)
    res, err = runner(results)
    print(res + "\n", err)


def sep_grammar_review(expr_gr, max_digit=100, nb_operator=1, nb_separator=1):
    results = random.choices(expr_gr["<digit>"], k=max_digit)
    for i in range(0, nb_operator):
        operator = random.choices(expr_gr["<OPERATOR>"], k=1)
        nb = random.choices(expr_gr["<digit>"], k=max_digit)
        results += operator + nb
    for i in range(0, nb_separator):
        separator = random.choices(expr_gr["<SEPARATOR>"], k=1)
        results += separator
    results = ''.join(results)
    res, err = runner(results)
    print(res + "\n", err)


def exceptions_grammar_review(exp_gr, max_digit=100, nb_operator=1):
    print("without digit: ")
    simple_grammar_review(exp_gr, 0, nb_operator)
    print("without operator: ")
    simple_grammar_review(exp_gr, max_digit, 0)
    print("zero division: ")
    result = str(max_digit) + "/0"
    res, err = runner(result)
    print(res + "\n", err)
