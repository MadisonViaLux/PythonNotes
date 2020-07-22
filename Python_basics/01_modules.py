"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print('\n***This is the command line***', sys.argv)
newLine = str(sys.argv).split('/')
print(newLine)
for m in newLine:
    print('\nargument: ', m)

# Print out the OS platform you're using:
import platform
print('\n***OS Platform***', platform.system() + platform.release(), "Version " + platform.version())
#https://stackoverflow.com/questions/1854/what-os-am-i-running-on

# Print out the version of Python you're using:
print('\n***version of Python***', sys.version)
#https://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
print("\n***OS module***", os.name)
# Print the current process ID
print("\n***process ID***", os.getpid())
# Print the current working directory (cwd):
print("\n***directory***", os.getcwd())
# Print out your machine's login name
print("\n***machine's login name***", os.getlogin())