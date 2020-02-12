#!/usr/bin/env python3
import sys
import random
from os.path import join

i = int(sys.argv[1])
print(' '.join([' ' + str(random.randint(-i, i)) for x in range(i)]))


