
# Steganography using Least Significant Bit (LSB)

This repository contains a Python-based implementation of the Least Significant Bit (LSB) steganography technique. LSB steganography allows users to hide secret messages within images without significantly altering their appearance. The project provides both encoding (hiding a message in an image) and decoding (extracting the hidden message) functionalities.

## Features

- **Encode Messages**: Hide a secret message in an image.
- **Decode Messages**: Retrieve the hidden message from an encoded image.
- **Simple Interface**: Designed for ease of use.
- **Flexible Input**: Works with `.png` images for lossless data hiding.

## Requirements

Ensure you have the following Python libraries installed:
- `Pillow` (for image manipulation)
- `numpy` (for efficient data processing)

You can install the required libraries using the following command:

```bash
pip install Pillow numpy
```

## How It Works

1. **Encoding Process**:
   - The secret message is converted into binary format.
   - Each bit of the message is embedded into the least significant bit of the image's pixel values.
   - The modified image is saved as a new file.

2. **Decoding Process**:
   - Reads the least significant bits of the image's pixel values.
   - Reconstructs the binary data to retrieve the hidden message.

This process ensures that the changes in the image are imperceptible to the human eye.

## Usage

### Encoding a Message

1. Provide the input image (e.g., `input.png`) and the secret message to hide.
2. Run the encoding script:

```python
python encode.py --input input.png --message "Your secret message" --output encoded_image.png
```

### Decoding a Message

1. Provide the encoded image (e.g., `encoded_image.png`).
2. Run the decoding script:

```python
python decode.py --input encoded_image.png
```

