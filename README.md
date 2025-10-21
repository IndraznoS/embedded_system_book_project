# Embedded System Book Project

A comprehensive project for learning embedded systems using Arduino, featuring a LaTeX book, Arduino examples with PlatformIO, and Python data analysis tools.

## Project Structure

```
embedded_system_book_project/
├── book/                   # LaTeX documentation
│   ├── main.tex           # Main book document
│   ├── preamble.tex       # LaTeX preamble configuration
│   ├── chapters/          # Book chapters
│   │   ├── chapter01.tex # Introduction to Embedded Systems
│   │   └── chapter02.tex # Digital I/O and GPIO
│   ├── figures/           # Figures and diagrams
│   ├── Makefile          # Build automation for LaTeX
│   └── build/            # Compiled PDF output (generated)
│
├── arduino/               # PlatformIO Arduino projects
│   ├── platformio.ini    # PlatformIO configuration
│   ├── src/              # Main source code
│   │   └── main.cpp     # Default program
│   ├── include/          # Header files
│   ├── lib/              # Custom libraries
│   ├── test/             # Unit tests
│   └── examples/         # Chapter-specific examples
│       ├── chapter01_blink/
│       └── chapter02_button/
│
└── scripts/              # Python analysis tools
    ├── requirements.txt  # Python dependencies
    ├── serial_tools/     # Serial communication utilities
    │   └── serial_monitor.py
    └── data_analysis/    # Data analysis and visualization
        ├── plot_data.py
        └── analyze_sensor_data.py
```

## Getting Started

### Prerequisites

- **LaTeX**: TeX Live (Linux), MiKTeX (Windows), or MacTeX (macOS)
- **PlatformIO**: VS Code extension or CLI (`pip install platformio`)
- **Python 3.7+**: For analysis scripts
- **Arduino Board**: Uno, Mega, Nano, or compatible

### Building the Book

```bash
cd book
make pdf
```

The compiled PDF will be in `book/build/main.pdf`.

**Other make targets:**
- `make clean` - Remove build artifacts
- `make view` - Build and open PDF
- `make pdf-bib` - Build with bibliography

### Running Arduino Examples

```bash
cd arduino

# Build the project
pio run

# Upload to Arduino board
pio run -t upload

# Open serial monitor
pio device monitor
```

### Using Python Tools

```bash
cd scripts

# Install dependencies
pip install -r requirements.txt

# Monitor serial output
python serial_tools/serial_monitor.py /dev/ttyUSB0 9600

# Plot real-time data
python data_analysis/plot_data.py /dev/ttyUSB0 9600

# Analyze logged data
python data_analysis/analyze_sensor_data.py data.txt --plot
```

## Book Contents

The book covers:

1. **Introduction to Embedded Systems**
   - Characteristics and applications
   - Arduino platform overview
   - PlatformIO development environment

2. **Digital I/O and GPIO**
   - Digital signals and GPIO configuration
   - Reading buttons and controlling LEDs
   - Debouncing techniques

*(Additional chapters to be added)*

## Arduino Examples

Each chapter includes corresponding Arduino examples:

- **Chapter 1**: Basic LED blink program
- **Chapter 2**: Button input and LED control
- *(More examples for additional chapters)*

## Python Scripts

### Serial Monitor
Monitor and log Arduino serial output:
```bash
python serial_tools/serial_monitor.py PORT BAUDRATE --log output.txt
```

### Real-time Plotter
Visualize sensor data in real-time:
```bash
python data_analysis/plot_data.py PORT BAUDRATE
```

### Data Analyzer
Analyze logged sensor data with statistics and plots:
```bash
python data_analysis/analyze_sensor_data.py datafile.txt --plot
```

## Contributing

This is an educational project. Contributions, corrections, and improvements are welcome!

## License

This project is for educational purposes.

## Resources

- [Arduino Documentation](https://www.arduino.cc/reference/en/)
- [PlatformIO Documentation](https://docs.platformio.org/)
- [LaTeX Documentation](https://www.latex-project.org/)

## Author

Your Name

---

For detailed documentation, see the README files in each subdirectory.