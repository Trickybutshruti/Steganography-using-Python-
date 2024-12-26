from PIL import Image

# Function to encode a message into an image
def encode_message(image_path, message, output_image_path):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Convert the image to RGB (in case it's not)

    # Convert the message to binary (adding delimiter for end of message)
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # Delimiter: '1111111111111110'
    
    # Get the pixels of the image
    pixels = img.load()

    # Index to keep track of position in the binary message
    msg_index = 0
    for i in range(img.size[0]):  # Loop through image width (X)
        for j in range(img.size[1]):  # Loop through image height (Y)
            pixel = list(pixels[i, j])  # Get the RGB values of the pixel
            
            for k in range(3):  # Loop through R, G, and B channels
                if msg_index < len(binary_message):
                    # Modify the LSB (Least Significant Bit) of the current channel
                    pixel[k] = pixel[k] & 0xFE | int(binary_message[msg_index])  # Mask the last bit (clear it) and add the message bit
                    msg_index += 1

            # Update the pixel with the modified RGB values
            pixels[i, j] = tuple(pixel)
            
            # Stop if all bits from the message are embedded
            if msg_index >= len(binary_message):
                break
        if msg_index >= len(binary_message):
            break
    
    # Save the modified image
    img.save(output_image_path)
    print(f"Message encoded and saved to {output_image_path}")

# Function to decode the message from the image
def decode_message(image_path):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure it's in RGB format
    
    # Get the pixels of the image
    pixels = img.load()
    
    binary_message = ''
    
    for i in range(img.size[0]):  # Loop through image width (X)
        for j in range(img.size[1]):  # Loop through image height (Y)
            pixel = pixels[i, j]
            
            for k in range(3):  # Loop through R, G, and B channels
                # Extract the LSB (Least Significant Bit) of the current channel
                binary_message += str(pixel[k] & 1)
    
    # Split the binary message into chunks of 8 bits (1 byte)
    byte_message = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    
    # Convert the binary message back to text
    decoded_message = ''
    for byte in byte_message:
        if byte == '11111111':  # End of message delimiter
            break
        decoded_message += chr(int(byte, 2))
    
    return decoded_message

# Main function for user input
def main():
    print("Welcome to the Image Steganography System!")
    
    # User input for message and image paths
    message = input("Enter the message you want to encode: ")
    input_image = input("Enter the input image file path (e.g., 'input_image.png'): ")
    output_image = input("Enter the output image file path (e.g., 'encoded_image.png'): ")
    
    # Encode the message into the image
    encode_message(input_image, message, output_image)
    
    # Decode the message from the encoded image
    print("\nDecoding the message from the encoded image...")
    decoded_message = decode_message(output_image)
    print(f"Decoded Message: {decoded_message}")

# Run the program
if __name__ == "__main__":
    main()
