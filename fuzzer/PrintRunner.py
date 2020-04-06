# coding=utf-8
from Runner import Runner


class PrintRunner(Runner):
    def run(self, input):
        print(input)
        return (input, Runner.UNRESOLVED)
