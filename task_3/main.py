from log import log_direct, log_file
import sys
from pathlib import Path

try:
    path_arg = sys.argv[1]
except IndexError:
    print(f"Usage: python {sys.argv[0]} <directory_path>")
    sys.exit(1)

def find_path(path, deep = 1):

    direct_name = "\t" * (deep - 1) + path.name
    log_direct(direct_name)

    for p in path.iterdir():

        if p.is_dir():
            find_path(p, deep + 1)
        else:
            name_file = "\t" * deep + p.stem
            extension = p.suffix.lstrip(".")
            log_file(name_file, extension)

find_path(Path(path_arg))