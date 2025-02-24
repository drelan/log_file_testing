## Project 1 (parser.py)
Given a sample/example log file, create a parser with the following requirements. Ignore
the line labels (e.g. “Line 1:”).
- Given a message severity (Information, Error, Critical) return all matching lines
- Given a message string and a starting time stamp return the matching message line(s) or
timeout after 30 minutes.

### Steps
We will be opening the log file for reading, and traversing it line-by-line to find out the lines matching the given criteria.

### Installation
- Install pytest testing framework using pip
  
### Execution
- Clone the repo from GitHub.
- From the project/ directory:
   - Run the script: python src/log_parser.py
   - Run unit tests: pytest tests/test_log_parser.py --verbose


##  Project 2 (unique_integer.py)
Given a list of mixed integers and characters, where each integer is repeated twice except for one:

- Write a program to find the one integer that is not repeating twice.
- Write unit tests for your program.

There is no need to solve for all possible scenario (Non-English support, Unicode support, white
spaces, etc.). 

### Installation
- Install pytest testing framework using pip

### Execution
- Clone the repo from GitHub.
- From the project/ directory:
   - Run the script: python src/log_unique_integer.py
   - Run unit tests: pytest tests/test_unique_integer.py --verbose
