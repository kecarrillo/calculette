#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module remove the old log files.

.. seealso:: log, gui_calculatrice, backs
"""

from os import walk, remove
from os.path import abspath, join, split, getctime, dirname
from re import match
from .log import file_log

default_folder = dirname(abspath(split(__file__)[0]))


def cleaning_folder():
    """Function that suppress the old log files.

    It keeps only 10 log files a time.

    :return: Remove the old log files.
    :rtype: void
    """
    # Catching the full path of the files
    for fodr, _, fs in walk(default_folder):
        file_log("Succès: récupération des fichiers.")
        files = [join(fodr, fname) for fname in fs]
        log_list = {}

        for f in files:
            # Filter the files to keep only the log files
            if match('^(.)+.log$', f) is not None:
                # Sort the logs from the dictionnary by creation date
                log_list[getctime(f)] = f
                sorted(log_list.keys())
        # If there is more than 9 logs, create 2 lists:
        # keys and values from dictionnary
        if len(log_list) > 9:
            k_logs = [k for k in log_list]
            v_logs = [log_list[k] for k in log_list]
            i = 0
            while i < 10:
                del k_logs[0]
                del v_logs[0]
                i += 1
            # Delete older logs to keep only 10 log files
            logs = {a: b for a, b in zip(k_logs, v_logs)}
            for old in logs.values():
                remove(old)
