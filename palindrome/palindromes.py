#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
SKIP_CHARS = string.punctuation+string.whitespace


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):

    # remove punctuation and spaces from text
    # by using a translation table
    text = text.translate(str.maketrans('', '', SKIP_CHARS))

    # loop over characters, comparing first
    # character to last character - current index
    for index in range(1, len(text)-1//2):
        if (text[index-1].lower() != text[-index].lower()):
            return False

    # return True if all characters matched with their complement
    return True


def is_palindrome_recursive(text, left=None, right=None):

    # remove punctuation and spaces and
    # intialize left and right on first iteration
    if left is None or right is None:
        text = text.translate(str.maketrans('', '', SKIP_CHARS)).lower()
        left, right = 0, len(text)-1

    # once left is >= right we are done
    if left >= right:
        return True

    # if the character at the left doesn't match the one
    # on the right, return False
    if text[left] != text[right]:
        return False

    # otherwise keep going
    return is_palindrome_recursive(text, left+1, right-1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
