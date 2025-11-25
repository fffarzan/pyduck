from PIL import Image, ImageFilter

img = Image.open('/Users/farzan/projs/python/hello/projs/img-playground/Pokedex/pikachu.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)

fb_img = img.filter(ImageFilter.BLUR)
fb_img.save("blur.png", "png") # png supports these filters not jpg

fs_img = img.filter(ImageFilter.SMOOTH)
fs_img.save("smooth.png", "png")

c_img = img.convert('L')
c_c_img = c_img.rotate(90)
r_c_c_img = c_c_img.crop((100, 100, 400, 400))
r_c_c_img.save("grey.png", "png")
r_c_c_img.show()

# thumbnail method

# OpenCV library