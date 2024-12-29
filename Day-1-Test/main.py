import os
from PIL import Image

def pixelate_image(input_image_path, output_image_path, num_squares_width, num_squares_height):
    # Print the current working directory
    print("Current working directory:", os.getcwd())
    
    # Check if the image file exists
    if not os.path.exists(input_image_path):
        print(f"File not found: {input_image_path}")
        return
    
    # Open the input image
    original_image = Image.open(input_image_path)
    
    # Calculate the size of each pixel block
    pixel_size_width = original_image.width // num_squares_width
    pixel_size_height = original_image.height // num_squares_height
    
    # Resize the image to the desired number of squares
    small_image = original_image.resize(
        (num_squares_width, num_squares_height),
        resample=Image.NEAREST
    )
    
    # Resize the image back to the original size
    pixelated_image = small_image.resize(
        (original_image.width, original_image.height),
        Image.NEAREST
    )
    
    # Save the pixelated image
    pixelated_image.save(output_image_path)
    print(f"Pixelated image saved as {output_image_path}")

# Example usage
input_path = "C:/Users/xdweb/OneDrive/Documents/30-days-of-python/nser.png"  # Absolute path to your input image
output_path = "C:/Users/xdweb/OneDrive/Documents/30-days-of-python/nser_pixelated.png"  # Absolute path to save the pixelated image
num_squares_width = 20  # Number of squares along the width
num_squares_height = 20  # Number of squares along the height

# Print the contents of the directory to confirm the presence of the image
print("Contents of the directory:")
print(os.listdir("C:/Users/xdweb/OneDrive/Documents/30-days-of-python"))

pixelate_image(input_path, output_path, num_squares_width, num_squares_height)