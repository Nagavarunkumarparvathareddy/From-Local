from ExceptionCreation import ConvertError
def integer(val):
    if val.isdigit():
        return int(val)
    elif val[0] == '-':
        if val[1:].isdigit():
            return int(val)
        else:
            raise ConvertError
    else:
        raise ConvertError