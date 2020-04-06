# coding=utf-8
class Runner(object):
    """Runner: affiche les états des résultats."""
    # Résultats de tests
    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"

    def __init__(self):
        """constructeur"""
        pass

    def run(self, input):
        return (input, Runner.UNRESOLVED)
