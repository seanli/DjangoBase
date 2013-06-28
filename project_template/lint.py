#!/usr/bin/python

import os
from subprocess import call

activate_file = 'venv/bin/activate_this.py'
execfile(activate_file, dict(__file__=activate_file))

directory_list = [path for path in os.listdir('.') if os.path.isdir(path) and path != 'venv']

for directory in directory_list:
    print 'Checking: %s' % directory
    call(['pylint', '--rcfile=pylint.rc', directory])
    call(['pep8', '--repeat', '--ignore=E501,E128,E124', "--exclude='migrations'", directory])
