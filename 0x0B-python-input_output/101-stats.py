#!/usr/bin/python3
import sys
import signal

"""Dictionary to store status code counts"""

status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}

total_file_size = 0
line_count = 0

def print_metrics(signum, frame):
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def process_line(line):
    global total_file_size
    global line_count

    try:
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[-2]
            file_size = parts[-1]

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            total_file_size += int(file_size)
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(None, None)

    except Exception as e:
        pass

"""Register the SIGINT signal (CTRL + C) to trigger the print_metrics function"""

signal.signal(signal.SIGINT, print_metrics)

try:
    for line in sys.stdin:
        process_line(line)
except KeyboardInterrupt:
    pass

print_metrics(None, None)
