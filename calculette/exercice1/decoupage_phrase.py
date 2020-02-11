#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Ce module découpe les phrases saisies par un utilisateur dans une liste."""


def catch_sentence():
    """Function which catch the sentence of the user.

    :return: return the user's sentence.
    :rtype: string
    :raise Exception: when input problem

    :Example:

    >>> catch_sentence()
    Saisissez votre phrase: 'my sentence'

    .. seealso:: split_sentence(), main()
    """
    try:
        # Catch the user's sentence
        user_sentence = input("Saisissez votre phrase:")
        return user_sentence
    except Exception as e:
        # If it isn't possible, tell why
        print(f'Erreur: {e}')
        catch_sentence()


def split_sentence(user_sentence):
    """Function which split the sentence in a list.

    :param user_sentence: the user's sentence.
    :type: string
    :return: return the splited sentence in a list.
    :rtype: list
    :raise Exception: when the sentence can't be splited.

    :Example:

    >>> split_sentence('my sentence')
    [my, sentence]

    .. seealso:: catch_sentence(), main()
    """
    try:
        # Split the sentence in a list
        splited_sentence = user_sentence.split()
        return splited_sentence
    except Exception as e:
        # If it isn't possible, tell why
        print(f'Erreur: {e}')


# Launch the functions
def main():
    """Run the functions

    :return: the user's sentence splited in a list.
    :rtype: list

    :Example:

    >>> catch_sentence()
    Saisissez votre phrase: 'my sentence'
    >>> split_sentence('my sentence')
    [my, sentence]

    .. seealso:: catch_sentence(), split_sentence()
    """
    sentence = catch_sentence()
    sentence_in_list = split_sentence(sentence)

    # Display the result in the console
    print(sentence_in_list)


if __name__ == "__main__":
    main()
