""" Mesh control and meshing operations
"""

import advcubit.system as _system


def setInterval(body, interval, equal=True, bodyType='curve'):
    """ Set the number of intervals for a curve

    :param body: the base curve
    :param interval: number of intervals
    :param equal: flag for equal intervals
    :param bodyType: type of body
    :return: None
    """
    _system.cubitCmd('{0} {1} interval {2}'.format(bodyType, body.id(), interval))
    if equal:
        _system.cubitCmd('{0} {1} scheme equal'.format(bodyType, body.id()))


def setAutoSize(body, factor, propagate=True, bodyType='curve'):
    """ Set auto size on a surface or curve

    :param body: the body
    :param factor: the auto size factor
    :param propagate: flag for propagation
    :param bodyType: the body type
    :return: None
    """
    tmpStr = '{0} {1} size auto factor {2}'.format(bodyType, body.id(), factor)
    if propagate:
        tmpStr += ' propagate'
    _system.cubitCmd(tmpStr)


def setMeshScheme(body, meshScheme, bodyType='surface'):
    """ Assign a meshing scheme to a body

    :param body: the body
    :param meshScheme: the scheme
    :param bodyType: the type of the body
    :return: None
    """
    _system.cubitCmd('{0} {1} scheme {2}'.format(bodyType, body.id(), meshScheme))


def createSideset(bodies, sidesetId, bodyType='surface'):
    """ Create a side set

    :param bodies: list of bodies to assign to side set
    :param sidesetId: the id number of the sideset
    :param bodyType: the type of the bodies
    :return:
    """
    tmpStr = ''
    for body in bodies:
        tmpStr += ' {0}'.format(body.id())
    _system.cubitCmd('sideset {0} {1} {2}'.format(sidesetId, bodyType, tmpStr))


def nameSideset(sidesetId, name):
    """ Assign a name to a sideset

    :param sidesetId: the number of the sideset
    :param name: the name to be assigned
    :return: None
    """
    _system.cubitCmd('sideset {0} name "{1}"'.format(sidesetId, name))


def createNodeset(bodies, nodesetId, bodyType='vertex'):
    """ Adds bodies to or creates node set

    :param bodies: list of bodies
    :param nodesetId: number for new/existing node set
    :param bodyType: type of bodies
    :return: None
    """
    tmpStr = ''
    for body in bodies:
        tmpStr += ' {0}'.format(body.id())
    _system.cubitCmd('nodeset {0} {1} {2}'.format(nodesetId, bodyType, tmpStr))


def nameNodeset(nodesetId, name):
    """ Assign a name to a node set

    :param nodesetId: the number of the node set
    :param name: the name to be assigned
    :return: None
    """
    _system.cubitCmd('nodeset {0} name "{1}"'.format(nodesetId, name))


def mesh(body, bodyType='volume'):
    """ Meshes a body using Cubits internal meshing function, that behaves differently

    :param body: the body to mesh
    :param bodyType: the body type
    :return: None
    """
    _system.cubitCmd('mesh {0} {1}'.format(bodyType, body.id()))


def sweepMesh(body, sources, targets):
    """ set the meshing scheme of a volume to sweep

    :param body: the body
    :param sources: list/single source surface
    :param targets: list/single target surface
    :return: None
    """
    try:
        sourceStr = ''
        for source in sources:
            sourceStr += ' {0}'.format(source.id())
    except TypeError:
        sourceStr = '{0}'.format(sources.id())
    try:
        targetStr = ''
        for target in targets:
            targetStr += ' {0}'.format(target.id())
    except TypeError:
        targetStr = '{0}'.format(targets.id())

    _system.cubitCmd('volume {0} scheme sweep source {1} target {2}'.format(body.id(), sourceStr, targetStr))
    mesh(body.volumes()[0])


def scaleMesh(factor):
    """ Scale created mesh
    :param factor: factor to scale with
    :return: None
    """
    _system.cubitCmd('transform mesh output scale {0}'.format(factor))
