# coding=utf-8
from Runner import Runner
import subprocess


class ProgramRunner(Runner):
    def __init__(self, program):
        """Constructeur"""
        super(ProgramRunner, self).__init__()
        self.program = program

    def run_process(self, input=""):
        """Lance le programme contenant input en entrée.

        :arg input: Entrée
        :type input: string
        :return: Résultat de l'execution du programme.
        :rtype: object
        """
        return subprocess.run(self.program,
                              input=input,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              universal_newlines="text")

    def run(self, input=""):
        """Execute le programme avec la méthode run_process.

        :arg input: Entrée
        :type input: string
        :return: Résultat du test.
        :rtype: tuple
        """
        result = self.run_process(input)

        if result.returncode == 0:
            outcome = self.PASS
        elif result.returncode < 0:
            outcome = self.FAIL
        else:
            outcome = self.UNRESOLVED

        return (result, outcome)
