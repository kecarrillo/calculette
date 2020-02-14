import unittest
import test_calc_fuzzer as t
import re
from fuzzer_calc import EXPR_GRAMMAR as ex


print(t.simple_grammar_review(ex, 2, 3))


class TestCompteurFunction(unittest.TestCase):
    def test_Test1(self):
        self.assertRegex(t.simple_grammar_review(ex, 2, 3),
                                 r'^[0-9]{2}([\/*+\-%]{1}[0-9]{2}){3}$')

    def test_Test2(self):
        self.assertNotIn(t.simple_grammar_review(ex, 0, 3), r'^[0-9].$')

    def test_Test3(self):
        self.assertNotIn(t.simple_grammar_review(ex, 2, 0), r'^.[\/*+\-%].$')


if __name__ == '__main__':
    unittest.main()

