#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Calculatrice en python."""


def log(alerte, message, lvl='DEBUG'):
    """This function makes a log file.

    :param alerte: Debug level of the alert to log.
    :type alerte: string
    :param message: Message to display in the log file.
    :type message: string
    :param lvl: (Optional) Level of displayed alert in log file.
    :type: string
    :return: Message to display.
    :rtype: string
    """
    from logging import (debug, error, warning, critical, basicConfig,
                         DEBUG, WARNING, CRITICAL, ERROR)

    # Associate the lvl arg with the logging level
    level_names = {'DEBUG': DEBUG,
                   'WARNING': WARNING,
                   'CRITICAL': CRITICAL,
                   'ERROR': ERROR}

    if level_names[lvl]:  # with appropriate arg
        level = level_names[lvl]
    else:  # if wrong arg
        level = DEBUG

    # Config of the log file.
    basicConfig(filename='log_calculatrice.log',
                format='%(asctime)s - %(levelname)s: %(message)s',
                level=level,
                filemode='a')

    if alerte is 'debug':  # information
        debug(message)
        message = ''
    elif alerte is 'error':  # error
        error(message)
    elif alerte is 'warning':  # warning
        warning(message)
    elif alerte is 'critical':  # critical error (end of the execution)
        critical(message)
    else:  # Bad use of the log function
        message = 'Le paramètre alerte passé à la fonction log() est ' \
                  f'incorrecte !\nL\'ancien message était: "{message}".\n'\
                  f'L\'ancien niveau d\'alerte était: "{alerte}".'
        alerte = 'error'
        log(alerte, message)
    return message


def recuperation_saisie():
    """This function return the result from user's operation.

    :result: The result from the user's operation.
    :rtype: float or integer

    :example:

    >>> recuperation_saisie()
    Saisissez votre calcul:
    >>> 5*5
    25

    .. seealso:: main()
    """
    try:
        result = eval(input("Saisissez votre calcul:"))
        log('debug', f'Success: catching user\'s input and calculate '
                     f'it: "{result}".')
    except Exception as e:
        print(log('error', f'Erreur:{e}'))
        result = recuperation_saisie()
    return result


def fichier(result):
    """This function create a file and a folder the user can choose and write
    the result in this file.

    :param result: Result from the function reciperation_saisie().
    :type: float or integer.
    :return: Result within a file.
    :rtype: Object.
    """
    from os import makedirs, sep
    from os.path import abspath, split, join

    local_path = abspath(split(__file__)[0])

    folder_path = input("Où désirez-vous stocker votre fichier de résultat? \n"
                        "(Saisir None pour conserver l'emplacement du fichier"
                        " à l'emplacement du script)")

    if folder_path == 'None':
        folder_path = local_path
    else:
        makedirs(folder_path, exist_ok=True)
    log('debug', f'Success: folder: {folder_path}.')

    file_name = input("Comment souhaitez-vous nommer votre fichier?\n"
                      "(Ou quel fichier souhaitez vous complèter?)")
    file_name = file_name + '.txt'
    log('debug', f'Success: name of the file: {file_name}.')

    # Récupération du chemin complet du fichier à complèter ou créer:
    full_path = join(folder_path + sep, file_name)

    try:
        decor = 30 * '*'
        separator = 'END'.center(30, '*')
        with open(full_path, 'a') as w_file:
            w_file.write(str(result))
            w_file.write('\n' + decor + '\n')
            w_file.write(separator + '\n')
            w_file.write(decor + '\n')
        print(f"Votre fichier se trouve à l'emplacement suivant:{full_path}")
        log('debug', f'Success: result added in the file.')
    # En cas d'erreur:
    except Exception as e:
        log('error', f'Error: impossible to add the result in the file: {e}.')


def main():
    """This function run the differents functions of the script.

    :return: The file with the result of the user's operation.
    :rtype: Object.

    .. seealso:: recuperation_saisie(), fichier().
    """
    fichier(recuperation_saisie())


if __name__ == "__main__":
    main()
