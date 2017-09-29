"""Module that handles the include path and the startup of cubit

The module provides helper functions to locate the cubit inlcude paths on
different operating systems and imports the cubit files
"""

import sys as _sys
import os as _os
import warnings as _warnings

cubitModule = None  # reference to the cubit module
cubitWrapper = None  # reference to the cubit wrapper module, used in all submodules
cubitCmdRef = None  # reference to the used cubit command
debugging = False  # debugging flag


class AdvCubitException(RuntimeError):
    """ default exception for advcubit
    """

    def __init__(self, msg):
        """ Constructor
        :param msg: message string
        """
        super(AdvCubitException, self).__init__(msg)


def init(cubitPath=None, silentMode=True):
    """ Sets up the advcubit module

    :param cubitPath: Path to cubit installation director, if None $CUBIT_PATH will be used
    :param silentMode: Flag to suppress cubit commands
    :return: None
    """
    import platform

    global cubitModule
    global cubitWrapper

    if cubitPath is None:
        try:
            cubitPath = _os.environ['CUBIT_PATH']
        except KeyError:
            raise EnvironmentError('$CUBIT_PATH not set')

    osType = platform.system()
    if osType == 'Linux':
        _initLinux(cubitPath)
    elif osType == 'Darwin':
        _initDarwin(cubitPath)
    else:
        raise EnvironmentError('Unsupported operating system: ' + osType)

    try:
        import cubit
    except ImportError as e:
        raise ImportError(
            'Error initializing advcubit\nImportError: {0}\nIs the path to Cubit installation directory set correctly?'
                .format(e))

    cubitModule = cubit
    enableSilentMode(silentMode)

    import advcubit.wrapper_module as wrapper

    cubitWrapper = wrapper
    cubitWrapper.init()

    # add more functionality to classes
    import advcubit.class_module as classes
    classes.patch_classes()


def enableSilentMode(silentMode=True):
    """ Activates the silent mode

    :param silentMode: Flag for activation or deactivation
    :return: None
    """
    global cubitCmdRef

    if silentMode:
        cubitCmdRef = cubitModule.silent_cmd
    else:
        cubitCmdRef = cubitModule.cmd

def disableSilentMode():
    """ Deactivate the silent mode
    """
    enableSilentMode(False)


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


def cubitCmd(cmdStr):
    """ Executes a cubit command and checks for errors
    :param cmdStr: cubit journal command string
    :raises AdvCubitException: Raises an exception, if command fails
    :return: None
    """
    errorCount = cubitModule.get_error_count()
    cubitCmdRef(cmdStr)
    newCount = cubitModule.get_error_count()
    # check if a new error occurred
    if newCount > errorCount:
        raise AdvCubitException('Error executing command: "{0}"'.format(cmdStr))


def cubitExec(function, *args, **kwargs):
    """ Wraps a cubit function and detects execution errors
    :param function: cubit function to wrap
    :param args: parameters to the function
    :param kwargs: keyword parameters to the function
    :return: function return
    """
    errorCount = cubitModule.get_error_count()
    returnValue = function(*args, **kwargs)
    newCount = cubitModule.get_error_count()
    if newCount > errorCount:
        raise AdvCubitException('Error executing cubit function: "{0}" with {1} and {2}'
                                .format(function.__name__, args, kwargs))
    return returnValue


def warning(msg):
    """ Central warning wrapper
    :param msg: Warning message
    :return: None
    """
    _warnings.warn(msg, RuntimeWarning)


def debug(msg):
    """ central debug wrapper
    :param msg: message string
    :return: None
    """
    if debugging:
        print(msg)
