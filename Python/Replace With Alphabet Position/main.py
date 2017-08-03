def alphabet_position(text):
    text = text.lower()
    l = []
    for c in text:
        if c >'z' or c < 'a':
            continue
        l.append(ord(c) - 96)
    l = map(str, l)
    string = " ".join(l)
    return string

def alphabet_position2(text):
    return " ".join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


print(alphabet_position("The sunset sets at twelve o' clock."))