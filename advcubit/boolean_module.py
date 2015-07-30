""" Module providing boolean operations
"""

import advcubit.system_module as _system
import advcubit.transform_module as _transform
import advcubit.function_module as _functions


def subtract(tool_in, from_in, imprint_in=False, keep_old_in=False):
    """ Provides a bug fix for subtract in Cubit 13.1

    :param tool_in: list of bodies to be subtracted
    :param from_in: list of base bodies
    :param imprint_in: flag to imprint
    :param keep_old_in: flag to keep original bodies
    :return:
    """
    if not isinstance(from_in, (list, tuple)):
        from_in = [from_in]

    try:
        for body in tool_in:
            from_in = _system.cubitWrapper.subtract([body], from_in, imprint_in, keep_old_in)
    except TypeError:
        from_in = _system.cubitWrapper.subtract([tool_in], from_in, imprint_in, keep_old_in)

    return from_in


def intersect(bodies, *args, **kwargs):
    """ Create the logical AND of bodies

    :param bodies: list of bodies
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: intersected body
    """
    _system.cubitCmd('intersect {0[0]} {0[1]} {1} {2}'.format(_functions.listIdString(bodies),
                                                              _functions.listStr(args),
                                                              _functions.listKeywordString(kwargs)))
    return _transform.getLastBody()
