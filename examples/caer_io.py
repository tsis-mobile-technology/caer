import caer

# Load Matplotlib to display our images
import matplotlib.pyplot as plt
from urllib.parse import urlparse

# Set a variable to store the current working dir
here = caer.path.cwd()

# Image path
tens_path = caer.path.join(here, 'thumbs', 'camera.jpg')

# URL
url = r"https://raw.githubusercontent.com/jasmcaus/caer/master/caer/data/beverages.jpg"

def imshow(tens):
    # We expect `tens` to be an RGB image (default in Caer)
    plt.imshow(tens)
    plt.xticks([]), plt.yticks([])  # Hides the graph ticks and x / y axis
    plt.margins(0,0)
    plt.show()

# Read one of the standard images that Caer ships with
tens = caer.imread(tens_path, rgb=True)

# To know which colorspace the Tensor is in, use:
print(f"Colorspace = {tens.cspace}")

imshow(tens)

# Read one of the standard images that Caer ships with
tens = caer.imread(url, rgb=True)

# To know which colorspace the Tensor is in, use:
print(f"Colorspace = {tens.cspace}")

imshow(tens)


# Read one of the standard images that Caer ships with
# target_size follows the (width,height) format
tens = caer.imread(tens_path, rgb=True, target_size=(200,180))

# Note that tens.shape might follow the (height, width) format as Caer uses Numpy to process
# images
print(f"Image shape = {tens.shape}")

imshow(tens)

# Read one of the standard images that Caer ships with
# target_size follows the (width,height) format
tens = caer.imread(url, rgb=True, target_size=(200,180), preserve_aspect_ratio=True)

# Note that tens.shape might follow the (height, width) format as Caer uses Numpy to process
# images
print(f"Image shape = {tens.shape}")

imshow(tens)

caer.imsave('beverages.jpg', tens)