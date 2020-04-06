# coding=utf-8
from Runner import Runner
from PrintRunner import PrintRunner
from test_calc_fuzzer import TestCalcFuzzer


class Fuzzer(object):
    def __init__(self):
        pass

    @staticmethod
    def fuzz(self, tester=TestCalcFuzzer()):
        return tester.grammar_review()

    def run(self, runner=Runner()):
        return runner.run(self.fuzz())

    def runs(self, runner=PrintRunner(), trials=10):
        outcomes = []
        for i in range(trials):
            outcomes.append(self.run(runner))
        return outcomes
