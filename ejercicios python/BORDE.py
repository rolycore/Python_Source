from PIL import Image, ImageOps


imagen = Image.open("15.jpg")
imagen.size   # 500x200
imagen.mode   # RGB
imagenconborde = ImageOps.expand(imagen, border=5, fill=(0,0,255))
imagen.show()
imagenconborde.show()
imagenconborde.save("15borde.jpg")
