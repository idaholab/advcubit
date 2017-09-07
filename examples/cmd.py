""" Example file to show the difference of the cmd command
"""

# import and init advcubit
import advcubit
advcubit.init(None, False)
import cubit

# start cubit
advcubit.startCubit()

# use the originally cmd function
print('First try the original cmd')
try:
    # execute a wrong command
    cubit.cmd('this is not a command')
    # passed command, print it
    print('#' * 80)
    print('No error found in cubit.cmd')
# catch a possible error
except Exception as e:
    print('#' * 80)
    print('We got an error with cubit.cmd:\n' + str(e))
# print that we are done
print('Done!!!')
print('#' * 80)


# use the advanced cmd function
print('Lets try the advcubit cmd')
try:
    # execute a wrong command
    advcubit.cmd('this is not a command')
    # passed command, print it
    print('#' * 80)
    print('No error found in advcubit.cmd')
# catch a possible error
except Exception as e:
    print('#' * 80)
    print('We got an error with advcubit.cmd:\n' + str(e))
# print that we are done
print('Done!!!')
print('#' * 80)

# close cubit and clean
advcubit.closeCubit()
advcubit.deleteJournalFiles()
