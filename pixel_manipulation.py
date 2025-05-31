from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """
    Encrypt an image using XOR with a key
    """
    img = Image.open(input_path).convert('RGB')  # Ensure RGB
    img_array = np.array(img, dtype=np.uint8)    # Use uint8 to avoid overflow
    
    # XOR operation with the key
    encrypted_array = np.bitwise_xor(img_array, key)

    # Save without compression to avoid artifacts
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path, format='PNG')  # Use PNG for lossless save
    print(f"✅ Encrypted image saved as: {output_path}")

def decrypt_image(input_path, output_path, key):
    """
    Decrypt the image (same as encryption due to XOR reversibility)
    """
    img = Image.open(input_path).convert('RGB')
    img_array = np.array(img, dtype=np.uint8)
    
    # XOR again with the same key to decrypt
    decrypted_array = np.bitwise_xor(img_array, key)
    
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path, format='PNG')  # Use PNG for lossless save
    print(f"✅ Decrypted image saved as: {output_path}")

def main():
    while True:
        print("\n=== 🔐 Image XOR Encryption Tool ===")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            input_path = input("📥 Enter path of image to encrypt: ").strip()
            output_path = input("📤 Enter path to save encrypted image: ").strip()
            key = int(input("🔑 Enter encryption key (0-255): ").strip())
            if not 0 <= key <= 255:
                print("❌ Key must be between 0 and 255.")
                continue
            try:
                encrypt_image(input_path, output_path, key)
            except Exception as e:
                print("❌ Error:", e)

        elif choice == "2":
            input_path = input("📥 Enter path of encrypted image: ").strip()
            output_path = input("📤 Enter path to save decrypted image: ").strip()
            key = int(input("🔑 Enter decryption key (must be same as encryption): ").strip())
            if not 0 <= key <= 255:
                print("❌ Key must be between 0 and 255.")
                continue
            try:
                decrypt_image(input_path, output_path, key)
            except Exception as e:
                print("❌ Error:", e)

        elif choice == "3":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
