def encrypt_image(image_path, output_path, key):
    # Open the image file in binary mode for reading
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Convert binary data to byte array
    byte_array = bytearray(image_data)

    # Encrypt the byte array using XOR operation with the key
    for i in range(len(byte_array)):
        byte_array[i] ^= key

    # Write the encrypted byte array to a new file
    with open(output_path, "wb") as encrypted_file:
        encrypted_file.write(byte_array)

    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(encrypted_image_path, output_path, key):
    # Open the encrypted image file in binary mode for reading
    with open(encrypted_image_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Convert binary data to byte array
    byte_array = bytearray(encrypted_data)

    # Decrypt the byte array using XOR operation with the same key
    for i in range(len(byte_array)):
        byte_array[i] ^= key

    # Write the decrypted byte array to a new file
    with open(output_path, "wb") as decrypted_file:
        decrypted_file.write(byte_array)

    print(f"Image decrypted and saved to {output_path}")

# Taking inputs from the user
image_path = input("Enter the path of the image: ").strip('"')
output_encrypted_path = "encrypted_image.png"
output_decrypted_path = "decrypted_image.png"
key = int(input("Enter the encryption key (0-255): "))

# Encrypt the image
encrypt_image(image_path, output_encrypted_path, key)

# Decrypt the image
decrypt_image(output_encrypted_path, output_decrypted_path, key)
