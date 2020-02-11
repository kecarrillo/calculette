#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This program is a calculator.

This module is the main module, where all other modules are executed.

.. seealso:: log, cleaning, backs
"""

import os
from os import makedirs
from os.path import abspath, split, join, sep
from stat import filemode
from tkinter import (Button, Frame, Tk, Entry, StringVar, BOTH, LabelFrame,
                     messagebox)
from math import pi, inf, sin, asin, cos, acos, tan, atan, log, pow, sqrt
from sqlite3 import connect
from datetime import datetime
from backs.log import file_log
from backs.cleaning import cleaning_folder


default_text = 'Saisissez votre calcul'
default_file = "Résultats"
default_folder = abspath(split(__file__)[0])
calculate = ""
list_math_operator = ["sqrt", "pow", "cos", "acos", "tan", "atan", "sin",
                      "asin", "log"]
key_list = [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 107, 109, 106, 111,
            110, 53, 219, 187, 188, 112, 113, 114, 115, 116, 117, 118, 119,
            120, 121, 122, 8, 46, 27, 13]


# press echap on window
def exit_calc(event):
    """This function allow the user to quit the program with the escape key.

    It will send the data from the database to the result file.

    :param event: Catch the escape key.
    :type: object
    :return: Quit the program and write the datas from the database on the result file.
    :rtype: void
    """
    if event.keycode == 27:
        resp = messagebox.askquestion("Quitter?", "En êtes-vous sûr?")
        if resp == 'yes':
            path_results = join(file_path.get() + sep,
                                file_name.get() + ".txt")
            use_db(req='fetch', path=path_results)
            file_log("Succès: sortie du programme.")
            main_screen.destroy()


def on_event(event):
    """This function catch and apply the key pressed by users in display screen.

    :param event: Value of the key.
    :type: object
    :return: display the equation or result, and generate log.
    :rtype: void
    """
    global calculate
    file_log("Succès: touche récupérée.")
    # Nettoyage de l'écran
    if equation.get() is default_text:
        equation.set('')
    kbc = event.keycode
    if kbc in key_list:
        file_log(f"Succès: touche reconnue: {event.keysym}.")
        numbers = key_list[:17]
        if kbc in numbers:
            calculate += event.char
            equation.set(calculate)
        elif kbc == 188:
            b_click(".")
        elif kbc == 13 or kbc == 187:
            b_click("=")
        elif kbc == 46:
            b_click("C")
        elif kbc == 112:
            b_click("pi")
        elif kbc == 113:
            b_click("inf")
        elif kbc == 114:
            b_click("log")
        elif kbc == 115:
            b_click("sqrt")
        elif kbc == 116:
            b_click("pow")
        elif kbc == 117:
            b_click("sin")
        elif kbc == 118:
            b_click("asin")
        elif kbc == 119:
            b_click("cos")
        elif kbc == 120:
            b_click("acos")
        elif kbc == 121:
            b_click("tan")
        elif kbc == 122:
            b_click("atan")
        elif kbc == 8:
            file_log("Succès: suppression de la dernière entrée.")
            if len(calculate) > 0:
                del calculate[-1]
                equation.set(calculate)
            else:
                calculate = default_text
                equation.set(calculate)
        else:
            messagebox.showerror("Echec", "Caractère incorrecte!")
            file_log("Echec: impossible d'utiliser la touche.", "error")
    else:
        messagebox.showerror("Echec", "Cette touche n'est pas disponible!")
        file_log("Echec: touche non reconnue.", "error")


def b_click(x):
    """Function that catch the value from buttons.

    :param x: Value of the button.
    :type: string
    :return: display the equation or result, create a database, insert result within the database and generate log.
    :rtype: void
    """
    global calculate
    file_log("Succès: lancement de la phase bouton.")

    if x is "=":
        file_log("Succès: reconnaissance du bouton '='.")
        try:
            result = str(eval(calculate))
            file_log("Succès: calcul effectué.")
            equation.set(result)
            file_log("Succès: affichage du résultat.")
            calculate = ""
            file_log("Succès: réinitialisation du calcul.")
            # Insert the data in the database
            path_result(file_path.get(), file_name.get(), result)
            use_db(req='insert', value=result)

        except Exception as err:
            messagebox.showerror("Echec", f" error: {err} ")
            file_log("Echec: Calcul impossible.", "error")
            calculate = ""
            file_log("Succès: réinitialisation du calcul.")
    elif x is '0':
        file_log("Succès: reconnaissance du bouton '0'.")
        if calculate[-1] is "/":
            messagebox.showerror("Echec",
                                 " Erreur: Division par 0 impossible.")
            file_log("Echec: Calcul impossible.", "error")
        else:
            calculate += str(x)
            equation.set(calculate)
    elif x is 'C':
        file_log("Succès: reconnaissance du bouton 'C'.")
        calculate = ""
        file_log("Succès: réinitialisation du calcul.")
        equation.set(default_text)
        file_log("Succès: reinitialisation de l'affichage.")
    elif x in list_math_operator:
        file_log("Succès: reconnaissance du bouton.")
        x += "("
        calculate += str(x)
        equation.set(calculate)
    else:
        file_log("Succès: reconnaissance du bouton.")
        try:
            calculate += str(x)
            equation.set(calculate)
        except Exception as err:
            messagebox.showerror("Echec", f" error: {err} ")
            file_log("Echec: Calcul impossible.", "error")
            calculate = ""
            file_log("Succès: réinitialisation du calcul.")


def path_result(path_folder, name, final):
    """Function that catch and get the file name and folder path to write the results.

        :param path_folder: Path of the folder.
        :type: string
        :param name: Name of the file.
        :type: string
        :param final: Result of the user's equation.
        :type: string
        :return: Write the result in a file chosen by the user, and generate log.
        :rtype: void
        """
    file_log("Succès: lancement de la phase d'écriture du fichier.")
    name += ".txt"
    full_path = join(path_folder + sep, name)
    try:
        if os.name is not "nt":
            file_log(f"Droits sur dossier: {filemode(path_folder)}.")
        makedirs(path_folder, exist_ok=True)
        file_log("Succès: création/récupération du dossier.")
        with open(full_path, 'a') as w_file:
            w_file.write('\n***Nouveau Résultat***\n')
            w_file.write(str(final))
        file_log("Succès: écriture du fichier.")
    except Exception as err:
        messagebox.showerror("Echec", err)
        file_log(f"Echec: erreur au moment de l'écriture du fichier:\n\t{err}"
                 ".", "error")


def use_db(req=None, value=None, path=None):
    """This function create a database in sqLite3 to keep the results.

    :return: Create a database.
    :rtype: void
    """
    db_path = join(default_folder + sep, "my_db.sqlite")
    resultats = connect(db_path)

    if req is not None:
        # create the table in sqLite3
        rslt = resultats.cursor()
        query = '''CREATE TABLE IF NOT EXISTS results(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        result TEXT NOT NULL,
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);'''
        rslt.execute(query)
        resultats.commit()
        # Insert the data
        if req is "insert":
            rslt = resultats.cursor()
            insert = '''INSERT INTO results(result, date) 
                            VALUES (?, ?);'''
            rslt.execute(insert, (value, datetime.now()))
            resultats.commit()
        # Get the data and write it in the file
        if req is "fetch":
            rslt = resultats.cursor()
            with open(path, 'a') as w_file:
                w_file.write('\nid | '.rjust(0))
                w_file.write('resultats     | '.rjust(5))
                w_file.write('dates      | '.rjust(10))
                w_file.write('moment'.rjust(13))
                w_file.write('\n' + ("-" * 55))
                rslt.execute('SELECT * FROM results;')
                for r in rslt.fetchall():
                    row = " ".join(str(x) for x in r)
                    rid, rres, rdate, rmoment = row.split()
                    rid += " | "
                    rdate = " | " + rdate + " | "
                    w_file.write('\n' + rid + rres.rjust(10) + rdate.rjust(20)
                                 + rmoment)
    resultats.close()


# create main window
main_screen = Tk()
main_screen.title('Ma calculatrice python')
file_log("Succès: création de la fenêtre principale.")
main_screen.bind("<Any-KeyPress>", exit_calc)

# create main block
main_cadre = Frame(main_screen, width=280, height=250,
                   borderwidth=1, bg="red")
main_cadre.pack(fill=BOTH)
file_log("Succès: création du cadre principal.")

# create display block
display_cadre = Frame(main_cadre, width=280, height=30, borderwidth=1)
display_cadre.pack(fill='x', side='top')
file_log("Succès: création du cadre d'affichage.")

# create buttons block
little_button_cadre = Frame(main_cadre, width=280, height=100, borderwidth=1)
little_button_cadre.pack(fill='x')
file_log("Succès: création du cadre de touches.")

# create configuration block
entries_cadre = LabelFrame(main_cadre, width=280, height=60, borderwidth=1,
                           text="Configuration du stockage des résultats")
entries_cadre.pack(fill='x', side='bottom')
file_log("Succès: création du cadre de configuration.")

# create display screen and input
equation = StringVar()
expression_field = Entry(display_cadre, textvariable=equation)
expression_field.pack(side="top", fill=BOTH, ipady=15)
equation.set(default_text)
expression_field.config(font=("Courier", 20))
expression_field.bind("<Any-KeyPress>", on_event)
file_log("Succès: création de la zone de saisie d'affichage.")

# create folder path input
file_path = StringVar()
folder = Entry(entries_cadre, textvariable=file_path, width=30)
file_path.set(default_folder)
folder.pack(side='top', fill='x')
file_log("Succès: création de la zone de saisie du dossier.")

# create file name input
file_name = StringVar()
file = Entry(entries_cadre, textvariable=file_name, width=30)
file_name.set(default_file)
file.pack(side='bottom', fill='x')
file_log("Succès: création de la zone de saisie du nom du fichier.")

# Create and link buttons
b_1 = Button(little_button_cadre,
             text="1",
             command=lambda: b_click("1"),
             bg="#98DB9C",
             fg="black",
             activebackground="white",
             activeforeground="black",
             height="5",
             width="10",
             padx="1",
             pady="1").grid(row=3, column=1)
b_2 = Button(little_button_cadre,
             text="2",
             bg="#98DB9C",
             fg="black",
             command=lambda: b_click("2"),
             activebackground="white",
             activeforeground="black",
             height="5",
             width="10",
             padx="1",
             pady="1").grid(row=3, column=2)
b_3 = Button(little_button_cadre,
             text="3",
             bg="#98DB9C",
             fg="black",
             command=lambda: b_click("3"),
             activebackground="white",
             activeforeground="black",
             height="5",
             width="10",
             padx="1",
             pady="1").grid(row=3, column=3)
b_4 = Button(little_button_cadre,
             text="4",
             bg="#98DB9C",
             fg="black",
             command=lambda: b_click("4"),
             activebackground="white",
             activeforeground="black",
             height="5",
             width="10",
             padx="1",
             pady="1").grid(row=4, column=1)
b_5 = Button(little_button_cadre,
             text="5",
             bg="#98DB9C",
             fg="black",
             command=lambda: b_click("5"),
             activebackground="white",
             activeforeground="black",
             height="5",
             width="10",
             padx="1",
             pady="1").grid(row=4, column=2)
b_6 = Button(little_button_cadre,
             text="6",
             bg="#98DB9C",
             fg="black",
             command=lambda: b_click("6"),
             activebackground="white",
             activeforeground="black",
             height="5",
             width="10",
             padx="1",
             pady="1").grid(row=4, column=3)
b_7 = Button(little_button_cadre,
             text="7",
             bg="#98DB9C",
             fg="black",
             command=lambda: b_click("7"),
             activebackground="white",
             activeforeground="black",
             height="5",
             width="10",
             padx="1",
             pady="1").grid(row=5, column=1)
b_8 = Button(little_button_cadre,
             text="8",
             bg="#98DB9C",
             fg="black",
             command=lambda: b_click("8"),
             activebackground="HotPink",
             activeforeground="black",
             height="5",
             width="10",
             padx="1",
             pady="1").grid(row=5, column=2)
b_9 = Button(little_button_cadre,
             text="9",
             bg="#98DB9C",
             fg="black",
             command=lambda: b_click("9"),
             activebackground="white",
             activeforeground="black",
             height="5",
             width="10",
             padx="1",
             pady="1").grid(row=5, column=3)
b_0 = Button(little_button_cadre,
             text="0",
             bg="#98DB9C",
             fg="black",
             command=lambda: b_click("0"),
             activebackground="white",
             activeforeground="black",
             height="5",
             width="10",
             padx="1",
             pady="1").grid(row=6, column=2)
b_coma = Button(little_button_cadre,
                text=",",
                bg="#98DB9C",
                fg="black",
                command=lambda: b_click("."),
                activebackground="white",
                activeforeground="black",
                height="5",
                width="10",
                padx="1",
                pady="1").grid(row=6, column=1)
b_opar = Button(little_button_cadre,
                text="(",
                bg="#98DB9C",
                fg="black",
                command=lambda: b_click("("),
                activebackground="white",
                activeforeground="black",
                height="5",
                width="10",
                padx="1",
                pady="1").grid(row=1, column=2)
b_cpar = Button(little_button_cadre,
                text=")",
                bg="#98DB9C",
                fg="black",
                command=lambda: b_click(")"),
                activebackground="white",
                activeforeground="black",
                height="5",
                width="10",
                padx="1",
                pady="1").grid(row=1, column=3)
b_add = Button(little_button_cadre,
               text="+",
               bg="#00734F",
               fg="white",
               command=lambda: b_click("+"),
               activebackground="white",
               activeforeground="black",
               height="5",
               width="10",
               padx="1",
               pady="1").grid(row=2, column=2)
b_minus = Button(little_button_cadre,
                 text="-",
                 bg="#00734F",
                 fg="white",
                 command=lambda: b_click("-"),
                 activebackground="white",
                 activeforeground="black",
                 height="5",
                 width="10",
                 padx="1",
                 pady="1").grid(row=2, column=1)
b_multiply = Button(little_button_cadre,
                    text="×",
                    bg="#00734F",
                    fg="white",
                    command=lambda: b_click("*"),
                    activebackground="white",
                    activeforeground="black",
                    height="5",
                    width="10",
                    padx="1",
                    pady="1").grid(row=2, column=4)
b_divide = Button(little_button_cadre,
                  text="/",
                  bg="#00734F",
                  fg="white",
                  command=lambda: b_click("/"),
                  activebackground="white",
                  activeforeground="black",
                  height="5",
                  width="10",
                  padx="1",
                  pady="1").grid(row=2, column=3)
b_sqrt = Button(little_button_cadre,
                text="√",
                bg="#2B2E2A",
                fg="white",
                command=lambda: b_click("sqrt"),
                activebackground="white",
                activeforeground="black",
                height="5",
                width="10",
                padx="1",
                pady="1").grid(row=3, column=4)
b_pow = Button(little_button_cadre,
               text="^",
               bg="#2B2E2A",
               fg="white",
               command=lambda: b_click("pow"),
               activebackground="white",
               activeforeground="black",
               height="5",
               width="10",
               padx="1",
               pady="1").grid(row=3, column=5)
b_is = Button(little_button_cadre,
              text="=",
              bg="#00734F",
              fg="white",
              command=lambda: b_click("="),
              activebackground="white",
              activeforeground="black",
              height="5",
              width="10",
              padx="1",
              pady="1").grid(row=6, column=3)
b_pi = Button(little_button_cadre,
              text="π",
              bg="#415E53",
              fg="white",
              command=lambda: b_click("pi"),
              activebackground="white",
              activeforeground="black",
              height="5",
              width="10",
              padx="1",
              pady="1").grid(row=1, column=4)
b_infinite = Button(little_button_cadre,
                    text="∞",
                    bg="#415E53",
                    fg="white",
                    command=lambda: b_click("inf"),
                    activebackground="white",
                    activeforeground="black",
                    height="5",
                    width="10",
                    padx="1",
                    pady="1").grid(row=1, column=5)
b_log = Button(little_button_cadre,
               text="Log",
               bg="#2B2E2A",
               fg="white",
               command=lambda: b_click("log"),
               activebackground="white",
               activeforeground="black",
               height="5",
               width="10",
               padx="1",
               pady="1").grid(row=2, column=5)
b_sin = Button(little_button_cadre,
               text="Sin",
               bg="#2B2E2A",
               fg="white",
               command=lambda: b_click("sin"),
               activebackground="white",
               activeforeground="black",
               height="5",
               width="10",
               padx="1",
               pady="1").grid(row=4, column=4)
b_asin = Button(little_button_cadre,
                text="aSin",
                bg="#2B2E2A",
                fg="white",
                command=lambda: b_click("asin"),
                activebackground="white",
                activeforeground="black",
                height="5",
                width="10",
                padx="1",
                pady="1").grid(row=4, column=5)
b_cos = Button(little_button_cadre,
               text="Cos",
               bg="#2B2E2A",
               fg="white",
               command=lambda: b_click("cos"),
               activebackground="white",
               activeforeground="black",
               height="5",
               width="10",
               padx="1",
               pady="1").grid(row=5, column=4)
b_acos = Button(little_button_cadre,
                text="aCos",
                bg="#2B2E2A",
                fg="white",
                command=lambda: b_click("acos"),
                activebackground="white",
                activeforeground="black",
                height="5",
                width="10",
                padx="1",
                pady="1").grid(row=5, column=5)
b_tan = Button(little_button_cadre,
               text="Tan",
               bg="#2B2E2A",
               fg="white",
               command=lambda: b_click("tan"),
               activebackground="white",
               activeforeground="black",
               height="5",
               width="10",
               padx="1",
               pady="1").grid(row=6, column=4)
b_atan = Button(little_button_cadre,
                text="aTan",
                bg="#2B2E2A",
                fg="white",
                command=lambda: b_click("atan"),
                activebackground="white",
                activeforeground="black",
                height="5",
                width="10",
                padx="1",
                pady="1").grid(row=6, column=5)
b_clear = Button(little_button_cadre,
                 text="C",
                 bg="#CF4024",
                 fg="white",
                 command=lambda: b_click("C"),
                 activebackground="white",
                 activeforeground="black",
                 height="5",
                 width="10",
                 padx="1",
                 pady="1").grid(row=1, column=1)
file_log("Succès: création des boutons.")


if __name__ == '__main__':
    use_db()
    main_screen.mainloop()
    file_log("Succès: lancement de l'interface graphique.")
    try:
        cleaning_folder()
        file_log("Succès: nettoyage des log obsolètes.")
    except Exception as e:
        file_log(f"Echec: nettoyage des log obsolètes:\n{e}.", "error")
