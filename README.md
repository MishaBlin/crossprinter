# Crossword Printer

## Usage:

pip install pillow

python3 crossprinter.py -i "directory of initial files" -p "directory of processed files" -o "directory for output"

Example:\
python3 crossprinter.py -i init_dir -p processed_dir -o out_dir

To avoid any errors, make sure that number of files in init_dir is the same as
the number of files in processed_dir.\
Font file (Roboto.ttf) must be in the same folder as crossprinter.py

Also, init_dir files should be in the same order as in processed_dir.

Example:

init_dir:
- input0
- input1

processed_dir:
- processed0
- processed1

In case of any problem, contact @mishabl1n
