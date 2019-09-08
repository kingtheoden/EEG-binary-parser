# EEG binary parser
 A python program that parses a binary file structure.

## Assumptions
This parser reads the raw binary information of it's input file, not a string representation of a binary number.
Such a file is provided in this repo called `test_file` and you can look at `parse_test_filemaker.py` to see how that file was generated.

## Run Instructions
1. Make sure you have python 3.5 or later installed (this is because I used type hinting to try and better satisfy the typed language preference, which is only available since 3.5)
2. Open Terminal and navigated to the cloned repo and enter `py parser.py < test_file` or the linux equivalent (you can replace text_file with your own file's name)
