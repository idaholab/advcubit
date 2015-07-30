""" Create wrapper functions for all cubit functions. Wrapper functions check for errors
"""

import inspect as _inspect

import advcubit
import advcubit.system_module as _system


def init():
    """ Read cubit module and create wrapper functions
    :return: None
    """
    advcubitDict = vars(advcubit)

    for name in dir(_system.cubitModule):
        # test for protected
        if name[0] == '_':
            continue

        var = getattr(_system.cubitModule, name)

        # detect function
        if _inspect.isfunction(var):
            args = _inspect.getargspec(var)
            docStr = var.__doc__

            argStrDefaults = ''
            argStr = ''
            for i, arg in enumerate(args[0]):
                argStrDefaults += ', {0}'.format(arg)
                argStr += ', {0}'.format(arg)

                if args[3] is not None:
                    t = len(args[0]) - len(args[3])
                    if i >= t:
                        argStrDefaults += '={0}'.format(args[3][i - t])

            if args[1] is not None:
                argStrDefaults += ', *{0}'.format(args[1])
                argStr += ', *{0}'.format(args[1])

            if args[2] is not None:
                argStrDefaults += ', **{0}'.format(args[2])
                argStr += ', **{0}'.format(args[2])

            funcStr = '''def {0}(*args):
            """ {1}
            """
            return _system.cubitExec(_system.cubitModule.{0}, *args)'''.format(name, docStr, argStrDefaults[1:], argStr)

            exec funcStr

            # copy to global namespace in wrapper
            globals()[name] = locals()[name]

            # test if we have already defined a function
            if name in advcubitDict:
                _system.debug(name + ' already in advcubit')
            else:
                # copy to advcubit
                advcubitDict[name] = locals()[name]

        # import all classes, no wrapping here at the moment
        elif _inspect.isclass(var):
            globals()[name] = var
            # test if we have already defined a function
            if name in advcubitDict:
                _system.debug(name + ' already in advcubit')
            else:
                # copy to advcubit
                advcubitDict[name] = var
