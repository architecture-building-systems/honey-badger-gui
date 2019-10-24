"""
honey-badger-gui is a simple GUI wrapper for the ``honey-badger.exe`` command line tool.
"""

from gooey import Gooey, GooeyParser
import subprocess
import sys

def run_honey_badger(badger_file, editable, install, honey_badger_exe):
    command = [honey_badger_exe]
    if editable:
        command.append("-e")
    if install:
        command.append("-i")
    command.append(badger_file)
    print(" ".join(command))
    print(subprocess.check_output(command).decode("utf-8"))


@Gooey(advanced=True, required_cols=1, optional_cols=2)
def main():
    parser = GooeyParser(description="Honey-badger GUI") 
    parser.add_argument('-i', '--install', action="store_true", default=True, help="Install compiled .ghpy file to Grasshopper Libraries folder")
    parser.add_argument('BADGERFILE', action="store", widget="FileChooser", help="The BADGERFILE to compile (*.json)", gooey_options={
        "wildcard": "*.json",
    })
    parser.add_argument('honey-badger', action="store", widget="FileChooser", default="../honey-badger/honey-badger.exe", help="Path to the honey-badger.exe")
    args = parser.parse_args(sys.argv[1:])
    run_honey_badger(badger_file=args.BADGERFILE, editable=False, install=args.install, honey_badger_exe=vars(args)["honey-badger"])


if __name__ == '__main__':
    main()