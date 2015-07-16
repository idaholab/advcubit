"""
Provides general utility functions
"""


def roundTuple(baseTuple, prec=2, tupleType=tuple):
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


def checkZero(baseTuple, prec=1e-15, tupleType=tuple):
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


def listStr(objects):
    """ create a string with all objects
    :param objects: single object or list
    :return: list string
    """
    try:                                        # try list
        strList = ''
        for item in objects:
            strList += ' {0}'.format(item)
    except TypeError:                           # catch single item
        strList = ' {0}'.format(objects)
    return strList


def listIdString(objects):
    """ create a string of object ids from a list or single object
    :param objects: single object or list
    :return: id list string
    """
    try:                                        # try list
        strList = ''
        for item in objects:
            strList += ' {0}'.format(item.id())
    except TypeError:                           # catch single item
        strList = ' {0}'.format(objects.id())
    return strList


def listKeywordString(kargs):
    """ create list string of keyword arguments
    :param kargs: keyword dict
    :return: string of keyword arguments
    """
    strList = ''
    for key, value in kargs.items():
        strList += ' {0} {1}'.format(key, value)
    return strList
