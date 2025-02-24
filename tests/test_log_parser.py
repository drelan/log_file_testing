import pytest
import os
from log_parser import get_lines_by_severity, get_lines_by_message_and_time

# Sample log file content
LOG_CONTENT = """07:22:54 TylanceSvc(2172)[88] Information: Logging Started: Thursday, May 10, 2018 7:22:54 AM
07:25:32 TylanceSvc(2172)[88] Error: [ImpersonatedTaskManager] GetLogonTokenForImpersonatedTask:Unable To Get Token
07:49:12 TylanceSvc(2172)[98] Information: [LogUploadEngine] Log Rollover Event received
08:13:23 TylanceSvc(2172)[98] Critical: [LogUploadEngine] The service has stopped
08:16:44 TylanceSvc(2172)[20] Information: [Tylance.Host.Analyzer.FileProcessor] GetFileStatus_QueryCloudSetResults
08:32:55 TyUpdate(10836)[1] Error: [UpdateMgr] EXCEPTION MESSAGE Could not connect to service control manager"""

@pytest.fixture
def log_file(tmp_path):
    # Create a temporary log file for testing
    log_path = tmp_path / "test_log.txt"
    log_path.write_text(LOG_CONTENT)
    return str(log_path)

# Positive Test Cases for 1a
def test_get_information_lines(log_file):
    lines = get_lines_by_severity(log_file, "Information")
    assert len(lines) == 3
    assert "Logging Started" in lines[0]

def test_get_error_lines(log_file):
    lines = get_lines_by_severity(log_file, "Error")
    assert len(lines) == 2
    assert "GetLogonTokenForImpersonatedTask" in lines[0]

def test_get_critical_lines(log_file):
    lines = get_lines_by_severity(log_file, "Critical")
    assert len(lines) == 1
    assert "The service has stopped" in lines[0]

# Positive Test Cases for 1b
def test_get_message_in_time_window(log_file):
    lines = get_lines_by_message_and_time(log_file, "Log", "07:22:54")
    assert len(lines) >= 1  # At least one line with "Log" within 30 mins
    assert "Log Rollover Event received" in lines[0]

# Negative Test Cases
def test_invalid_severity(log_file):
    lines = get_lines_by_severity(log_file, "Warning")
    assert len(lines) == 0  # No matches for invalid severity

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        get_lines_by_severity("nonexistent.txt", "Information")

def test_message_not_found(log_file):
    lines = get_lines_by_message_and_time(log_file, "Nonexistent", "07:22:54")
    assert len(lines) == 0  # No matches for message
