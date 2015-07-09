""" Module for volume creation and operations.

This module provides functions to create missing volume types in Cubit.
"""

import advcubit.system as _system
import advcubit.curve as _curve
import advcubit.transform as _transform
import advcubit.boolean as _boolean

import math


def getLastVolume():
    """ Retrieve the last created volume

    :return: The last volume created within Cubit
    """
    lastId = _system.cubitModule.get_last_id('body')

    try:
        return _system.cubitModule.volume(lastId)
    except RuntimeError as e:
        print('Cannot retrieve last volume id:\n' + str(e))
        return None


def sweepDirection(surface, distance, direction = 'z'):
    """
    :param surface: source surface
    :param distance: distance to sweep
    :param direction: direction: x, y, z, negative: nx, ny, nz
    :return: created volume
    """
    _system.cubitCmd('sweep surface {0} direction {1} distance {2}'.format(surface.id(), direction, distance))
    return _transform.getLastBody()


def sweepSurface(surface, curve):
    """ Creates a volume by sweeping a surface along an arbitrary curve
    :param surface: source surface
    :param curve: sweep curve
    :return: create volume
    """
    _system.cubitCmd('Sweep surface {0} along curve {1}'.format(surface.id(), curve.id()))
    return _transform.getLastBody()


def cylinder(height, radius):
    """ Creates a cylinder with an imprinted line

    :param height: cylinder height
    :param radius: cylinder radius
    :return: created volume
    """
    circle = _curve.createCircle(radius, 0.5 * height)
    surface = _system.cubitModule.create_surface([circle]).surfaces()[0]

    return sweepDirection(surface, height, 'nz')


def ring(height, innerRadius, outerRadius):
    """  Create a annular ring
    :param height: height of ring
    :param innerRadius: radius of inner surface
    :param outerRadius: radius of outer surface
    :return: created volume
    """
    inner = cylinder(height, innerRadius)
    outer = cylinder(height, outerRadius)

    return _boolean.subtract([inner], [outer])[0]


def arc(radius, startAngle, endAngle, height, thickness):
    """ Create an arc

    :param radius: radius of the arc
    :param startAngle: angle from which the arc is created
    :param endAngle: angle to which the arc is created
    :param height: Height of volume
    :param thickness:
    :return: created volume
    """
    center = _system.cubitModule.create_vertex(0, 0, height/2)
    points = [_system.cubitModule.create_vertex(math.cos(startAngle) * radius, math.sin(startAngle) * radius, height/2),
              _system.cubitModule.create_vertex(math.cos(endAngle) * radius, math.sin(endAngle) * radius, height/2),
              _system.cubitModule.create_vertex(math.cos(endAngle) * (radius + thickness), math.sin(endAngle) * (radius + thickness), height/2),
              _system.cubitModule.create_vertex(math.cos(startAngle) * (radius + thickness), math.sin(startAngle) * (radius + thickness), height/2)
              ]

    curves = [_curve.createArc(center, points[0], points[1]),
              _system.cubitModule.create_curve(points[1], points[2]),
              _curve.createArc(center, points[2], points[3]),
              _system.cubitModule.create_curve(points[3], points[0])
              ]

    normal = _system.cubitModule.create_curve(center, _system.cubitModule.create_vertex(0, 0, -height/2))
    surface = _system.cubitModule.create_surface(curves).surfaces()[0]
    body = sweepSurface(surface, normal)
    _transform.delete(normal, 'curve')

    return body
