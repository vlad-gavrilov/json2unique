import sys
import argparse
import json
from pathlib import Path

from .parser import parse_json_to_list_of_unique
from .context_manager import RecursionDepth


def main():
    parser = argparse.ArgumentParser(description='JSON parser')

    parser.add_argument('infile', nargs='?',
                        type=argparse.FileType(encoding="utf-8"),
                        help='the path to the JSON file to be parsed',
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?',
                        type=Path,
                        help='the path to the output file',
                        default=None)
    parser.add_argument('-d', '--depth',
                        type=int, default=10_000,
                        help='set maximum recursion depth')

    args = parser.parse_args()

    with args.infile as infile:
        try:
            loaded = json.load(infile)
        except json.JSONDecodeError as e:
            raise SystemExit(e)

    with RecursionDepth(args.depth):
        resulting_list = parse_json_to_list_of_unique(loaded)

    if args.outfile is None:
        out = sys.stdout
    else:
        out = args.outfile.open('w', encoding='utf-8')
    with out as outfile:
        outfile.write(str(resulting_list))
        outfile.write('\n')


if __name__ == '__main__':
    try:
        main()
    except BrokenPipeError as exc:
        sys.exit(exc.errno)
