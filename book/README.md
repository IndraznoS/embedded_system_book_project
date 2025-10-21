# Embedded Systems Book

LaTeX source for the "Embedded Systems: A Practical Guide with Arduino" book.

## Structure

- `main.tex` - Main document that includes all chapters
- `preamble.tex` - LaTeX preamble with package configurations
- `chapters/` - Individual chapter files
- `figures/` - Images and diagrams
- `build/` - Compiled output directory (generated)

## Building the Book

### Using Make (Recommended)

```bash
make pdf        # Build the PDF
make clean      # Remove build artifacts
make view       # Build and open the PDF
make pdf-bib    # Build with bibliography
```

### Manual Compilation

```bash
# Create build directory
mkdir -p build

# Compile (run multiple times for references)
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

## Adding Content

### Adding a New Chapter

1. Create a new file in `chapters/`, e.g., `chapter03.tex`
2. Add `\input{chapters/chapter03.tex}` to `main.tex`
3. Rebuild the document

### Adding Figures

1. Place image files in the `figures/` directory
2. Reference in LaTeX:

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{filename.png}
    \caption{Your caption here}
    \label{fig:your_label}
\end{figure}
```

3. Reference in text: `As shown in Figure~\ref{fig:your_label}...`

### Adding Code Listings

The preamble includes a custom style for Arduino code:

```latex
\begin{lstlisting}[caption=Your Caption]
void setup() {
    pinMode(13, OUTPUT);
}

void loop() {
    digitalWrite(13, HIGH);
    delay(1000);
}
\end{lstlisting}
```

## Preamble Features

The `preamble.tex` file includes:

- **Packages**: Graphics, tables, code listings, hyperlinks
- **Code Highlighting**: Custom Arduino/C++ style
- **Circuit Diagrams**: CircuiTikZ support
- **Custom Commands**: `\code{}`, `\register{}`
- **Headers/Footers**: Fancy page headers

## Requirements

### LaTeX Distribution

- **Linux**: TeX Live (`sudo apt-get install texlive-full`)
- **macOS**: MacTeX (https://www.tug.org/mactex/)
- **Windows**: MiKTeX (https://miktex.org/)

### Required Packages

Most packages are included in full distributions. Key packages:
- `geometry` - Page layout
- `graphicx` - Graphics support
- `listings` - Code listings
- `xcolor` - Color support
- `hyperref` - Hyperlinks
- `circuitikz` - Circuit diagrams
- `fancyhdr` - Headers and footers
- `titlesec` - Section formatting

## Tips

- Run `make pdf` multiple times if cross-references aren't resolved
- Use `\label{}` and `\ref{}` for cross-references
- Keep figure files in PDF or PNG format for best quality
- Use vector graphics (PDF) when possible
- Check the log file in `build/` if compilation fails

## Troubleshooting

### Missing Packages

If you get "File not found" errors:
```bash
# TeX Live (Linux)
sudo tlmgr update --all

# MiKTeX (Windows)
# Use MiKTeX Console to install missing packages
```

### References Not Working

Run LaTeX multiple times:
```bash
make clean
make pdf
```

### Figures Not Found

Ensure `\graphicspath{{figures/}}` is set in preamble and files are in `figures/` directory.
