"""
Provides general utility functions
"""


def roundTuple(baseTuple, prec = 2, tupleType = tuple):
    """ Round a tuple

    :param baseTuple: input tuple
    :param prec: numer of digits
    :param tupleType: type of final tuple
    :return: rounded tuple of type tupleType
    """
    rounded = []
    for item in baseTuple:
        rounded.append(round(item, prec))
    return tupleType(rounded)


def checkZero(baseTuple, prec = 1e-15, tupleType = tuple):
    """ Check for numerical issues and set them to zero

    :param baseTuple: input tuple
    :param prec: abs value of zero
    :param tupleType: type of final tuple
    :return: zerod tuple of type tupleType
    """
    zeroed = []
    for item in baseTuple:
        if abs(item) < prec:
            item = 0.0
        zeroed.append(item)
    return tupleType(zeroed)
