#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Runtime Complexity: θ(n) Space Complexity: θ(1)
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # if index is found in text, return true
    # otherwise return false
    return find_index(text, pattern) is not None


def find_index(text, pattern, start=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Runtime Complexity: θ(n) Space Complexity: θ(1)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # we need two variables to keep track of what
    # index we are at in the pattern and how many
    # characters of pattern have been matched consecutively
    patternIndex = 0
    matchedCount = 0

    # loop through characters in text
    for textIndex in range(start, len(text)):

        # handle the special case of an empty string pattern
        if len(pattern) == 0:
            return textIndex

        # increment pattern count and index if current character
        # in pattern matches current character in text
        if text[textIndex] == pattern[patternIndex]:
            matchedCount += 1
            patternIndex += 1

        # if there is overlap, restart the pattern count and index at 1
        elif text[textIndex] == pattern[0]:
            patternIndex = 1
            matchedCount = 1

        # otherwise restart the pattern count and index at 0
        else:
            patternIndex = 0
            matchedCount = 0

        # once the pattern count becomes equal to length of pattern
        # we have a match - return the starting index
        if matchedCount >= len(pattern):
            return textIndex - matchedCount+1

    # return None if index was not found
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Runtime Complexity: θ(n) Space Complexity: θ(1)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # result list for starting indexes of windows that
    # match the pattern
    resultingIndices = []

    resultingIndex = 0
    # loop until we get None for the resultingIndex
    while resultingIndex is not None:
        resultingIndex = find_index(text, pattern, resultingIndex)
        if resultingIndex is not None:
            resultingIndices.append(resultingIndex)
            resultingIndex += 1

    # return resulting list of indices
    return resultingIndices


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
