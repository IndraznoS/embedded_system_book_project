"""
Sensor Data Analyzer

Analyzes logged sensor data and generates statistics and plots.

Usage:
    python analyze_sensor_data.py data.txt
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def parse_log_file(filename):
    """
    Parse log file and extract numerical data.
    
    Args:
        filename: Path to log file
    
    Returns:
        List of numerical values
    """
    data = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines and session markers
            if not line or line.startswith('---'):
                continue
            
            # Try to extract number from line
            try:
                # Try to parse the entire line as float
                value = float(line)
                data.append(value)
            except ValueError:
                # Try to find a number in the line
                parts = line.split()
                for part in parts:
                    try:
                        value = float(part)
                        data.append(value)
                        break
                    except ValueError:
                        continue
    
    return data


def analyze_data(data):
    """
    Calculate statistics for the data.
    
    Args:
        data: List of numerical values
    
    Returns:
        Dictionary of statistics
    """
    if not data:
        return None
    
    arr = np.array(data)
    
    stats = {
        'count': len(arr),
        'mean': np.mean(arr),
        'median': np.median(arr),
        'std': np.std(arr),
        'min': np.min(arr),
        'max': np.max(arr),
        'range': np.max(arr) - np.min(arr)
    }
    
    return stats


def plot_data(data, filename):
    """
    Create visualization plots for the data.
    
    Args:
        data: List of numerical values
        filename: Original filename for plot title
    """
    if not data:
        print("No data to plot")
        return
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle(f'Sensor Data Analysis: {filename}')
    
    # Time series plot
    axes[0, 0].plot(data, 'b-', linewidth=0.5)
    axes[0, 0].set_xlabel('Sample')
    axes[0, 0].set_ylabel('Value')
    axes[0, 0].set_title('Time Series')
    axes[0, 0].grid(True)
    
    # Histogram
    axes[0, 1].hist(data, bins=30, edgecolor='black')
    axes[0, 1].set_xlabel('Value')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].set_title('Distribution')
    axes[0, 1].grid(True)
    
    # Box plot
    axes[1, 0].boxplot(data)
    axes[1, 0].set_ylabel('Value')
    axes[1, 0].set_title('Box Plot')
    axes[1, 0].grid(True)
    
    # Rolling average (if enough data)
    if len(data) > 10:
        window = min(20, len(data) // 5)
        rolling_avg = np.convolve(data, np.ones(window)/window, mode='valid')
        axes[1, 1].plot(data, 'b-', alpha=0.3, label='Raw')
        axes[1, 1].plot(range(window-1, len(data)), rolling_avg, 'r-', 
                       linewidth=2, label=f'Rolling Avg (w={window})')
        axes[1, 1].set_xlabel('Sample')
        axes[1, 1].set_ylabel('Value')
        axes[1, 1].set_title('Smoothed Data')
        axes[1, 1].legend()
        axes[1, 1].grid(True)
    else:
        axes[1, 1].text(0.5, 0.5, 'Not enough data\nfor rolling average', 
                       ha='center', va='center', transform=axes[1, 1].transAxes)
    
    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description='Analyze sensor data from log file')
    parser.add_argument('filename', help='Log file to analyze')
    parser.add_argument('--plot', action='store_true', 
                       help='Generate plots')
    
    args = parser.parse_args()
    
    print(f"Analyzing {args.filename}...")
    
    # Parse data
    data = parse_log_file(args.filename)
    
    if not data:
        print("No numerical data found in file")
        return
    
    print(f"Found {len(data)} data points\n")
    
    # Calculate statistics
    stats = analyze_data(data)
    
    if stats:
        print("Statistics:")
        print(f"  Count:   {stats['count']}")
        print(f"  Mean:    {stats['mean']:.3f}")
        print(f"  Median:  {stats['median']:.3f}")
        print(f"  Std Dev: {stats['std']:.3f}")
        print(f"  Min:     {stats['min']:.3f}")
        print(f"  Max:     {stats['max']:.3f}")
        print(f"  Range:   {stats['range']:.3f}")
    
    # Generate plots if requested
    if args.plot:
        plot_data(data, args.filename)


if __name__ == '__main__':
    main()
