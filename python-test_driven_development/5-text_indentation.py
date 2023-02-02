#!/usr/bin/python3
'''Module to prints a text'''


def text_indentation(text):
    '''
    Print a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): text to be printed

    Raises:
        TypeError: If text is not str

    Returns:
        Nothing
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    start = 0
    for i in text:
        if start == 0:
            if i == ' ':
                continue
            else:
                start = 1

        if start == 1:
            if i == '.' or i == '?' or i == ':':
                print('{:s}\n'.format(i))
                start = 0
            else:
                print(i, end='')

