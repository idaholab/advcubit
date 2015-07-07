""" Module providing boolean operations
"""

import advcubit.system as _system
import advcubit.transform as _transform


def subtract(tool_in, from_in, imprint_in = False, keep_old_in = False):
    """ Provides a bug fix for subtract in Cubit 13.1

    :param tool_in: list of bodies to be subtracted
    :param from_in: list of base bodies
    :param imprint_in: flag to imprint
    :param keep_old_in: flag to keep original bodies
    :return:
    """
    for body in tool_in:
        from_in = _system.cubitModule.subtract([body], from_in, imprint_in, keep_old_in)

    return from_in


def intersect(bodies):
    """ Create the logical AND of bodies

    :param bodies: list of bodies
    :return: intersected body
    """
    tmpStr = 'intersect body '
    for body in bodies:
        tmpStr += '{0} '.format(body.id())
    _system.cubitCmd(tmpStr)
    return _transform.getLastBody()
