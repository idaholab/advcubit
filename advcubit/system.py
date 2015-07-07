"""Module that handles the include path and the startup of cubit

The module provides helper functions to locate the cubit inlcude paths on
different operating systems and imports the cubit files
"""

import sys as _sys
import os as _os

cubitModule = None  # reference to the cubit module, used in all submodules
cubitCmd = None     # reference to the used cubit command


def init(cubitPath = None, silentMode = True):
    """ Sets up the advcubit module

    :param cubitPath: Path to cubit installation director, if None $CUBIT_PATH will be used
    :param silentMode: Flag to suppress cubit commands
    :return: None
    """
    import platform
    global cubitModule

    if cubitPath is None:
        cubitPath = _os.environ['CUBIT_PATH']
        if cubitPath is None:
            raise EnvironmentError('$CUBIT_PATH not set')

    osType = platform.system()
    if osType == 'Linux':
        _initLinux(cubitPath)
    elif osType == 'Darwin':
        _initDarwin(cubitPath)
    else:
        raise RuntimeError('Unsupported operating system: ' + osType)

    import cubit
    cubitModule = cubit
    enableSilentMode(silentMode)


def enableSilentMode(silentMode = True):
    """ Activates the silent mode

    :param silentMode: Flag for activation or deactivation
    :return: None
    """
    global cubitCmd
    if silentMode:
        cubitCmd = cubitModule.silent_cmd
    else:
        cubitCmd = cubitModule.cmd


def _initLinux(cubitPath):
    """ Adds the necessary folders to the python path on Linux OS

    :param cubitPath: path to Cubit installation directory
    :return: None
    """
    cubitDirs = [cubitPath + '/bin', cubitPath + '/structure', cubitPath + '/GUI']
    _sys.path.extend(cubitDirs)


def _initDarwin(cubitPath):
    """ Adds the necessary folders to the python path on Mac OS

    :param cubitPath: path to Cubit installation directory
    :return: None
    """
    if _sys.version_info[0] != 2 and _sys.version_info[1] >= 7:
        EnvironmentError('Mac OS cubit can only handle Python 2.6 or maybe less')

    cubitDirs = [cubitPath, cubitPath + '/bin', cubitPath + '/structure', cubitPath + '/GUI']
    _sys.path.extend(cubitDirs)


def checkVersion():
    if _sys.version[0] > 2:
        EnvironmentError('Cubit can only handle Python version 2')
    if _sys.version_info[1] < 7:
        warning('Advcubit may have problems with Python version < 2.7')


def warning(msg):
    """ Central warning wrapper
    :param msg: Warning message
    :return: None
    """
    print('Warning: ' + msg)
