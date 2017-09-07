""" Module for volume creation and operations.

This module provides functions to create missing volume types in Cubit.
"""

import math

import advcubit.system_module as _system
import advcubit.function_module as _functions
import advcubit.curve_module as _curve
import advcubit.transform_module as _transform
import advcubit.boolean_module as _boolean


def getLastVolume():
    """ Retrieve the last created volume

    :return: The last volume created within Cubit
    """
    lastId = _system.cubitWrapper.get_last_id('body')

    try:
        return _system.cubitWrapper.volume(lastId)
    except RuntimeError as e:
        print('Cannot retrieve last volume id:\n' + str(e))
        return None


def sweepDirection(surface, distance, direction='z', *args, **kwargs):
    """
    :param surface: source surface
    :param distance: distance to sweep
    :param direction: direction: x, y, z, negative: nx, ny, nz
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: created volume
    """
    _system.cubitCmd('sweep surface {0} direction {1} distance {2} {3} {4}'.format(surface.id(), direction, distance,
                                                                                   _functions.listStr(args),
                                                                                   _functions.listKeywordString(
                                                                                       kwargs)))
    return _transform.getLastBody()


def sweepCurve(surface, curve, *args, **kwargs):
    """ Creates a volume by sweeping a surface along an arbitrary curve
    :param surface: source surface
    :param curve: sweep curve
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: create volume
    """
    _system.cubitCmd('Sweep surface {0} along curve {1} {2} {3}'.format(surface.id(), curve.id(),
                                                                        _functions.listStr(args),
                                                                        _functions.listKeywordString(kwargs)))
    return _transform.getLastBody()


def sweepVector(surface, vector, *args, **kwargs):
    """ Creates a volume by sweeping a surface along an arbitrary curve
    :param surface: source surface
    :param vector: vector in tuple form
    :param args: additional parameters for the command: 'option'
    :param kwargs: additional parameter value pairs: option=value
    :return: create volume
    """
    _system.cubitCmd('Sweep surface {0} vector {1[0]} {1[1]} {1[2]} {2} {3}'.format(surface.id(), vector,
                                                                                    _functions.listStr(args),
                                                                                    _functions.listKeywordString(
                                                                                        kwargs)))
    return _transform.getLastBody()


def cylinder(height, radius):
    """ Creates a cylinder with an imprinted line

    :param height: cylinder height
    :param radius: cylinder radius
    :return: created volume
    """
    circle = _curve.createCircle(radius, 0.5 * height)
    surface = _system.cubitWrapper.create_surface([circle]).surfaces()[0]

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
    center = _system.cubitWrapper.create_vertex(0, 0, height / 2)
    points = [
        _system.cubitWrapper.create_vertex(math.cos(startAngle) * radius, math.sin(startAngle) * radius, height / 2),
        _system.cubitWrapper.create_vertex(math.cos(endAngle) * radius, math.sin(endAngle) * radius, height / 2),
        _system.cubitWrapper.create_vertex(math.cos(endAngle) * (radius + thickness),
                                          math.sin(endAngle) * (radius + thickness), height / 2),
        _system.cubitWrapper.create_vertex(math.cos(startAngle) * (radius + thickness),
                                          math.sin(startAngle) * (radius + thickness), height / 2)
    ]

    curves = [_curve.createArc(center, points[0], points[1]),
              _system.cubitWrapper.create_curve(points[1], points[2]),
              _curve.createArc(center, points[2], points[3]),
              _system.cubitWrapper.create_curve(points[3], points[0])
              ]

    normal = _system.cubitWrapper.create_curve(center, _system.cubitWrapper.create_vertex(0, 0, -height / 2))
    surface = _system.cubitWrapper.create_surface(curves).surfaces()[0]
    body = sweepCurve(surface, normal)
    _transform.delete(normal, 'curve')

    return body


def setName(entities, name):
    """ Set a name for a single entity or a list of entities

    :param entities: single or list of entities
    :param name: name to be set
    :return: None
    """
    _system.cubitCmd('{0[0]} {0[1]} rename "{1}"'.format(_functions.listIdString(entities), name))


def setColor(entities, color):
    """ Set the color for a single entity or a list of entities

    Colors available are:
    red green yellow magenta khaki cyan white skyblue gold lightblue lightgreen salmon coral pink purple paleturquoise
    lightsalmon springgreen lightcyan orange seagreen pink turquoise greenyellow powderblue mediumturquoise, grey
    tomato lightcyan dodgerblue aquamarine lightgoldenrodyellow darkgreen lightcoral mediumslateblue lightseagreen
    goldenrod indianred mediumspringgreen darkturquoise yellowgreen chocolate steelblue burlywood hotpink saddlebrown
    violet tan mediumseagreen thistle palegoldenrod firebrick palegreen lightyellow darksalmon orangered palevioletred
    limegreen mediumblue blueviolet deeppink beige royalblue darkkhaki lawngreen lightgoldenrod plum sandybrown
    lightslateblue orchid cadetblue peru olivedrab mediumpurple maroon lightpink darkslateblue rosybrown
    mediumvioletred lightsteelblue mediumaquamarine proe_background win2kgray proe_2001_top proe_2001_bottom
    wildfire_top wildfire_bottom

    :param entities: single or list of entities
    :param color: color, choose from available colors
    :return: None
    """

    _system.cubitCmd('color {0[0]} {0[1]} {1}'.format(_functions.listIdString(entities), color))
