from PIL import  Image

imageObject = Image.open('./image-dataset/opel_insignia/0003.jpg')

cropped = imageObject.crop((90,70,320,260))

cropped.show()