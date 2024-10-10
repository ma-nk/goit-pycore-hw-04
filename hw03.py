import os
from pathlib import Path
from colorama import Fore, Style

def parse_file(path):
    for el in path.iterdir():
        level = str(el).count(os.sep)
        indents = 2 * '  ' * (level)
        if el.is_dir():
            print(indents + Fore.GREEN + str(os.path.basename(el)))
            parse_file(el)
        else:
            print(indents + Fore.LIGHTBLUE_EX + str(os.path.basename(el)))
    print(Style.RESET_ALL)


print(parse_file(Path("test")))
