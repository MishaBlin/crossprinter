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

Initial directory and processed directory cannot be empty.

Example:

init_dir:
- input0
- input1

processed_dir:
- processed0
- processed1


**No module named "PIL" problem**:\
To solve the issue, run the following commands:

+ pip uninstall PIL
+ python3 -m pip install --upgrade pip
+ python3 -m pip install Pillow



In case of any problem, contact @mishabl1n.
