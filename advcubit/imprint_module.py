""" Module containing methods for imprinting, merging and compressing

This module contains different methods for imprinting, e.g. all or curve on surface.
"""

import advcubit.system_module as _system
import advcubit.common_module as _common
import advcubit.function_module as _functions


def compress():
    """ Compress cubit internal numbering

    :return: None
    """
    _system.cubitCmd('compress all')


def imprintAll(*args, **kwargs):
    """ Unconditional imprint operations

    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('imprint all {0} {1}'.format(_functions.listStr(args),
                                                  _functions.listKeywordString(kwargs)))


def imprintTolerantAll(*args, **kwargs):
    """ Unconditional tolerant imprint operation

    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('imprint tolerant all {0} {1}'.format(_functions.listStr(args),
                                                           _functions.listKeywordString(kwargs)))


def mergeAll(*args, **kwargs):
    """ Unconditional merge command

    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('merge all {0} {1}'.format(_functions.listStr(args),
                                                _functions.listKeywordString(kwargs)))


def imprintCurve(surface, curve, *args, **kwargs):
    """ Imprint a curve onto a surface

    :param surface: Surface to imprint on
    :param curve: Curve to imprint
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('imprint surface {0} curve {1[1]} {2} {3}'
                     .format(_functions.listIdString(surface, _common.BodyTypes.surface),
                             _functions.listIdString(curve, _common.BodyTypes.curve),
                             _functions.listStr(args),
                             _functions.listKeywordString(kwargs)))


def imprint(entities=None, *args, **kwargs):
    """ Imprint a list of bodies

    :param entities: list of bodies or None
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    if entities is None:
        imprintAll(*args, **kwargs)
    else:
        _system.cubitCmd('imprint {0[0]} {0[1]} {1} {2}'.format(_functions.listIdString(entities),
                                                                _functions.listStr(args),
                                                                _functions.listKeywordString(kwargs)))


def merge(entities=None, *args, **kwargs):
    """ Merge a list of bodies

    :param entities: list of bodies or None
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    if entities is None:
        mergeAll(*args, **kwargs)
    else:
        _system.cubitCmd('merge {0[0]} {0[1]} {1} {2}'.format(_functions.listIdString(entities),
                                                              _functions.listStr(args),
                                                              _functions.listKeywordString(kwargs)))


def smartImprint(entities=_common.BodyTypes.body, *args, **kwargs):
    """ Imprint function to only imprint overlapping entities
    :param entities: lis of entities
    :param args: additional parameters for the command: 'option'
    :param kwargs:  additional parameter value pairs: option=value
    :return: None
    """
    if isinstance(entities, str):
        entities = _functions.getEntities(entities, 'all')
    pairs = _functions.searchOverlaps(entities)
    for pair in pairs:
        imprint(pair, *args, **kwargs)


def smartMerge(entities=_common.BodyTypes.body, *args, **kwargs):
    """ Merge function to only merge overlapping entities
    :param entities: lis of entities
    :param args: additional parameters for the command: 'option'
    :param kwargs:  additional parameter value pairs: option=value
    :return: None
    """
    if isinstance(entities, str):
        entities = _functions.getEntities(entities, 'all')
    pairs = _functions.searchOverlaps(entities)
    for pair in pairs:
        merge(pair, *args, **kwargs)
