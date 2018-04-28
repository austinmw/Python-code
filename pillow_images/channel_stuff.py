# Use Pillow to break image into individual channels
from PIL import Image

img = Image.open("sampleImage1.jpg")

# Make sure image is a 3-color channel
print(img.mode)

# Split image into channels
r, g, b = img.split()
# r.show()

# Merge channels
new_img = Image.merge("RGB", (r, g, b)) 
new_img.show()
new_img2 = Image.merge("RGB", (b, g, r)) # combined out of order 
new_img2.show()

# Combine channels from different images together
img2 = Image.open("sampleImage3.png")
print(img2.mode)
r2, g2, b2 = img2.split()
# new_img3 = Image.merge("RGB", (r, g, b2))   # need to be same size images