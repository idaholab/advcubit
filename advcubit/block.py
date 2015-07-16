""" Module for block operations
"""

import advcubit.system as _system
import advcubit.common as _common
import advcubit.functions as _functions


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


def createBlock(bodies, blockId, bodyType=_common.BodyTypes.volume):
    """ Assign a body to a block

    :param bodies: the body or list of bodies to be assigned
    :param blockId: the block id
    :param bodyType: the body type
    :return: None
    """
    _system.cubitCmd('block {0} {1} {2}'.format(blockId, bodyType, _functions.listIdString(bodies)))


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