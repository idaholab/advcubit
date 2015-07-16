""" Module providing boolean operations
"""

import advcubit.system as _system
import advcubit.transform as _transform
import advcubit.functions as _functions


def subtract(tool_in, from_in, imprint_in=False, keep_old_in=False):
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


def intersect(bodies, *args, **kargs):
    """ Create the logical AND of bodies

    :param bodies: list of bodies
    :return: intersected body
    """
    _system.cubitCmd('intersect body {0}'.format(_functions.listIdString(bodies)))
    return _transform.getLastBody()
