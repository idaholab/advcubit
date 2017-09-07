""" Patching classes """

import advcubit.system_module as _system

def patch_classes():
    """ Fixes functionality of the cubit classes.

    Sometime I might write full wrappers, but till then I use this workaround.
    """
    def geomEntityHash(self):
        """ provide a useful hash function for objects based on subclass and id

        Be aware that the hash might change with a call to compress
        """
        return hash((self.__class__, self.id()))

    _system.cubitModule.GeomEntity.__hash__ = geomEntityHash

    def geomEntityEqual(self, rhs):
        """ equal function, based on subclass and id """
        return isinstance(rhs, self.__class__) and self.id() == rhs.id()

    _system.cubitModule.GeomEntity.__eq__ = geomEntityEqual

    def geomEntityNotEqual(self, rhs):
        """ not equal function, standard definition """
        return not self.__eq__(rhs)

    _system.cubitModule.GeomEntity.__ne__ = geomEntityNotEqual
