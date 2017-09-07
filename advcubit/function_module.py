"""
Provides general utility functions
"""

import advcubit.common_module as _common
import advcubit.system_module as _system


def roundTuple(baseTuple, prec=2, tupleType=tuple):
    """ Round a tuple

    :param baseTuple: input tuple
    :param prec: number of digits
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
    :return: zeroed tuple of type tupleType
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
    if not isinstance(cubitObject, _system.cubitWrapper.GeomEntity) \
            and not isinstance(cubitObject, _system.cubitWrapper.Body):
        raise _system.AdvCubitException('Object is not a Cubit geometric entity "{0}"'.format(cubitObject))

    if isinstance(cubitObject, _system.cubitWrapper.Body):
        return _common.BodyTypes.body
    elif isinstance(cubitObject, _system.cubitWrapper.Volume):
        return _common.BodyTypes.volume
    elif isinstance(cubitObject, _system.cubitWrapper.Surface):
        return _common.BodyTypes.surface
    elif isinstance(cubitObject, _system.cubitWrapper.Curve):
        return _common.BodyTypes.curve
    elif isinstance(cubitObject, _system.cubitWrapper.Vertex):
        return _common.BodyTypes.vertex
    else:
        raise _system.AdvCubitException('Unknown Cubit body type')


def getClass(entityType):
    """ Obtain reference to entity type class
    :param entityType: type of entity
    :return: reference to class
    """
    if entityType == _common.BodyTypes.vertex:
        return _system.cubitWrapper.Vertex
    elif entityType == _common.BodyTypes.curve:
        return _system.cubitWrapper.Curve
    elif entityType == _common.BodyTypes.surface:
        return _system.cubitWrapper.Surface
    elif entityType == _common.BodyTypes.volume:
        return _system.cubitWrapper.Volume
    elif entityType == _common.BodyTypes.body:
        return _system.cubitWrapper.Body
    else:
        raise _system.AdvCubitException('Unknown entity type "{0}"'.format(entityType))


def getTypeFct(entityType):
    """ Obtain the function to obtain a cubit entity by id
    :param entityType: type of entity
    :return: function reference
    """
    if entityType == _common.BodyTypes.vertex:
        return _system.cubitWrapper.vertex
    elif entityType == _common.BodyTypes.curve:
        return _system.cubitWrapper.curve
    elif entityType == _common.BodyTypes.surface:
        return _system.cubitWrapper.surface
    elif entityType == _common.BodyTypes.volume:
        return _system.cubitWrapper.volume
    elif entityType == _common.BodyTypes.body:
        return _system.cubitWrapper.body
    else:
        raise _system.AdvCubitException('Unknown entity type "{0}"'.format(entityType))


def getEntities(entityType, stringList='all'):
    """ Find all entities in current session of a type
    :param entityType: type of the entity to obtain
    :param stringList: cubit style list, default is all
    :return: list of cubit entities
    """
    ids = _system.cubitWrapper.parse_cubit_list(entityType, stringList)
    typeRef = getTypeFct(entityType)

    entityList = []
    for i in ids:
        entityList.append(typeRef(i))
    return entityList


def getSubEntities(cubitObject, entityType):
    """ Get all sub entities of one type for a single object
    :param cubitObject: single cubit entity
    :param entityType: entity type to obtain
    :return: list of sub entities
    """
    if entityType == _common.BodyTypes.body:
        tmpList = cubitObject.bodies()
    elif entityType == _common.BodyTypes.volume:
        tmpList = cubitObject.volumes()
    elif entityType == _common.BodyTypes.surface:
        tmpList = cubitObject.surfaces()
    elif entityType == _common.BodyTypes.curve:
        tmpList = cubitObject.curves()
    elif entityType == _common.BodyTypes.vertex:
        tmpList = cubitObject.vertices()
    else:
        raise _system.AdvCubitException('Unknown entity type "{0}"'.format(entityType))
    return tmpList


def getEntitiesFromObject(cubitObjects, entityType):
    """ Get all entities of a type from a single or a list of cubit objects
    :param cubitObjects: list or single cubit object
    :param entityType: the type of the entities
    :return: list of the sub entities
    """
    tmpList = []
    try:
        for item in cubitObjects:
            tmpList.extend(getSubEntities(item, entityType))
    except TypeError:
        tmpList = getSubEntities(cubitObjects, entityType)
    return tmpList


def listStr(objects):
    """ create a string with all objects
    :param objects: single object or list
    :return: list string
    """
    try:  # try list
        strList = ''
        for item in objects:
            strList += ' {0}'.format(item)
    except TypeError:  # catch single item
        if objects is None:
            strList = ' all'
        else:
            strList = ' {0}'.format(objects)
    return strList


def listIdString(objects, requiredType=None):
    """ create a string of object ids from a list or single object
    :param objects: single object or list, body type gives 'all' for body type
    :param requiredType: type necessary to be in list, None to ignore
    :return: id list string
    """
    if isinstance(objects, str):
        bodyType = objects
        strList = ' all'
    else:
        try:  # try list
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
                else:
                    bodyType = tmpBodyType
        except TypeError:  # catch single item
            bodyType = getBodyType(objects)
            strList = ' {0}'.format(objects.id())
    return bodyType, strList


def listKeywordString(kwargs):
    """ create list string of keyword arguments
    :param kwargs: keyword dict
    :return: string of keyword arguments
    """
    strList = ''
    for key, value in kwargs.items():
        strList += ' {0} {1}'.format(key, value)
    return strList


def searchOverlaps(entities):
    """ search for overlapping or touching objects
    :param entities: list of objects
    :return: list of pairs for overlapping objects
    """
    # get list of bounding boxes
    boxes = []
    for entity in entities:
        tmpBox = _system.cubitWrapper.get_bounding_box(getBodyType(entity), entity.id())
        boxes.append(((tmpBox[0], tmpBox[3], tmpBox[6]),
                      (tmpBox[1], tmpBox[4], tmpBox[7]),
                      entity))
    # sort by first dimension
    boxes.sort(key=lambda x: (x[0][0], -x[1][0], x[0][1], -x[1][1], x[0][2], -x[1][2]))

    # search for overlap
    pairs = []
    for i, item1 in enumerate(boxes[:-1]):
        for item2 in boxes[i + 1:]:
            if item1[1][0] < item2[0][0] or item1[0][0] > item1[1][0]:
                break
            if item1[1][1] < item2[0][1] or item1[0][1] > item1[1][1]:
                continue
            if item1[1][2] < item2[0][2] or item1[0][2] > item1[1][2]:
                continue

            pairs.append((item1[2], item2[2]))
    return pairs
