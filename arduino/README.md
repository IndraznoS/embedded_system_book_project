# Arduino Examples

This directory contains Arduino code examples for the Embedded Systems book, organized by chapter.

## Structure

```
arduino/
├── platformio.ini          # PlatformIO configuration
├── src/                    # Main source code
│   └── main.cpp           # Default main program
├── include/               # Header files
├── lib/                   # Custom libraries
├── test/                  # Unit tests
└── examples/              # Chapter-specific examples
    ├── chapter01_blink/
    ├── chapter02_button/
    └── ...
```

## Getting Started

### Prerequisites

- PlatformIO installed (VS Code extension or CLI)
- Arduino board (Uno, Mega, Nano, or compatible)
- USB cable for programming

### Building and Uploading

1. **Using PlatformIO CLI:**

```bash
# Build the project
pio run

# Upload to Arduino board
pio run -t upload

# Open serial monitor
pio device monitor
```

2. **Using VS Code:**

- Open this folder in VS Code
- Use PlatformIO toolbar buttons to build, upload, and monitor

### Running Examples

To run a specific example:

1. Copy the example code from `examples/` to `src/main.cpp`
2. Build and upload using PlatformIO

Or create a separate PlatformIO project for each example.

## Supported Boards

The `platformio.ini` file is configured for multiple Arduino boards:

- **uno**: Arduino Uno
- **mega2560**: Arduino Mega 2560
- **nano**: Arduino Nano

Select the environment when building:
```bash
pio run -e uno
pio run -e mega2560
pio run -e nano
```

## Serial Communication

Most examples use serial communication for debugging. Open the serial monitor at 9600 baud:

```bash
pio device monitor -b 9600
```

## Additional Resources

- [PlatformIO Documentation](https://docs.platformio.org/)
- [Arduino Reference](https://www.arduino.cc/reference/en/)
- Book chapters for detailed explanations
