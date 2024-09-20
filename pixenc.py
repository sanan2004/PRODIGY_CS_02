from PIL import Image
import numpy as np

def encrypt_image(path, key):
    # Open the image
    img = Image.open(path)
    
    # Convert the image to a NumPy array
    array = np.array(img)

    # Ensure key has the same shape as img_array
    key = np.resize(key, array.shape)

    # Encrypt each pixel using XOR with the key
    encrypted_array = np.bitwise_xor(array, key)
    
    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")


def decrypt_image(encrypted_path, key):
    
    encrypted_img = Image.open(encrypted_path)

    encrypted_array = np.array(encrypted_img)

    key = np.resize(key, encrypted_array.shape)

    decrypted_array = np.bitwise_xor(encrypted_array, key)
    
    decrypted_img = Image.fromarray(decrypted_array)
    
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")


def main():
    print("Image Encryption and Decryption using Pixel Manipulation")
    image_path = input("Enter the path to the image file: ")
    
    key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)

    #Encryption
    encrypt_image(image_path, key)
    
    # Decryption
    decrypt_image("encrypted_image.png", key)

if __name__ == "__main__":
    main()