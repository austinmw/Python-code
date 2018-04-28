# 3.4 = Pillow, 2.7 = PIL (PIL is 3.4 compatible, use it)
from PIL import Image 


# Open image
img = Image.open("sampleImage1.jpg")


# Print image size, format
print(img.size)
print(img.format)


# Crop image
area = (100, 100, 200, 200)  # (left, top, right, bottom)
cropped_img = img.crop(area)


# Display image
cropped_img.show() # opens with default image viewer, creates temp file name


# Combine images together
img1 = Image.open("sampleImage2.jpg")
img2 = cropped_img
area1 = (100, 100, 200, 200)
img1.paste(img2, area1)
img1.show()