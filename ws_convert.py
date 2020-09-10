import argparse

parser = argparse.ArgumentParser(description='WordStar documents to plain txt converter')

parser.add_argument(
    'input_file',
    action="store",
    help='input file name',
)
parser.add_argument(
    'output_file',
    action='store',
    help='output file name',
    )

args = parser.parse_args()


output_fh = open(args.output_file, 'w')

with open(args.input_file, 'r') as input_fh:
    line = input_fh.read()
    for char in line:
        output_fh.write(chr(ord(char) & 0b01111111))
output_fh.close()
