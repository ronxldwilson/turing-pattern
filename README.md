# Turing Pattern Generator

This Python script generates Turing-like patterns by repeatedly applying blur and sharpen effects to an original image.

## Requirements

- Python 3.x
- Pillow (PIL) library

Install Pillow with: `pip install pillow`

## Usage

1. Place your original image as `original.jpg` in the same directory as the script.
2. Run the script: `python turing_pattern.py`
3. The resulting image will be saved as `turing_pattern.jpg`

## How it works

The script loads the original image and applies the following operations 1000 times:
- Blur the image
- Sharpen the image using UnsharpMask filter

This iterative process can create interesting pattern-like effects reminiscent of Turing patterns, though it's a simplified approximation.

## Note

Applying 1000 iterations on a large image may take some time and result in significant image degradation or noise amplification.
