"""
Utility functions for controlling Cubit

This module provides general functions to controll settings, load, save and export files
and merging and imprinting
"""

import advcubit.system_module as _system


def startCubit():
    """ Starts cubit

    :return: None
    """
    try:
        _system.cubitModule.init([''])
    except AttributeError:
        raise RuntimeError('AdvCubit is not initialized')


def closeCubit():
    """ Closes cubit
    :return: None
    """
    _system.cubitModule.destroy()


def enableDeveloperCommands(enabled=True):
    """ Enable the developer commands granting access to advanced beta functionality

    :param enabled: Flag if on or off
    :return: None
    """
    if enabled:
        enabled = 'on'
    else:
        enabled = 'off'
    _system.cubitCmd('set developer commands {0}'.format(enabled))


def enableJournal(enabled=True):
    """ Turn the journal on or off,

    :param enabled: Flag if on or off
    :return:
    """
    if enabled:
        enabled = 'on'
    else:
        enabled = 'off'
    _system.cubitCmd('journal {0}'.format(enabled))


def reset():
    """ Creates an empty workspace

    :return: None
    """
    _system.cubitCmd('reset')


def resetErrors():
    """ Reset the error count to supress the error message at the end of a scripts
    """
    _system.cubitCmd('reset errors')


def newFile():
    """ Creates an empty workspace

    :return: None
    """
    _system.cubitCmd('reset')


def open(fileName):
    """ Open a Cubit format file

    :param fileName: File path to open
    :return: None
    """
    _system.cubitCmd('open "{0}"'.format(fileName))


def save(fileName, overwrite=True):
    """ Saves the current file to Cubit format

    :param fileName: File name to save to
    :param overwrite: Flag if existing files is to overwrite
    :return: None
    """

    if overwrite:
        _system.cubitCmd('save as "{0}" overwrite'.format(fileName))
    else:
        _system.cubitCmd('save as "{0}"'.format(fileName))


def export(filename, overwrite=True):
    """ Export to external format

    :param filename: path to export to
    :param overwrite: flag if to everwrite existing file
    :return: None
    """
    if overwrite:
        _system.cubitCmd('export mesh "{0}" overwrite'.format(filename))
    else:
        _system.cubitCmd('export mesh "{0}"'.format(filename))

def executeJournalFile(fileName, echo=False):
    """ Read and execute a journal file

    :param fileName: path and name of journal file
    :param echo: print commands before executing them, default False
    :return: None
    """
    import __builtin__

    with __builtin__.open(fileName, 'r') as journal:
        for line in journal:
            # line = line.split('#')[0].strip()
            line = line.strip()
            if line:
                print(line)
                _system.cubitCmd(line)


def deleteJournalFiles(path='.', fileName='cubit*.jou'):
    """ Delete all Cubit journal files in specified folder
    :param path: path to  search
    :param fileName: glob file name to delete
    :return:
    """
    import glob
    import os

    filelist = glob.glob(path + '/{0}'.format(fileName))
    for f in filelist:
        os.remove(f)
