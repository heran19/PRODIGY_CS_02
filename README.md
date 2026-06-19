# Pixel Manipulation for Image Encryption
 
A Python program that encrypts and decrypts images using pixel manipulation. This project was completed as part of the **Prodigy InfoTech Cybersecurity Internship** (Task-02).
 
## About
 
This project demonstrates a simple yet effective image encryption technique based on pixel-level manipulation. Instead of operating on raw bytes or files, the program reads each pixel's RGB values and modifies them using a mathematical operation (XOR) combined with a user-defined key. The same operation, applied a second time with the same key, fully restores the original image.
 
## Features
 
- Encrypt any image by scrambling its pixel values
- Decrypt the scrambled image back to its original form using the same key
- Works on common image formats (JPG, PNG, etc.)
- Simple key-based system (0–255) controls the transformation
- Visual proof of encryption — encrypted image appears as noise/static
## How It Works
 
Each pixel in the image consists of three values: Red, Green, and Blue (RGB). The program applies a bitwise **XOR** operation between each color value and the chosen key:
 
```
new_value = pixel_value XOR key
```
 
XOR is used because it is reversible — applying the same operation with the same key twice returns the original value:
 
```
(pixel_value XOR key) XOR key = pixel_value
```
 
This means the exact same function can be used for both encryption and decryption, as long as the same key is used both times.
 
## Requirements
 
- Python 3.x
- Pillow library
Install Pillow with:
 
```bash
pip install Pillow
```
 
## Usage
 
1. Clone this repository or download the script.
```bash
git clone https://github.com/your-username/pixel-image-encryption.git
cd pixel-image-encryption
```
 
2. Run the script:
```bash
python image_encryption.py
```
 
3. Follow the prompts:
```
Enter key (0-255): 12
Encrypt or Decrypt (e/d): e
Input image path: C:\Users\Heran\Pictures\input.jpg
Output image path: C:\Users\Heran\Pictures\encrypted.jpg
Saved to C:\Users\Heran\Pictures\encrypted.jpg
```
 
4. To decrypt, run the script again using the **same key** and the encrypted image as input.
## Example
 
| Operation | Input Image | Key | Output |
|-----------|-------------|-----|--------|
| Encrypt | original.jpg | 12 | Scrambled/noisy image |
| Decrypt | encrypted.jpg | 12 | Original image restored |
 
## File Structure
 
```
pixel-image-encryption/
│
├── image_encryption.py   # Main program
└── README.md             # Project documentation
```
 
## Learning Outcomes
 
- Understanding how images are represented as pixel/RGB data
- Using the Pillow (PIL) library to read and write image files
- Applying bitwise XOR operations for reversible encryption
- Practical introduction to the principles behind image-based cryptography
## Acknowledgements
 
This project was completed as part of the Cybersecurity Internship offered by **Prodigy InfoTech**.
 
## License
 
This project is open source and available for educational purposes.
 
