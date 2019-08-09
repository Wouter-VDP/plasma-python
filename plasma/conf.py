from plasma.conf_parser import parameters
import os
import errno

print('\nlooking for conf file:')
print(__file__)
print(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples/conf.yaml'))
print(os.path.exists(os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'examples/conf.yaml')))

conf_file = ''
if os.path.exists(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../examples/conf.yaml')):
    conf_file = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), '../examples/conf.yaml')
elif os.path.exists(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'examples/conf.yaml')):
    conf_file = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'examples/conf.yaml')
elif os.path.exists('./conf.yaml'):
    conf_file = './conf.yaml'
elif os.path.exists('./examples/conf.yaml'):
    conf_file = './examples/conf.yaml'
elif os.path.exists('../examples/conf.yaml'):
    conf_file = '../examples/conf.yaml'
else:
    raise FileNotFoundError(
        errno.ENOENT, os.strerror(errno.ENOENT), 'conf.yaml')

conf = parameters(conf_file)
