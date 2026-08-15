from PIL import Image
import os

def resize_image(input_path, output_path, width, height):
    image = Image.open(input_path)
    resized = image.resize((width, height))
    resized.save(output_path)
    print(f"✅ Image resized and saved to {output_path}")

print("╔══════════════════════════════════╗")
print("║      🖼️  IMAGE RESIZER 🖼️        ║")
print("╚══════════════════════════════════╝")

input_path = input("\nEnter image path: ")
width = int(input("Enter new width: "))
height = int(input("Enter new height: "))

filename = os.path.basename(input_path)
output_path = f"resized_{filename}"

resize_image(input_path, output_path, width, height)