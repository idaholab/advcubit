""" Module containing methods for imprinting, merging and compressing

This module contains different methods for imprinting, e.g. all or curve on surface.
"""

import advcubit.system as _system


def compress():
    """ Compress cubit internal numbering

    :return: None
    """
    _system.cubitCmd('compress all')


def imprintAll():
    """ Unconditional imprint operations

    :return: None
    """
    _system.cubitCmd('imprint all')


def imprintTolerantAll():
    """ Unconditional tolerant imprint operation

    :return: None
    """
    _system.cubitCmd('imprint tolerant all')


def mergeAll():
    """ Unconditional merge command
    :return: None
    """
    _system.cubitCmd('merge all')


def imprintCurve(surface, curve):
    """ Imprint a curve onto a surface

    :param surface: Surface to imprint on
    :param curve: Curve to imprint
    :return: None
    """
    _system.cubitCmd('imprint surface {0} curve {1}'.format(surface.id(), curve.id()))


def imprint(bodies=None, bodyType='body'):
    """ Imprint a list of bodies

    :param bodies: list of bodies or None
    :param bodyType: type of bodies
    :return: None
    """
    if bodies is None:
        imprintAll()
    else:
        tmpStr = 'imprint {0}'.format(bodyType)
        for body in bodies:
            tmpStr += ' {0}'.format(body.id())
        _system.cubitCmd(tmpStr)


def merge(bodies=None, bodyType='body'):
    """ Merge a list of bodies

    :param bodies: list of bodies or None
    :param bodyType: type of bodies
    :return: None
    """
    if bodies is None:
        mergeAll()
    else:
        tmpStr = 'merge {0}'.format(bodyType)
        for body in bodies:
            tmpStr += ' {0}'.format(body.id())
        _system.cubitCmd(tmpStr)
