from PIL import Image, ImageDraw
import numpy as np
import os

# Debugging: Check the current directory and its contents
print("Current working directory:", os.getcwd())
print("Contents of the directory:", os.listdir())

# Input and output paths
input_image_path = 'nser.png'  # Ensure pic.jpg is in the same directory
output_image_path = 'nser.jpg'

# Verify if the input file exists
if not os.path.exists(input_image_path):
    print(f"Error: File '{input_image_path}' not found. Please check the file location.")
    exit()

# Load the image
image = Image.open(input_image_path)

# Resize the image to make it easier to trace each pixel
grid_size = 16  # Adjust to control the number of squares
image = image.resize((grid_size, grid_size), Image.NEAREST)

# Get pixel data
pixels = np.array(image)
height, width = pixels.shape[:2]

# Create a new image for tracing
grid_image = Image.new("RGB", (width * 10, height * 10), "white")  # Enlarged for visibility
draw = ImageDraw.Draw(grid_image)

# Draw the pixel grid and color each square
for y in range(height):
    for x in range(width):
        color = tuple(pixels[y, x][:3])  # Get RGB color of the pixel
        x0, y0 = x * 10, y * 10  # Top-left corner of the square
        x1, y1 = x0 + 10, y0 + 10  # Bottom-right corner of the square
        draw.rectangle([x0, y0, x1, y1], fill=color, outline="black")

# Save the traced image
grid_image.save(output_image_path)
print(f"Traced image saved to {output_image_path}")

# Display the number of squares
print(f"Number of squares: {width} x {height} = {width * height}")
