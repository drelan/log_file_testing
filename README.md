## Project 1 (parser.py)
Given a sample/example log file, create a parser with the following requirements. Ignore
the line labels (e.g. “Line 1:”).
a. Given a message severity (Information, Error, Critical) return all matching lines
b. Given a message string and a starting time stamp return the matching message line(s) or
timeout after 30 minutes.

### Steps
We will be opening the log file for reading, and traversing it line-by-line to find out the lines matching the given criteria.

### Installation
- Install pytest testing framework using pip
  
### Execution
- Pre-Requisite: Python 3.13.x is installed
- `$ pytest test_log_parser.py`


##  Project 2 (unique_integer.py)
Given a list of mixed integers and characters, where each integer is repeated twice except for one:

a. Write a program to find the one integer that is not repeating twice.
b. Write unit tests for your program.

There is no need to solve for all possible scenario (Non-English support, Unicode support, white
spaces, etc.). 

### Installation
- Install pytest testing framework using pip

### Execution
- Pre-Requisite: Python 3.13.x is installed
- `$ pytest test_unique_integer.py --verbose`
