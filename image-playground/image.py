from PIL import Image, ImageFilter

# # using PIL
# img = Image.open('./Pokedex/206_pikachu.jpg')
# # filter_img = img.filter(ImageFilter.SHARPEN)
# filter_img = img.convert('L')
# resize = filter_img.resize((200, 200))
# resize.save("resized.png", 'png')
# # resize.show()

img1 = Image.open("./Pokedex/208_astro.jpg")
# resizing and keeping the original aspect ratio
img1.thumbnail((350, 350))
img1.save("astrnt.png", "png")
print(img1.size)
