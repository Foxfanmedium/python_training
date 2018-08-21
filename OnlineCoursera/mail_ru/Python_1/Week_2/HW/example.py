# import argparse
# parser = argparse.ArgumentParser()
# parser.parse_args()

"""
$ python example.py --help
>>> usage: example.py [-h]
optional arguments:
  -h, --help  show this help message and exit
============================================================================================
$ python example.py --verbose
>>> usage: example.py [-h]
example.py: error: unrecognized arguments: --verbose
"""

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('echo')
# args = parser.parse_args()
# print(args.echo)
"""
$ python example.py
>>> usage: example.py [-h] echo
example.py: error: the following arguments are required: echo
============================================================================================
$ python example.py -h
>>> usage: example.py [-h] echo
positional arguments:
  echo
optional arguments:
  -h, --help  show this help message and exit
============================================================================================
$ python example.py foo
>>> foo
"""

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('echo', help='echo the string you use here')
# args = parser.parse_args()
# print(args.echo)
"""
$ python example.py -h
>>> usage: example.py [-h] echo
positional arguments:
  echo        echo the string you use here
optional arguments:
  -h, --help  show this help message and exit
============================================================================================
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('square', help='display a square of a given number', type = int)
args = parser.parse_args()
print(args.square**2)
"""
$ python example.py 4
>>> 16
============================================================================================
$ python example.py four
>>> usage: example.py [-h] square
example.py: error: argument square: invalid int value: 'four'
"""









