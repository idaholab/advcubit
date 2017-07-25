""" Transformation operations
"""

import advcubit.system_module as _system
import advcubit.function_module as _functions


def getLastBody():
    """ Retrieve the last created body

    :return: The last body created within Cubit
    """
    lastId = _system.cubitWrapper.get_last_id('body')

    try:
        return _system.cubitWrapper.body(lastId)
    except RuntimeError as e:
        raise _system.AdvCubitException('Cannot retrieve last created body:\n' + str(e))


def delete(entities):
    """ Delete a list or single entity

    :param entities: the entity or list of entities to be deleted
    :return: None
    """
    _system.cubitCmd('delete {0[0]} {0[1]}'.format(_functions.listIdString(entities)))


def rotate(entities, angle, axis='z', *args, **kwargs):
    """ Rotate a entity
    :param entities: the entity or list of entities
    :param angle: angle in degrees
    :param axis: coordinate system axis x, y, z
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('rotate {0[0]} {0[1]} angle {1} about {2} {3} {4}'.format(_functions.listIdString(entities),
                                                                               angle, axis,
                                                                               _functions.listStr(args),
                                                                               _functions.listKeywordString(kwargs)))


def webcut(entities, plane='x', offset=0, *args, **kwargs):
    """
    :param entities: entities or single one to cut
    :param plane: plane: x, y, z
    :param offset: offset from origin
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd(
        'webcut {0[0]} {0[1]} with plane {1}plane offset {2} {3} {4}'.format(_functions.listIdString(entities),
                                                                             plane, offset,
                                                                             _functions.listStr(args),
                                                                             _functions.listKeywordString(kwargs)))


def sectionCut(entities, plane='x', *args, **kwargs):
    """ Section cut a entity or list of entities
    :param entities: the entity or a list of entities
    :param plane: plane to cut at: x, y, z
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('section {0[0]} {0[1]} {1}plane {2} {3}'.format(_functions.listIdString(entities), plane,
                                                                     _functions.listStr(args),
                                                                     _functions.listKeywordString(kwargs)))


def copyReflect(entities, plane='x', *args, **kwargs):
    """ Reflect and copy a list of entities

    :param entities: list or single base entity
    :param plane: reflection plane x, y, z
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: created entity
    """
    # TODO get list of entities back
    _system.cubitCmd('{0[0]} {0[1]} copy reflect {1} {2} {3}'.format(_functions.listIdString(entities), plane,
                                                                     _functions.listStr(args),
                                                                     _functions.listKeywordString(kwargs)))
    return getLastBody()


def move(entities, vector):
    """ Move a list of entities at once

    :param entities: list of entities or single entity
    :param vector: move vector in vector/list form
    :return: None
    """
    try:
        for entity in entities:
            _system.cubitWrapper.move(entity, vector)
    except TypeError:
        _system.cubitWrapper.move(entities, vector)


def copy(entities):
    """ Copy a list of entities

    :param entities: List of entities or single entity
    :return: List of copied entities or single entity
    """

    bodies = []
    try:
        for entity in entities:
            bodies.append(_system.cubitWrapper.copy_body(entity))
    except TypeError:
        bodies = _system.cubitWrapper.copy_body(entities)

    return bodies
