import re
import datetime as dt
import time
import os

def parse_log_file(logfile):
    try:
        with open(logfile, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Log file {logfile} not found")

def get_lines_by_severity(logfile, severity):
    lines = parse_log_file(logfile)
    matching_lines = []
    severity_pattern = re.compile(rf"\b{severity}\b")
    for line in lines:
        if severity_pattern.search(line):
            matching_lines.append(line.strip())
    return matching_lines

def get_lines_by_message_and_time(logfile, message, start_timestamp, timeout_minutes=30):
    lines = parse_log_file(logfile)
    matching_lines = []
    start_time = dt.datetime.strptime(start_timestamp, "%H:%M:%S")
    end_time = start_time + dt.timedelta(minutes=timeout_minutes)
    start_processing = time.time()
    
    time_pattern = re.compile(r'\d{2}:\d{2}:\d{2}')
    for line in lines:
        if time.time() - start_processing > timeout_minutes * 60:
            print(f"Timeout after {timeout_minutes} minutes")
            break
        match = time_pattern.search(line)
        if not match:
            continue
        log_time = dt.datetime.strptime(match.group(), "%H:%M:%S")
        if start_time <= log_time <= end_time and message in line:
            matching_lines.append(line.strip())
    return matching_lines

if __name__ == "__main__":
    # Construct path to data/log_file.txt relative to this script
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of log_parser.py
    logfile = os.path.join(base_dir, "..", "data", "log_file.txt")
    
    print("Severity 'Information':")
    info_lines = get_lines_by_severity(logfile, "Information")
    for line in info_lines:
        print(line)
    
    print("\nMessage 'Log' with timestamp '07:22:54':")
    message_lines = get_lines_by_message_and_time(logfile, "Log", "07:22:54")
    for line in message_lines:
        print(line)
