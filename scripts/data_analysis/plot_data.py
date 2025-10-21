"""
Data Plotter

Reads numerical data from serial port and plots it in real-time.
Useful for visualizing sensor readings, PWM values, etc.

Usage:
    python plot_data.py /dev/ttyUSB0 9600
"""

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import argparse
import sys


class SerialPlotter:
    def __init__(self, port, baudrate, max_points=100):
        """
        Initialize the serial plotter.
        
        Args:
            port: Serial port name
            baudrate: Communication speed
            max_points: Maximum number of points to display
        """
        self.port = port
        self.baudrate = baudrate
        self.max_points = max_points
        
        # Data storage
        self.data = deque(maxlen=max_points)
        self.time = deque(maxlen=max_points)
        self.counter = 0
        
        # Serial connection
        self.ser = None
        
        # Plot setup
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], 'b-')
        
        self.ax.set_xlabel('Sample')
        self.ax.set_ylabel('Value')
        self.ax.set_title(f'Real-time Data from {port}')
        self.ax.grid(True)
    
    def init_plot(self):
        """Initialize plot elements."""
        self.line.set_data([], [])
        return self.line,
    
    def update_plot(self, frame):
        """Update plot with new data."""
        try:
            # Open serial if not already open
            if self.ser is None or not self.ser.is_open:
                self.ser = serial.Serial(self.port, self.baudrate, timeout=0.1)
            
            # Read data from serial
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8', errors='replace').strip()
                
                try:
                    # Try to parse as float
                    value = float(line)
                    self.data.append(value)
                    self.time.append(self.counter)
                    self.counter += 1
                    
                    # Update plot
                    self.line.set_data(list(self.time), list(self.data))
                    
                    # Adjust axes
                    if len(self.data) > 0:
                        self.ax.set_xlim(min(self.time), max(self.time) + 1)
                        data_min = min(self.data)
                        data_max = max(self.data)
                        margin = (data_max - data_min) * 0.1 or 1
                        self.ax.set_ylim(data_min - margin, data_max + margin)
                
                except ValueError:
                    # Not a number, skip
                    pass
        
        except serial.SerialException as e:
            print(f"Serial error: {e}")
        
        return self.line,
    
    def start(self):
        """Start the plotter."""
        try:
            ani = animation.FuncAnimation(
                self.fig, self.update_plot, init_func=self.init_plot,
                interval=50, blit=True
            )
            plt.show()
        
        except KeyboardInterrupt:
            print("\nStopping plotter...")
        
        finally:
            if self.ser and self.ser.is_open:
                self.ser.close()


def main():
    parser = argparse.ArgumentParser(description='Real-time Serial Data Plotter')
    parser.add_argument('port', help='Serial port (e.g., /dev/ttyUSB0 or COM3)')
    parser.add_argument('baudrate', type=int, default=9600,
                        help='Baud rate (default: 9600)')
    parser.add_argument('--points', type=int, default=100,
                        help='Maximum points to display (default: 100)')
    
    args = parser.parse_args()
    
    plotter = SerialPlotter(args.port, args.baudrate, args.points)
    plotter.start()


if __name__ == '__main__':
    main()
