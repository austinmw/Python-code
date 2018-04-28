from PIL import Image

# Open image, check size
img = Image.open("sampleImage1.jpg")
print(img.size)

# Resize image
square_img = img.resize((250, 250)) # tuple
print(square_img.size)

# Flip Image
flip_img = square_img.transpose(Image.FLIP_LEFT_RIGHT)

# Spin Image
spin_img = square_img.transpose(Image.ROTATE_90)
spin_img.show()