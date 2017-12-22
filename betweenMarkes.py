def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    lBegin = len(begin)
    sBegin = (text.find(begin))
    sEnd = (text.find(end))


    if sBegin >= 0 and sEnd >= 0:
        if (sEnd - sBegin) > 0:
            sBegin += lBegin
            return text[sBegin : sEnd]

    if sBegin >= 0 and sEnd < 0:
        sBegin += lBegin
        return (text[sBegin:])


    if sBegin < 0 and sEnd >= 0:
        return (text[: sEnd])

    if sBegin < 0 and sEnd < 0:
        return text

    else:
        return ''



if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    #These "asserts" are used for self-checking and not for testing
    assert between_markers("Never send a human to do a machine's job.", "Never", "do")
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')