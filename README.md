Pixel Manipulation for Image Encryption

Objective: Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images

Procedure: This Python script utilizes the PIL (Python Imaging Library) and NumPy libraries to perform image encryption and decryption. Image encryption is achieved through a bitwise XOR operation between the image array and a randomly generated encryption key. Decryption is then conducted by applying the same XOR operation with the key.

Note: Before running this script, ensure that the PIL (Python Imaging Library) is installed. If it's not installed, you can do so using the command "pip install pillow".