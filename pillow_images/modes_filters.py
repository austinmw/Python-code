from PIL import Image
from PIL import ImageFilter

# Open image, check size
img = Image.open("sampleImage1.jpg")

# Modes
# Black and white 
black_white = img.convert("L")  # L: luminance (black & white)
black_white.show()

# Filters
blur = img.filter(ImageFilter.BLUR)
blur.show()

detail = img.filter(ImageFilter.DETAIL)
detail.show()

edges = img.filter(ImageFilter.FIND_EDGES)
edges.show()