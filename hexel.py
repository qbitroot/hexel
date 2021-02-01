#!/usr/bin/python3
import sys
import string
import argparse

#types_desc = '''Available types(name, example):
#  hex   315fc0ffee
#  raw   \x31\x5f\xc0\xff\xee
#  c     1_\\xc0\\xff\\xee
#  ch    \\x31\\x5f\\xc0\\xff\\xee
#  arr   0x31,0x5f,0xc0,0xff,0xee'''

dtypes = ('raw', 'hex', 'c', 'arr')

parser = argparse.ArgumentParser(description='Convert hex')
parser.add_argument('-t', '--type', default='raw', choices=dtypes, help='Type of input')
parser.add_argument('-o', '--outf', default='all', choices=dtypes+('all','ch'), help='Format of output')
parser.add_argument('-s', '--swap', help='Swap endianness', action='store_true')
parser.add_argument('-i', '--input', help='Input data')
parser.add_argument('-f', '--file', help='Input file (if no input data)')
parser.add_argument('-p', '--pipe', default=True, help='Take input from stdin pipe', action='store_true')
parser.add_argument('-n', help='Strip new line of output', action='store_true')
parser.add_argument('-d', '--debug', help='Debug mode', action='store_true')

args = parser.parse_args()


def keep_hex(s):
    return ''.join([c for c in s if c in string.hexdigits])

def nraw(d):
    return ''.join([chr(i) for i in d])

def nhex(d):
    return bytearray(d).hex()

def ncstr(d):
    r = repr(bytes(d))
    if r.startswith("b'"):
        r = r[2:-1].replace("\\'", "'").replace('"', '\\"')
    else:
        r = r[2:-1]
    return r

def narr(d):
    return ','.join(['0x{:02x}'.format(i) for i in d])

def nch(d):
    return ''.join(['\\x{:02x}'.format(i) for i in d])

if args.input:
    inp = args.input.encode()
elif args.file:
    inp = open(args.file, 'rb').read()
elif args.pipe:
    inp = sys.stdin.buffer.read()

if args.type == 'raw':
    data = list(inp)
elif args.type == 'hex':
    data = list(map(int, bytearray.fromhex(keep_hex(inp.decode()))))
elif args.type == 'c':
    data = list(map(int, bytearray.fromhex(keep_hex(inp.decode()))))
elif args.type == 'arr':
    data = list(map(int, bytearray.fromhex(keep_hex(inp.decode().replace('0x','')))))

if args.debug:
    print(data)

if args.swap:
    data = data[::-1]

if args.n:
    e = ''
else:
    e = '\n'

if args.outf == 'all':
    print(f'[raw]\tRaw: {nraw(data)}')
    print(f'[hex]\tHex: {nhex(data)}')
    print(f'[c]\tC str: "{ncstr(data)}"')
    print(f'[ch]\tC hex str: "{nch(data)}"')
    print(f'[arr]\tArray: {narr(data)}')
elif args.outf == 'raw':
    print(nraw(data), end=e)
elif args.outf == 'hex':
    print(nhex(data), end=e)
elif args.outf == 'c':
    print(f'"{ncstr(data)}"', end=e)
elif args.outf == 'ch':
    print(f'"{nch(data)}"', end=e)
elif args.outf == 'arr':
    print(narr(data), end=e)
