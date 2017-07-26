""" Module for surface operations
"""

import advcubit.system_module as _system
import advcubit.function_module as _functions


def getLastSurface():
    """ Retrieve the last created surface

    :return: The last surface created within Cubit
    """
    lastId = _system.cubitWrapper.get_last_id('surface')

    try:
        return _system.cubitWrapper.surface(lastId)
    except RuntimeError as e:
        print('Cannot retrieve last body id:\n' + str(e))
        return None


def findSurfaceWithNormal(surfaces, normal, prec=2):
    """ Find the plain surfaces with the specified normal and return the list

    :param surfaces: list of surfaces
    :param normal: the normal in vector/list format
    :param prec: number of digits, the normals are compared to
    :return: list of surfaces
    """
    tmpSurfaces = []
    for surface in surfaces:
        # sort out cylinders
        if surface.is_cylindrical():
            continue

        # test for normal
        surfaceNormal = surface.normal_at([0, 0, 0])
        if _functions.roundTuple(surfaceNormal, prec) == _functions.roundTuple(normal, prec):
            tmpSurfaces.append(surface)

    return tmpSurfaces


def findClosestSurface(surfaces, point):
    """ Find the closet surface to a specified point

    :param surfaces: list of surfaces
    :param point: the point in vector/list format
    :return: closest surface
    """
    tmpDist = float('Inf')
    tmpSurface = None
    for surface in surfaces:
        # calc distance to center
        tmpPoint = surface.closest_point_trimmed(point)
        dist = (tmpPoint[0] - point[0]) ** 2 + (tmpPoint[1] - point[1]) ** 2 + (tmpPoint[2] - point[2]) ** 2
        # greater distance, store surface
        if dist < tmpDist:
            tmpDist = dist
            tmpSurface = surface

    return tmpSurface


def findCommonSurfaces(entities):
    """ Find surfaces that all bodies or volumes have in common

    :param entities: list of bodies or volumes
    :return: set of surfaces which all enteties have
    """

    surfaces = set(entities[0].surfaces())

    for entity in entities:
        surfaces &= set(entity.surfaces())

    return surfaces
