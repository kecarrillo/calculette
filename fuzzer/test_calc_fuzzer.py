# coding=utf-8

import random
import re
from fuzzer_calc import EXPR_GRAMMAR as GRAMMAR
from ExpansionError import ExpansionError
from Fuzzer import Fuzzer


class TestCalcFuzzer(Fuzzer):

    def __init__(self, grammar=GRAMMAR, start=GRAMMAR["<start>"],
                 max_expansion=10, max_ins_gr=10, log="text"):
        super(TestCalcFuzzer, self).__init__()
        self.grammar = grammar
        self.start = start
        self.max_expansion = max_expansion
        self.max_ins_gr = max_ins_gr
        self.log = log

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

    @staticmethod
    def simple_grammar_review(self, max_digit=100, nb_operator=1):
        results = random.choices(self.grammar["<digit>"], k=max_digit)
        for i in range(0, nb_operator):
            operator = random.choices(self.grammar["<operator>"], k=1)
            nb = random.choices(self.grammar["<digit>"], k=max_digit)
            results += operator + nb
        results = ''.join(results)
        # res, err = runner(results)
        # print(res + "\n", err)
        print(results)

    # Verification du contenu des extensions de grammaire:
    def check_grammar(self, expansion):

        re_grammar = re.compile(r'(<[^<> ]*>)')

        if isinstance(self.expansion, tuple):
            expansion = self.expansion[0]

        return re.findall(re_grammar, expansion)

    # fuzzer
    def grammar_review(self):

        nb_expansion = 0

        while len(self.check_grammar(self.start)) > 0:
            char_to_expand = random.choice(self.check_grammar(self.start))
            expansions = self.grammar[char_to_expand]
            expansion = random.choice(expansions)
            new_term = self.start.replace(char_to_expand, expansion, 1)

            if len(self.check_grammar(new_term)) < self.max_ins_gr:
                self.start = new_term
                if self.log:
                    print("%-40s" % (char_to_expand + " -> " + expansion),
                          self.start)
                nb_expansion = 0
            else:
                nb_expansion += 1
                if nb_expansion >= self.max_expansion:
                    raise ExpansionError("Ne peut pas être étendu par :\n"
                                         + repr(self.start))

        return self.start
