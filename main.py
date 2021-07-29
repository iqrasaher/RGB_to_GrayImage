from PIL import Image,ImageFont,ImageDraw
im=Image.open("images/parrot.jpg")
#print(im.width,im.height,im.mode,im.format,type(im))
#im.show()
im_g=im.convert("L")
im_g.save("images/parrot_gray.jpg")
Image.open("images/parrot_gray.jpg").show()
