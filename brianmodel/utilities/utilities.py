#!/usr/bin/python
# coding: utf-8

# #################################################################################
# Copyright (C) 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
# Authors: Francesco Giovannini
# email: francesco.giovannini@inria.fr
# website: http://neurosys.loria.fr/
# Permission is granted to copy, distribute, and/or modify this program
# under the terms of the GNU General Public License, version 3 or any
# later version published by the Free Software Foundation.
#
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details
# #################################################################################



"""
    utilities
    ~~~~~~~~~~~~~
    This module contains various utlity functions that are common to many modules in this package, and its subpackages.

    :copyright 2014 Francesco Giovannini, Neurosys - INRIA CR Nancy - Grand Est
    :licence GPLv3, see LICENCE for more details
"""

import sys



## ***************************************************************************************************************** ##
def getSafeStringParam(param):
    """
    Convert the given parameter into its safe string representation.
    Safe string means that the parameter is wrapped in brackets () to guarantee the omogeneity of equations,  when the parameter is used in mutiplication and division operations.
    """
    res = '''(''' + str(param) + ''')'''

    return res
## ***************************************************************************************************************** ##


## ***************************************************************************************************************** ##
def main(argv):
    pass
## ***************************************************************************************************************** ##


## ***************************************************************************************************************** ##
if __name__=="__main__":
    main(sys.argv[1:])
## ***************************************************************************************************************** ##

