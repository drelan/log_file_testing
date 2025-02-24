import re
import datetime as dt
import time

def parse_log_file(logfile):
    """Parse the log file and return its lines as a list."""
    try:
        with open(logfile, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Log file {logfile} not found")

def get_lines_by_severity(logfile, severity):
    """
    Return all lines matching the given severity (Information, Error, Critical).
    """
    lines = parse_log_file(logfile)
    matching_lines = []
    severity_pattern = re.compile(rf"\b{severity}\b")  # Word boundary for exact match
    
    for line in lines:
        if severity_pattern.search(line):
            matching_lines.append(line.strip())
    
    return matching_lines

def get_lines_by_message_and_time(logfile, message, start_timestamp, timeout_minutes=30):
    """
    Return lines matching the message string within 30 minutes of the start timestamp.
    """
    lines = parse_log_file(logfile)
    matching_lines = []
    start_time = dt.datetime.strptime(start_timestamp, "%H:%M:%S")
    end_time = start_time + dt.timedelta(minutes=timeout_minutes)
    start_processing = time.time()  # For real-time timeout
    
    time_pattern = re.compile(r'\d{2}:\d{2}:\d{2}')
    for line in lines:
        # Check timeout
        if time.time() - start_processing > timeout_minutes * 60:
            print(f"Timeout after {timeout_minutes} minutes")
            break
        
        # Extract timestamp
        match = time_pattern.search(line)
        if not match:
            continue
        log_time = dt.datetime.strptime(match.group(), "%H:%M:%S")
        
        # Check if line is within time window and contains message
        if start_time <= log_time <= end_time and message in line:
            matching_lines.append(line.strip())
    
    return matching_lines

if __name__ == "__main__":
    logfile = "log_file.txt"
    
    # Demo 1a
    print("Severity 'Information':")
    info_lines = get_lines_by_severity(logfile, "Information")
    for line in info_lines:
        print(line)
    
    # Demo 1b
    print("\nMessage 'Log' with timestamp '07:22:54':")
    message_lines = get_lines_by_message_and_time(logfile, "Log", "07:22:54")
    for line in message_lines:
        print(line)
