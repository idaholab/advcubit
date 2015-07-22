""" module for sidesets and nodesets
"""

import advcubit.system_module as _system
import advcubit.function_module as _functions


def createSideset(entities, sidesetId):
    """ Create a side set

    :param entities: list of entities to assign to side set
    :param sidesetId: the id number of the sideset
    :return: None
    """
    _system.cubitCmd('sideset {0} {1[0]} {1[1]}'.format(sidesetId, _functions.listIdString(entities)))


def nameSideset(sidesetId, name):
    """ Assign a name to a sideset

    :param sidesetId: the number of the sideset
    :param name: the name to be assigned
    :return: None
    """
    _system.cubitCmd('sideset {0} name "{1}"'.format(sidesetId, name))


def createNodeset(entities, nodesetId):
    """ Adds entities to or creates node set

    :param entities: list of entities
    :param bodyType: type of entities
    :return: None
    """
    _system.cubitCmd('nodeset {0} {1[0]} {1[1]}'.format(nodesetId, _functions.listIdString(entities)))


def nameNodeset(nodesetId, name):
    """ Assign a name to a node set

    :param nodesetId: the number of the node set
    :param name: the name to be assigned
    :return: None
    """
    _system.cubitCmd('nodeset {0} name "{1}"'.format(nodesetId, name))
