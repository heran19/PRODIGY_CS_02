from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Saved to {output_path}")

# XOR encryption is symmetric - same function decrypts
key = int(input("Enter key (0-255): "))
mode = input("Encrypt or Decrypt (e/d): ").lower()
input_path = input("Input image path: ")
output_path = input("Output image path: ")

encrypt_image(input_path, output_path, key)
