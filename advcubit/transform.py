""" Transformation operations
"""

import advcubit.system as _system
import advcubit.common as _common
import advcubit.functions as _functions


def getLastBody():
    """ Retrieve the last created body

    :return: The last body created within Cubit
    """
    lastId = _system.cubitModule.get_last_id('body')

    try:
        return _system.cubitModule.body(lastId)
    except RuntimeError as e:
        raise _system.AdvCubitException('Cannot retrieve last created body:\n' + str(e))


def delete(bodies, blockType=_common.BodyTypes.body):
    """ Delete a body

    :param body: the body or list of bodies to be deleted
    :param blockType: the body type
    :return: None
    """
    _system.cubitCmd('delete {0} {1}'.format(blockType, _functions.listIdString(bodies)))


def rotate(body, angle, axis='z', *args, **kwargs):
    """ Rotate a body
    :param body: the body
    :param angle: angle in degrees
    :param axis: coordinate system axis x, y, z
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('rotate body {0} angle {1} about {2} {3} {4}'.format(body.id(), angle, axis,
                                                                          _functions.listStr(args),
                                                                          _functions.listKeywordString(kwargs)))


def webcut(body, plane='x', offset=0, *args, **kwargs):
    """
    :param body: body to cut
    :param plane: plane: x, y, z
    :param offset: offset from origin
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd(
        'webcut body {0} with plane {1}plane offset {2} {3} {4}'.format(body.id(), plane, offset,
                                                                        _functions.listStr(args),
                                                                        _functions.listKeywordString(kwargs)))


def sectionCut(bodies, plane='x', *args, **kwargs):
    """ Section cut a body or list of bodies
    :param bodies: the body
    :param plane: plane to cut at: x, y, z
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('section body {0} {1}plane'.format(_functions.listIdString(bodies), plane,
                                                        _functions.listStr(args),
                                                        _functions.listKeywordString(kwargs)))


def copyReflect(bodies, plane='x', *args, **kwargs):
    """ Reflect and copy a body

    :param bodies: list or single base body
    :param plane: reflection plane x, y, z
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: created body
    """
    # TODO get list of bodies back
    _system.cubitCmd('body {0} copy reflect {1}'.format(_functions.listIdString(bodies), plane,
                                                        _functions.listStr(args),
                                                        _functions.listKeywordString(kwargs)))
    return getLastBody()


def move(bodies, vector):
    """ Move a list of bodies at once

    :param bodies: list of bodies or single body
    :param vector: move vector in vector/list form
    :return: None
    """
    try:
        for body in bodies:
            _system.cubitModule.move(body, vector)
    except TypeError:
        _system.cubitModule.move(bodies, vector)
