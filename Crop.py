from PIL import Image

img = Image.open("2020-03-22.png")

print(img.size )

comp = img.crop((0,0,1920/10,1080/10))

img.paste(im=comp,box=(0,0))