Python pixel manipulation for image encryption. By utilizing cryptographic methods and libraries such as NumPy and Pillow, the security of individual pixel values is improved through substitution, permutation, and diffusion. The implementation's potential for reliable and effective image encryption—critical for safeguarding digital information—is emphasized by a comparison with traditional approaches.

I have utilized the mathemaatical Operaton XOR to perform both Encryption and Decryption.
Each byte in the bytearray is XORed with the key, which alters the binary data of the image, rendering it unreadable by standard image viewers.

Important Notes:
The encryption key must be the same for both encryption and decryption. If different keys are used, the decryption will fail.
The XOR operation is symmetric, meaning applying it twice with the same key will restore the original data.
This method is effective for simple encryption but may not be secure enough for sensitive data.

Lastly when giving input ensure the correct format .

Example Usage:
Enter the path of the image:        C:\Users\USER\Downloads\ace.jpg
Enter the encryption key (0-255):   18


