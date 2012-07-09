#! /usr/bin/env python
# -*- coding: utf-8 -*-

# killp.py - Kill a process by its name 
# 
# Copyright (C) 2012 Mutse <yyhoo2.young@gmail.com>, all rights reserved.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import os
import subprocess
from optparse import OptionParser

def signal_callback(option, opt, value, parser):
    assert value is None
    value = []

    for arg in parser.rargs:
        if arg[:2] == "-s" and len(arg) > 1:
            break
        value.append(arg)

# kill process by its name
def kill_by_name(name):
    cmd = "ps -ef | grep " + name + "| grep -v grep | grep -v killp.py | sed -e 's/^  *//' | /usr/bin/awk '{print $2}'"
    output = subprocess.Popen([cmd], stdout = subprocess.PIPE, shell = True).communicate()

    pids = output[0].split('\n')

    #print pids
    for pid in pids:
        if not pid:
            continue
        else:
            #print pid
            cmd = 'kill -9 ' + pid
            os.system(cmd)

            print "%s Terminaled" % name

def main():
    usage = "usage: %prog [options] arg"
    version = "%prog (Chin Foundry) 1.0"
    parser = OptionParser(usage = usage, version = version)
    parser.add_option("-s",
         action ="callback", callback = signal_callback,
         dest = "verbose", default = True,
         help = "signal num")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    (options, args) = parser.parse_args()
    for arg in args:
	print arg
        kill_by_name(arg)

if __name__ == '__main__':
    main()
