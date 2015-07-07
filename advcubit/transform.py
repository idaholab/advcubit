""" Transformation operations
"""

import advcubit.system as _system


def getLastBody():
    """ Retrieve the last created body

    :return: The last body created within Cubit
    """
    lastId = _system.cubitModule.get_last_id('body')

    try:
        return _system.cubitModule.body(lastId)
    except RuntimeError as e:
        print('Cannot retrieve last created body:\n' + str(e))
        return None


def delete(body, blockType = 'body'):
    """ Delete a body

    :param body: the body to be deleted
    :param blockType: the body type
    :return: None
    """
    _system.cubitCmd('delete {0} {1}'.format(blockType, body.id()))


def rotate(body, angle, axis = 'z'):
    """ Rotate a body
    :param body: the body
    :param angle: angle in degrees
    :param axis: coordinate system axis x, y, z
    :return: None
    """
    _system.cubitCmd('rotate body {0} angle {1} about {2} include_merged '.format(body.id(), angle, axis))


def webcut(body, plane = 'x', offset = 0):
    """
    :param body: body to cut
    :param plane: plane: x, y, z
    :param offset: offset from origin
    :return: None
    """
    _system.cubitCmd('webcut body {0}  with plane {1}plane offset {2} noimprint nomerge '.format(body.id(), plane, offset))


def sectionCut(body, plane = 'x'):
    """ Section cut a body
    :param body: the body
    :param plane: plane to cut at: x, y, z
    :return: None
    """
    _system.cubitCmd('section body {0} {1}plane'.format(body.id(), plane))


def copyReflect(body, plane = 'x'):
    """ Reflect and copy a body

    :param body: base body
    :param plane: reflection plane x, y, z
    :return: created body
    """
    _system.cubitCmd('body {0} copy reflect {1}'.format(body.id(), plane))
    return getLastBody()


def rotateBodies(bodies, angle, axis):
    """ Rotate a list of bodies at once
    :param bodies: list of bodies
    :param angle: angle in degrees
    :param axis: coordinate system axis x, y, z
    :return: None
    """
    for body in bodies:
        rotate(body, angle, axis)


def moveBodies(bodies, vector):
    """ Move a list of bodies at once

    :param bodies: list of bodies
    :param vector: move vector in vector/list form
    :return: None
    """
    for body in bodies:
        _system.cubitModule.move(body, vector)


def deleteBodies(bodies):
    """ Delete a list of bodies at once
    :param bodies: list of bodies
    :return: None
    """
    for body in bodies:
        delete(body)


def copyBodies(bodies):
    """ Copy a list of bodies at once

    :param bodies: list of bodies
    :return: List of copies created
    """
    newBodies = []
    for body in bodies:
        newBodies.append(_system.cubitModule.copy_body(body))

    return newBodies
