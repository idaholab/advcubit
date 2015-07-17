""" module for sidesets and nodesets
"""

import advcubit.system_module as _system
import advcubit.common_module as _common


def createSideset(bodies, sidesetId, bodyType=_common.BodyTypes.surface):
    """ Create a side set

    :param bodies: list of bodies to assign to side set
    :param sidesetId: the id number of the sideset
    :param bodyType: the type of the bodies
    :return:
    """
    tmpStr = ''
    for body in bodies:
        tmpStr += ' {0}'.format(body.id())
    _system.cubitCmd('sideset {0} {1} {2}'.format(sidesetId, bodyType, tmpStr))


def nameSideset(sidesetId, name):
    """ Assign a name to a sideset

    :param sidesetId: the number of the sideset
    :param name: the name to be assigned
    :return: None
    """
    _system.cubitCmd('sideset {0} name "{1}"'.format(sidesetId, name))


def createNodeset(bodies, nodesetId, bodyType=_common.BodyTypes.vertex):
    """ Adds bodies to or creates node set

    :param bodies: list of bodies
    :param nodesetId: number for new/existing node set
    :param bodyType: type of bodies
    :return: None
    """
    tmpStr = ''
    for body in bodies:
        tmpStr += ' {0}'.format(body.id())
    _system.cubitCmd('nodeset {0} {1} {2}'.format(nodesetId, bodyType, tmpStr))


def nameNodeset(nodesetId, name):
    """ Assign a name to a node set

    :param nodesetId: the number of the node set
    :param name: the name to be assigned
    :return: None
    """
    _system.cubitCmd('nodeset {0} name "{1}"'.format(nodesetId, name))
