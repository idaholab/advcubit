""" Module for block operations
"""

import advcubit.system_module as _system
import advcubit.common_module as _common
import advcubit.function_module as _functions


class SurfaceElementTypes:
    """ Enum class for surface element types
    """
    QUAD4 = 'QUAD4'
    QUAD5 = 'QUAD5'
    QUAD8 = 'QUAD8'
    QUAD9 = 'QUAD9'

    TRI3 = 'TRI3'
    TRI6 = 'TRI6'
    TRI7 = 'TRI7'


class VolumeElementTypes:
    """ Enum class for volume element types
    """
    HEX8 = 'HEX8'
    HEX9 = 'HEX9'
    HEX20 = 'HEX20'
    HEX27 = 'HEX27'

    WEDGE6 = 'WEDGE6'
    WEDGE15 = 'WEDGE15'


def createBlock(entities, blockId):
    """ Assign a entity to a block

    :param entities: the entity or list of entities to be assigned
    :param blockId: the block id
    :return: None
    """
    _system.cubitCmd('block {0} add {1[0]} {1[1]}'.format(blockId, _functions.listIdString(entities)))


def createBlockFromElements(blockId, elementType, objects=None):
    """ Create a block with elements, limiting it to a specific entity
    :param blockId: the block id
    :param elementType: the element type, eg. hex
    :param objects: list or single element id or entity ids
    :return: None
    """
    try:
        idList = _functions.listIdString(objects)
        if idList[0] == _common.BodyTypes.body:
            idList = _functions.listIdString(_functions.getEntitiesFromObject(objects, _common.BodyTypes.volume))
        cmdStr = 'block {0} {1} in {2[0]} {2[1]}'.format(blockId, elementType, idList)
    except _system.AdvCubitException:
        cmdStr = 'block {0} {1} {2}'.format(blockId, elementType, _functions.listStr(objects))
    _system.cubitCmd(cmdStr)


def setElementType(blockId, elementType):
    """ Set block element type

    :param blockId: Id number of block
    :param elementType: Element type from enum ElementType
    :return: None
    """
    _system.cubitCmd('block {0} element type {1}'.format(blockId, elementType))


def nameBlock(blockId, name):
    """ Assign a name to a block

    :param blockId: number of block
    :param name: block name
    :return: None
    """
    _system.cubitCmd('block {0} name "{1}"'.format(blockId, name))
