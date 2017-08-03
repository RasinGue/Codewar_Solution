def printer_error(s):
    length = len(s)
    errors = 0
    for c in s:
        if c > 'm' and c <= 'z':
            errors = errors + 1
    string = str(errors) + "/" + str(length)
    return string

from re import sub

def printer_error2(s):
    return "{}/{}".format(len(sub("[a-m]", '', s)), len(s))

print(printer_error2("abcdefzdd"))