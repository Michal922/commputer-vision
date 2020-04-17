from PIL import  Image

imageObject = Image.open('./image-dataset/opel_insignia/0000.jpg')

cropped = imageObject.crop((50,20,300,300))

cropped.show()