# Quick Start Guide

This guide will help you get started with the Embedded System Book Project quickly.

## Setup (5 minutes)

### 1. Install Prerequisites

#### LaTeX (for building the book)
- **Linux**: `sudo apt-get install texlive-full`
- **macOS**: Download MacTeX from https://www.tug.org/mactex/
- **Windows**: Download MiKTeX from https://miktex.org/

#### PlatformIO (for Arduino development)
- **VS Code Extension** (recommended): Search "PlatformIO" in VS Code extensions
- **CLI**: `pip install platformio`

#### Python Tools (for data analysis)
```bash
cd scripts
pip install -r requirements.txt
```

### 2. Clone the Repository

```bash
git clone https://github.com/IndraznoS/embedded_system_book_project.git
cd embedded_system_book_project
```

## Quick Tasks

### Build the Book (2 minutes)

```bash
cd book
make pdf
```

Output: `book/build/main.pdf`

### Run Arduino Example (5 minutes)

1. Connect your Arduino board via USB

2. Build and upload:
```bash
cd arduino
pio run -t upload
```

3. Open serial monitor:
```bash
pio device monitor
```

You should see "LED: ON" and "LED: OFF" messages and the built-in LED blinking!

### Visualize Sensor Data (3 minutes)

1. Upload Arduino code that prints sensor values:
```cpp
void loop() {
    int value = analogRead(A0);
    Serial.println(value);
    delay(100);
}
```

2. Run the plotter:
```bash
cd scripts
python data_analysis/plot_data.py /dev/ttyUSB0 9600
```

*(Use COM3, COM4, etc. on Windows)*

## Project Structure at a Glance

```
📚 book/          → LaTeX book source (build with: make pdf)
🤖 arduino/       → PlatformIO projects (upload with: pio run -t upload)
🐍 scripts/       → Python tools (run with: python script_name.py)
```

## Common Commands

### LaTeX Book
```bash
cd book
make pdf          # Build PDF
make clean        # Remove build files
make view         # Build and open PDF
```

### Arduino/PlatformIO
```bash
cd arduino
pio run           # Compile
pio run -t upload # Upload to board
pio device list   # List connected devices
pio device monitor # Serial monitor
```

### Python Tools
```bash
cd scripts

# Serial monitor with logging
python serial_tools/serial_monitor.py /dev/ttyUSB0 9600 --log data.txt

# Real-time plotter
python data_analysis/plot_data.py /dev/ttyUSB0 9600

# Analyze logged data
python data_analysis/analyze_sensor_data.py data.txt --plot
```

## Troubleshooting

### Can't find serial port?
```bash
# Linux/Mac
ls /dev/tty*
# or
pio device list

# Windows: Check Device Manager → Ports (COM & LPT)
```

### LaTeX compilation errors?
```bash
cd book
make clean
make pdf
```

### PlatformIO not found?
```bash
pip install platformio
# Restart terminal
```

### Python package missing?
```bash
cd scripts
pip install -r requirements.txt
```

## Next Steps

1. **Read the Book**: Open `book/build/main.pdf`
2. **Try Examples**: Explore `arduino/examples/`
3. **Modify Code**: Edit `arduino/src/main.cpp` and upload
4. **Collect Data**: Use Python scripts to analyze sensor data

## Getting Help

- Check README.md files in each directory
- Review the book chapters for detailed explanations
- Consult PlatformIO documentation: https://docs.platformio.org/
- Arduino reference: https://www.arduino.cc/reference/

Happy learning! 🚀
