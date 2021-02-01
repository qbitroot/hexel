# 🔤 hexel
Convert various hex formats such as C-style string/array, raw, swap endianness and more!

## Usage
Run `python3 hexel.py -h` to get help.

```
usage: hexel.py [-h] [-t {raw,hex,c,arr}] [-o {raw,hex,c,arr,all,ch}] [-s] [-i INPUT] [-f FILE] [-p] [-n] [-d]

Convert hex

optional arguments:
  -h, --help            show this help message and exit
  -t {raw,hex,c,arr}, --type {raw,hex,c,arr}
                        Type of input
  -o {raw,hex,c,arr,all,ch}, --outf {raw,hex,c,arr,all,ch}
                        Format of output
  -s, --swap            Swap endianness
  -i INPUT, --input INPUT
                        Input data
  -f FILE, --file FILE  Input file (if no input data)
  -p, --pipe            Take input from stdin pipe
  -n                    Strip new line of output
  -d, --debug           Debug mode
```

**Example 1**: `python3 hexel.py -i Hello`. Sample output:
```
[raw]	Raw: Hello
[hex]	Hex: 48656c6c6f
[c]	C str: "Hello"
[ch]	C hex str: "\x48\x65\x6c\x6c\x6f"
[arr]	Array: 0x48,0x65,0x6c,0x6c,0x6f
```

**Example 2**: Convert binary file to C hex string: `python3 hexel.py -f file.bin -o ch`. Sample output:
```
"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
```

**Example 3**: Convert string to little-endian integer (userful for writing shellcode): `python3 hexel.py -i bash -o hex -s`. Sample output:
```
68736162
```
When you write assembly shellcode, output will be used with something like `push 0x68736162` to push `bash\0\0\0\0` to the stack.
