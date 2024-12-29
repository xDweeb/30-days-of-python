from PIL import Image, ImageDraw
import numpy as np

# Use relative paths
input_image_path = 'pic.jpg'
output_image_path = 'traced_image2.jpg'

# Load the image
image = Image.open(input_image_path)

# Get pixel data
pixels = np.array(image)
height, width = pixels.shape[:2]

# Create a new image for tracing
# The output image will have the same dimensions as the input but with a grid drawn
grid_image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(grid_image)

# Draw the pixel grid based on the image's actual pixels
for y in range(height):
    for x in range(width):
        color = tuple(pixels[y, x][:3])  # Get RGB color of the pixel
        draw.rectangle([x, y, x + 1, y + 1], fill=color, outline="black")

# Save the traced image
grid_image.save(output_image_path)
print(f"Traced image saved to {output_image_path}")
