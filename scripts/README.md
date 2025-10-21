# Python Scripts

This directory contains Python scripts for interacting with Arduino projects and analyzing data.

## Structure

```
scripts/
├── requirements.txt        # Python dependencies
├── serial_tools/          # Serial communication utilities
│   └── serial_monitor.py # Serial port monitor with logging
└── data_analysis/         # Data analysis tools
    ├── plot_data.py       # Real-time data plotter
    └── analyze_sensor_data.py # Sensor data analyzer
```

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Or with a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Tools

### Serial Monitor (`serial_tools/serial_monitor.py`)

Monitor serial output from Arduino and optionally log to a file.

**Usage:**
```bash
# Basic monitoring
python serial_tools/serial_monitor.py /dev/ttyUSB0 9600

# On Windows
python serial_tools/serial_monitor.py COM3 9600

# With logging
python serial_tools/serial_monitor.py /dev/ttyUSB0 9600 --log data.txt
```

### Real-time Data Plotter (`data_analysis/plot_data.py`)

Plot numerical data from Arduino in real-time.

**Usage:**
```bash
python data_analysis/plot_data.py /dev/ttyUSB0 9600

# Adjust number of points displayed
python data_analysis/plot_data.py /dev/ttyUSB0 9600 --points 200
```

**Arduino Code Example:**
```cpp
void loop() {
    int sensorValue = analogRead(A0);
    Serial.println(sensorValue);  // Send value to plotter
    delay(100);
}
```

### Sensor Data Analyzer (`data_analysis/analyze_sensor_data.py`)

Analyze logged sensor data and generate statistics.

**Usage:**
```bash
# Show statistics
python data_analysis/analyze_sensor_data.py data.txt

# Show statistics and plots
python data_analysis/analyze_sensor_data.py data.txt --plot
```

## Common Workflows

### 1. Monitor and Log Arduino Output

```bash
python serial_tools/serial_monitor.py /dev/ttyUSB0 9600 --log session.txt
```

### 2. Visualize Sensor Data in Real-time

```bash
python data_analysis/plot_data.py /dev/ttyUSB0 9600
```

### 3. Analyze Logged Data

```bash
python data_analysis/analyze_sensor_data.py session.txt --plot
```

## Finding Serial Ports

### Linux/Mac
```bash
ls /dev/tty*
# Arduino usually appears as /dev/ttyUSB0 or /dev/ttyACM0
```

### Windows
```bash
# Check Device Manager -> Ports (COM & LPT)
# Arduino usually appears as COM3, COM4, etc.
```

### Using PlatformIO
```bash
pio device list
```

## Tips

- Make sure Arduino is sending data via `Serial.println()` for the tools to work
- Use consistent baud rates between Arduino code and Python scripts
- Close other serial monitors before running these scripts
- Use Ctrl+C to stop any running script

## Dependencies

- **pyserial**: Serial port communication
- **numpy**: Numerical computing
- **matplotlib**: Data visualization
- **pandas**: Data manipulation (optional)
- **scipy**: Scientific computing (optional)
