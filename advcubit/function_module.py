"""
Provides general utility functions
"""

import advcubit.common_module as _common
import advcubit.system_module as _system


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


def getBodyType(cubitObject):
    """ Obtain the body type of an object

    :return: body type
    """
    if not isinstance(cubitObject, _system.cubitModule.GeomEntity):
        raise _system.AdvCubitException('Object is not a Cubit geometric entity')

    if isinstance(cubitObject, _system.cubitModule.Body):
        return _common.BodyTypes.body
    elif isinstance(cubitObject, _system.cubitModule.Volume):
        return _common.BodyTypes.volume
    elif isinstance(cubitObject, _system.cubitModule.Surface):
        return _common.BodyTypes.surface
    elif isinstance(cubitObject, _system.cubitModule.Curve):
        return _common.BodyTypes.curve
    elif isinstance(cubitObject, _system.cubitModule.Vertex):
        return _common.BodyTypes.vertex
    else:
        raise _system.AdvCubitException('Unknown Cubit body type')


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
        if objects is None:
            strList = ' all'
        else:
            strList = ' {0}'.format(objects)
    return strList


def listIdString(objects, requiredType=None):
    """ create a string of object ids from a list or single object
    :param objects: single object or list, None gives 'all'
    :param requiredType: type necessary to be in list
    :return: id list string
    """
    try:                                        # try list
        strList = ''
        bodyType = requiredType
        for item in objects:
            tmpBodyType = getBodyType(item)
            strList += ' {0}'.format(item.id())

            # test the body type we obtained
            if requiredType is not None:
                if tmpBodyType != requiredType:
                    raise _system.AdvCubitException('Cubit entity does not match required type')
            elif bodyType is not None and tmpBodyType != bodyType:
                raise _system.AdvCubitException('List contains more then one body type')
    except TypeError:                           # catch single item
        if objects is None:
            strList = ' all'
        else:
            bodyType = getBodyType(objects)
            strList = ' {0}'.format(objects.id())
    return bodyType, strList


def listKeywordString(kargs):
    """ create list string of keyword arguments
    :param kargs: keyword dict
    :return: string of keyword arguments
    """
    strList = ''
    for key, value in kargs.items():
        strList += ' {0} {1}'.format(key, value)
    return strList
