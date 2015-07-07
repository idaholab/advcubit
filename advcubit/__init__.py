"""
Package providing additional function for cubit that are not part of the normal cubit interface.

This package contains wrapper functions to access Cubit functionality, that is not (yet) included
in Cubit's python interface. Before it can be used, init() must be called and passed the path to the
Cubit installation.
"""

__author__ = 'Hans R Hammer'

import advcubit.system as _system

_system.checkVersion()

from advcubit.system import init

from advcubit.utility import *
from advcubit.vertex import *
from advcubit.curve import *
from advcubit.surface import *
from advcubit.volume import *
from advcubit.transform import *
from advcubit.boolean import *
from advcubit.imprint import *
from advcubit.mesh import *