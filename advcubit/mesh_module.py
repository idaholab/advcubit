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


def setInterval(entities, interval, *args, **kwargs):
    """ Set the number of intervals for a curve

    :param entities: the base curve
    :param interval: number of intervals
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('{0[0]} {0[1]} interval {1} {2} {3}'.format(_functions.listIdString(entities), interval,
                                                                 _functions.listStr(args),
                                                                 _functions.listKeywordString(kwargs)))


def setAutoSize(entities, factor, *args, **kwargs):
    """ Set auto size on a surface or curve

    :param entities: list or single entity
    :param factor: the auto size factor
    :param propagate: flag for propagation
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('{0[0]} {0[1]} size auto factor {1} {2} {3}'.format(_functions.listIdString(entities), factor,
                                                                         _functions.listStr(args),
                                                                         _functions.listKeywordString(kwargs)))


def setMeshScheme(entities, meshScheme, *args, **kwargs):
    """ Assign a meshing scheme to a body

    :param entities: list or single entity
    :param meshScheme: the scheme
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    idList = _functions.listIdString(entities)
    if idList[0] == _common.BodyTypes.body:
        idList = _functions.listIdString(_functions.getEntitiesFromObject(entities, _common.BodyTypes.volume))
    _system.cubitCmd('{0[0]} {0[1]} scheme {1} {2} {3}'.format(idList, meshScheme,
                                                               _functions.listStr(args),
                                                               _functions.listKeywordString(kwargs)))


def mesh(entities, *args, **kwargs):
    """ Meshes a body using Cubits internal meshing function, that behaves differently

    :param entities: list or single entity to mesh
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    idList = _functions.listIdString(entities)
    if idList[0] == _common.BodyTypes.body:
        idList = _functions.listIdString(_functions.getEntitiesFromObject(entities, _common.BodyTypes.volume))
    _system.cubitCmd('mesh {0[0]} {0[1]} {1} {2}'.format(idList,
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
    if not isinstance(body, _system.cubitWrapper.Body) and not isinstance(body, _system.cubitWrapper.Volume):
        raise _system.AdvCubitException('Object is not a valid cubit entity "{0}"'.format(body))
    _system.cubitCmd('volume {0} scheme sweep source {1[1]} target {2[1]} {3} {4}'
                     .format(body.volumes()[0].id(),
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


def meshQuality(entities, elementType='', *args, **kwargs):
    """ Function to check the quality of the mesh
    :param entities: list of entities or single body, None gives all
    :param elementType: mesh element type
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: None
    """
    _system.cubitCmd('quality {0[0]} {0[1]} {1} {2} {3}'.format(_functions.listIdString(entities),
                                                                elementType,
                                                                _functions.listStr(args),
                                                                _functions.listKeywordString(kwargs)))
