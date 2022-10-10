from PIL import Image,ImageChops
image1 = Image.open('new.jpg')
image2 = Image.open('new1.jpg')
diff=ImageChops.difference(image1,image2)
if diff.getbbox():
    diff.show()
