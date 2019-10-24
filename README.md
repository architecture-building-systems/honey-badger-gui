# honey-badger-gui
A simple GUI for running honey-badger.exe using Gooey


## Installation

Easy solution: just use the `honey-badger-gui.exe` in the root folder.

Harder version:

- install Anaconda / Miniconda
- `conda env create -f environment.yml`
- `conda activate honey-badger-gui`
- `pyinstaller honey-badger-gui.spec`

## Usage

Double-click `honey-badger-gui.exe`, choose the BADGERFILE to compile, keep "install" selected to copy the output to the Grasshopper Libraries folder.

If `honey-badger.exe` can't be found, set the path to `honey-badger.exe` (https://github.com/architecture-building-systems/honey-badger)

Click "Start" to start compilation process.
