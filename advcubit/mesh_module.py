""" Mesh control and meshing operations
"""

import advcubit.system_module as _system
import advcubit.common_module as _common
import advcubit.function_module as _functions


class SurfaceMeshSchemes:
    tri = 'trimesh'
    pave = 'pave'
    map = 'map'
    hole = 'hole'
    circle = 'circle'


class VolumeMeshSchemes:
    sweep = 'sweep'
    map = 'map'
    tet = 'tetmesh'
    sphere = 'sphere'


def setInterval(body, interval, bodyType=_common.BodyTypes.curve, *args, **kwargs):
    """ Set the number of intervals for a curve

    :param body: the base curve
    :param interval: number of intervals
    :param bodyType: type of body
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('{0} {1} interval {2} {3} {4}'.format(bodyType, body.id(), interval,
                                                           _functions.listStr(args),
                                                           _functions.listKeywordString(kwargs)))


def setAutoSize(body, factor, bodyType=_common.BodyTypes.curve, *args, **kwargs):
    """ Set auto size on a surface or curve

    :param body: the body
    :param factor: the auto size factor
    :param propagate: flag for propagation
    :param bodyType: the body type
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('{0} {1} size auto factor {2} {3} {4}'.format(bodyType, body.id(), factor,
                                                                   _functions.listStr(args),
                                                                   _functions.listKeywordString(kwargs)))


def setMeshScheme(body, meshScheme, bodyType=_common.BodyTypes.surface, *args, **kwargs):
    """ Assign a meshing scheme to a body

    :param body: the body
    :param meshScheme: the scheme
    :param bodyType: the type of the body
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('{0} {1} scheme {2} {3} {4}'.format(bodyType, body.id(), meshScheme,
                                                         _functions.listStr(args),
                                                         _functions.listKeywordString(kwargs)))


def mesh(body, bodyType=_common.BodyTypes.volume, *args, **kwargs):
    """ Meshes a body using Cubits internal meshing function, that behaves differently

    :param body: the body to mesh
    :param bodyType: the body type
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('mesh {0} {1} {2} {3}'.format(bodyType, body.id(),
                                                   _functions.listStr(args),
                                                   _functions.listKeywordString(kwargs)))


def sweepMesh(body, sources, targets, *args, **kwargs):
    """ set the meshing scheme of a volume to sweep

    :param body: the body
    :param sources: list/single source surface
    :param targets: list/single target surface
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('volume {0} scheme sweep source {1[1]} target {2[1]} {3} {4}'
                     .format(body.id(),
                             _functions.listIdString(sources, _common.BodyTypes.surface),
                             _functions.listIdString(targets, _common.BodyTypes.surface),
                             _functions.listStr(args),
                             _functions.listKeywordString(kwargs)))
    mesh(body.volumes()[0])


def scaleMesh(factor, *args, **kwargs):
    """ Scale created mesh
    :param factor: factor to scale with
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('transform mesh output scale {0} {1} {2}'.format(factor,
                                                                      _functions.listStr(args),
                                                                      _functions.listKeywordString(kwargs)))


def meshQuality(bodies, elementType='', *args, **kwargs):
    """ Function to check the quality of the mesh
    :param bodies: list of bodies or single body, None gives all
    :param elementType: mesh element type
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('quality {0[0]} {0[1]} {1} {2} {3}'.format(_functions.listIdString(bodies),
                                                                elementType,
                                                                _functions.listStr(args),
                                                                _functions.listKeywordString(kwargs)))
