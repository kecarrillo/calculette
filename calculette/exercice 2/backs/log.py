#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module generate a log file.

.. seealso:: gui_calculatrice, cleaning, backs
"""

from os import makedirs
from os.path import abspath, join, split, sep, dirname
from datetime import datetime
from random import randint
from logging import (debug, error, warning, critical, basicConfig, DEBUG,
                     WARNING, CRITICAL, ERROR)

rdm = randint(0, 999_999)
time_run = datetime.now().strftime('%A-%d-%B-%Y_a_%Hh%Mmin%Ssec')


def file_log(message='?', warn='debug', lvl='ERROR'):
    """This function makes a log file.

    :param message: Message to display in the log file.
    :type message: string
    :param warn: (Optional) Debug level of the alert to log.
    :type warn: string
    :param lvl: (Optional) Level of displayed alert in log file.
    :type: string
    :return: Message to display.
    :rtype: string
    """
    # Associate the lvl arg with the logging level
    level_names = {'DEBUG': DEBUG,
                   'WARNING': WARNING,
                   'CRITICAL': CRITICAL,
                   'ERROR': ERROR}

    if level_names[lvl]:  # with appropriate arg
        level = level_names[lvl]
    else:  # if wrong arg
        level = DEBUG
    log_folder = join(dirname(abspath(split(__file__)[0])) + sep, "logs")
    makedirs(log_folder, exist_ok=True)
    # Config of the log file.
    basicConfig(filename=join(log_folder + sep,
                              f'{rdm}_log_gui_calc-{time_run}.log'),
                format='%(asctime)s - %(levelname)s: %(message)s',
                level=level,
                filemode='a')

    if warn is 'debug':  # information
        debug(message)
    elif warn is 'error':  # error
        error(message)
    elif warn is 'warning':  # warning
        warning(message)
    elif warn is 'critical':  # critical error (end of the execution)
        critical(message)
    else:  # Bad use of the log function
        message = 'Le paramètre alerte passé à la fonction log() est ' \
                  f'incorrecte !\nL\'ancien message était: "{message}".\n'\
                  f'L\'ancien niveau d\'alerte était: "{warn}".'
        file_log(message)
    return message
