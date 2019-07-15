import getopt
import sys

argv = sys.argv[1:]
"""
try:
    opts, args = getopt.getopt(argv, 'h:d', ['help', 'my_file='])
    print(opts)
    print(args)
except getopt.GetoptError:
    #Print a message or do something useful
    print('Something went wrong!')
    sys.exit(2)
"""

options, remainder = getopt.gnu_getopt(
    sys.argv[1:], 'o:v', ['output=', 'debug', 'variant=',])
print('OPTIONS   :', options)

for opt, arg in options:
    if opt in ('-o', '--output'):
        print('Setting --output.')
        output_file = arg
    elif opt in ('-d', '--debug'):
        print('Setting --debug.')
        debug = True
    elif opt == '--variant':
        print('Setting --variant.')
        variant = arg

print('VARIANT   :', variant)
print('DEBUG   :', debug)
print('OUTPUT    :', output_file)
print('REMAINING :', remainder)