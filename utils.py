class Utils:
    def __init__(self):
        pass

    # map alphabets to digits, so as to use as array index
    @staticmethod
    def get_rev_alpha():
        _alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return dict([(x[1], x[0] + 1) for x in enumerate(_alphabets)])

    # convert to uppercase
    @staticmethod
    def convert_to_upper(val):
        if isinstance(val, list):
            return [i.upper() for i in val]
        elif isinstance(val, str):
            return val.upper()
