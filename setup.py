#!/usr/bin/python

import sys
import os
from subprocess import call

try:
    project_name = sys.argv[1]
except IndexError:
    print 'A project name is requried.'
    sys.exit()
try:
    directory = sys.argv[2]
except IndexError:
    print 'Please specify a directory to install the project.'
    sys.exit()

print 'Initializing...'
os.chdir('pip')
call(['python', 'setup.py', 'install'])
os.chdir('../')
call(['pip', 'install', 'virtualenv'])
call(['rm', '-rf', 'pip/dist'])
call(['rm', '-rf', 'pip/pip.egg-info'])

if not os.path.isdir('venv'):
    call(['virtualenv', 'venv', '--distribute'])

print 'Setting Up Django...'
activate_file = 'venv/bin/activate_this.py'
execfile(activate_file, dict(__file__=activate_file))
call(['pip', 'install', 'django'])

if not os.path.isdir(directory):
    print 'Creating Project Boilerplate...'
    os.makedirs(directory)
    call(['django-admin.py', 'startproject', '--template=project_template/', project_name, directory])

print 'Setting Up Python Modules...'

call(['rm', '-rf', 'venv'])

os.chdir(directory)
call(['virtualenv', 'venv', '--distribute'])
activate_file = 'venv/bin/activate_this.py'
execfile(activate_file, dict(__file__=activate_file))
call(['pip', 'install', '-r', 'requirements.txt'])

os.rename('lint.py', 'lint.sh')

print 'Starting Up Server...'

call(['python', 'manage.py', 'syncdb'])
call(['python', 'manage.py', 'migrate'])
