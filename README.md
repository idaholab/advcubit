# advcubit
A script package for an advanced cubit interface. Provides a lot of functionality, that is not included in the official python interface.

## Bugs and feature requests

If there is a bug or a feature, that is missing, please submit an issue. This package is maintained, but new features are only implemented on request. And even this can take a while, depending on my time. Providing fixes and new functionality is highly appreciated. Please refer to the coding guidelines. For a bug, please provide the error message and at least the call to the advcubit function. If possible, a short, executable example is appreciated and will speed up the process.

For feature requests, provide the Cubit syntax and a link to the Cubit documentation, where this syntax is described. Also give an example, what is expected by that command to be done.

## Installation

To install the package, run:

```bash
python setup.py install
```

Note, that Cubit only supports python 2.7 under Linux and python 2.6 under MacOs. Choose the according python executable. To install as a normal user, use the --user flag for the installation, e.g.

```bash
python2.6 setup.py install --user # for MacOs as normal user
```

## Usage

Import the module into python. The module must be initialized prior to usage. To do so, run:

```python
import advcubit
advcubit.init(cubitPath, silent)
```

The init() function expects the path to the Cubit installation. If the parameter is not provided, it will try to use the environment variable $CUBIT_PATH. This can be set by

``` bash
export CUBIT_PATH="path/to/Cubit/"
```

The second parameter is a flag to echo the commands performed. The default is silent. All functions are directly accessible, even though they are organized in different modules. To start Cubit, use

```python
advcubit.startCubit()
```

To directly access the cubit python interface, you must import the cubit module after the initialization of advcubit. It will be added to the python import path.

```python
import advcubit
advcubit.init(cubitPath)
import cubit
```

All cubit python interface functions are available directly in advcubit. The are imported and wrapped within the package for error detection. It is recommended to use the advcubit wrapper functions instead of directly the interface. All wrapper functions have the identical name.

## Examples

Examples are provides in the examples directory. The examples available at the moment are:

File | Description
--- | ---
[basic.py](examples/basic.py) | shows a simple script using advcubit
[cmd.py](examples/cmd.py) | demonstrates the difference of cubit.cmd and advcubit.cmd
[parameters.py](examples/parameters.py) | shows, how to pass arbitrary parameters to advcubit functions

## Tests

To run the tests, simply execute the run_tests.py scripts with the correct python interpreter. To run
the tests, $CUBIT_PATH must be set. To implement tests, please take a look at the already provided tests.
The framework already exists, the tests just need to be implemented and added to the according module's
test suite. For options executing the tests, please refer to the unittest documentation:

https://docs.python.org/2.6/library/unittest.html MacOs python 2.6
https://docs.python.org/2/library/unittest.html Linux python 2.7

## Coding Guidelines

The coding guidelines are PEP8. They can be found at https://www.python.org/dev/peps/pep-0008/.
Only the naming conventions differ from that. Classes start with an upper case, functions and
variables start lower case. After that, camel case is used for all. All internal, global variables
and all imports must start with a _ to avoid an import into the master module. All names must be
descriptive, but as short as possible.
Every module, class and function must have a doc string (triple double quotes) at the beginning.
This doc string must contain all important variables for classes, all parameters and return
values for functions and methods. The recommended IDE is PyCharm, which provides checks for the
coding guidelines (https://www.jetbrains.com/pycharm/).
All new implemented features must have tests. Please refer to the test section.
