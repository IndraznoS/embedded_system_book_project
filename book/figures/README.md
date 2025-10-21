# Figures Directory

This directory contains figures and diagrams used in the book.

## Adding Figures

Place image files (PNG, PDF, JPG) in this directory and reference them in LaTeX using:

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{filename.png}
    \caption{Figure description}
    \label{fig:label}
\end{figure}
```

## Recommended Tools

- **Circuit Diagrams**: Fritzing, KiCad
- **Block Diagrams**: draw.io, Inkscape
- **Plots and Graphs**: Python matplotlib, MATLAB
- **Screenshots**: Platform-specific tools

## File Naming Convention

Use descriptive names with chapter prefixes:
- `ch01_arduino_board.png`
- `ch02_led_circuit.pdf`
- `ch03_pwm_waveform.png`
