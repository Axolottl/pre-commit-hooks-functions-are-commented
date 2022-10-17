from __future__ import annotations

import argparse
from typing import Sequence

BLACKLIST = [
    b'def',
]

COMMENTS = [
    b'"""',
]


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    mapping = {}

    for filename in args.filenames:
        with open(filename, 'rb') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                for blacklist in BLACKLIST:
                    if blacklist in lines[i]:
                        for comments in COMMENTS:
                            if comments not in lines[i+1]:
                                if filename not in mapping.keys():
                                    mapping[filename] = []
                                mapping[filename].append(f'{i} : {lines[i]}')
        for key in mapping:
            print(f'Uncommented functions have been found: {key}')
            for values in mapping[key]:
                print(f'    Line : {values}')
        return 1
    else:
        return 0


if __name__ == '__main__':
    raise SystemExit(main())