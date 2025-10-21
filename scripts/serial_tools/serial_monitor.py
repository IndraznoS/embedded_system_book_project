"""
Serial Monitor Tool

A simple Python script to read data from Arduino via serial port
and optionally log it to a file.

Usage:
    python serial_monitor.py /dev/ttyUSB0 9600
    python serial_monitor.py COM3 9600 --log data.txt
"""

import serial
import argparse
import sys
from datetime import datetime


def monitor_serial(port, baudrate, log_file=None):
    """
    Monitor serial port and display/log data.
    
    Args:
        port: Serial port name (e.g., '/dev/ttyUSB0' or 'COM3')
        baudrate: Communication speed (e.g., 9600)
        log_file: Optional file path to log data
    """
    try:
        # Open serial connection
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Connected to {port} at {baudrate} baud")
        print("Press Ctrl+C to stop\n")
        
        # Open log file if specified
        log = None
        if log_file:
            log = open(log_file, 'a')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log.write(f"\n--- Session started at {timestamp} ---\n")
            print(f"Logging to {log_file}\n")
        
        # Read and display data
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='replace').strip()
                timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                output = f"[{timestamp}] {line}"
                
                print(output)
                
                if log:
                    log.write(output + '\n')
                    log.flush()
    
    except serial.SerialException as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n\nStopping monitor...")
    
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed")
        
        if log:
            log.close()
            print(f"Log file closed: {log_file}")


def main():
    parser = argparse.ArgumentParser(description='Arduino Serial Monitor')
    parser.add_argument('port', help='Serial port (e.g., /dev/ttyUSB0 or COM3)')
    parser.add_argument('baudrate', type=int, default=9600, 
                        help='Baud rate (default: 9600)')
    parser.add_argument('--log', '-l', dest='log_file', 
                        help='Log file path (optional)')
    
    args = parser.parse_args()
    
    monitor_serial(args.port, args.baudrate, args.log_file)


if __name__ == '__main__':
    main()
