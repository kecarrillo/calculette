import unittest
from tri import splitter

# Cas des listes possibles
# a = [12, 23, -45, 78]
# b = ["a", "b", "c"]
# c = [45.2, 12.5, 89.3]
# d = ["458", 456]
# e = []
# f = [" "]
# g = ["45,2", "89,5"]
# h = [["12", "78"], [465, 45]]
# i = [{"toto": 45}]
# n = [<object>]
# o = [("toto", 456)]
# m = [complex(45,45)]
# k = [True, False]
# l = [raise BaseException]

# Cas possibles separateurs: \
# a.split(" ", ",")
# a.split(" ", None)
# a.split(" ", "a")
# a.split(" ", 4)
# a.split(" ", 4.5)
# a.split(" ", [45.5, 78.9])

# Cas liste plus 1 million caractères
# Cas d'usage simultanné


class SplitTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions de la fonction 'splitter'.
    """

    def test_split_string_space(self):
        """Test le fonctionnement de la fonction 'splitter'."""
        string_space = "je suis un test"
        # Vérifie que 'elt' est dans 'liste'
        with self.assertRaises(ValueError):
            splitter(string_space)
        # self.assertRaises(ValueError, splitter, string_space)

    def test_split_ok(self):
        """Test le fonctionnement de la fonction 'splitter'."""
        string_space = "123 45 98 365"
        result_string_space = [123, 45, 98]
        elt = splitter(string_space)
        # Vérifie que 'elt' est dans 'liste'

        self.assertEqual(elt, result_string_space)

    def test_split_ok2(self):
        """Test le fonctionnement de la fonction 'splitter'."""
        string_space = "123 45 98 365 "
        result_string_space = [123, 45, 98, 365]
        elt = splitter(string_space)
        # Vérifie que 'elt' est dans 'liste'

        self.assertEqual(elt, result_string_space)

    def test_split_none(self):
        string_none = ''
        elt = splitter(string_none)
        self.assertIsNotNone(string_none)

unittest.main()
