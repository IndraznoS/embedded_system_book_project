# Makefile for building the embedded systems book

# Main LaTeX file
MAIN = main
# Output directory
OUTDIR = build

# LaTeX compiler
LATEX = pdflatex
# BibTeX compiler
BIBTEX = bibtex

# Compilation flags
LATEXFLAGS = -interaction=nonstopmode -halt-on-error -output-directory=$(OUTDIR)

.PHONY: all clean directories pdf view

all: pdf

# Create output directory
directories:
	@mkdir -p $(OUTDIR)

# Build PDF (run LaTeX multiple times for references)
pdf: directories
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	@echo "PDF built successfully: $(OUTDIR)/$(MAIN).pdf"

# Build with bibliography
pdf-bib: directories
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	cd $(OUTDIR) && $(BIBTEX) $(MAIN)
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	$(LATEX) $(LATEXFLAGS) $(MAIN).tex
	@echo "PDF with bibliography built successfully: $(OUTDIR)/$(MAIN).pdf"

# Clean build artifacts
clean:
	rm -rf $(OUTDIR)
	rm -f *.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg *.lol

# View PDF (requires a PDF viewer)
view: pdf
	@if command -v xdg-open > /dev/null; then \
		xdg-open $(OUTDIR)/$(MAIN).pdf; \
	elif command -v open > /dev/null; then \
		open $(OUTDIR)/$(MAIN).pdf; \
	else \
		echo "Please open $(OUTDIR)/$(MAIN).pdf manually"; \
	fi

# Help target
help:
	@echo "Available targets:"
	@echo "  make pdf       - Build the PDF document"
	@echo "  make pdf-bib   - Build PDF with bibliography"
	@echo "  make clean     - Remove build artifacts"
	@echo "  make view      - Build and view the PDF"
	@echo "  make help      - Show this help message"
