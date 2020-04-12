# import cv2
#
#
# def get_position(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         print(f'x={x}, y={y}')
#
#
# image = cv2.imread(r"C:\Users\Michal\Desktop\computer-vision\asset\images.jpg")
#
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', get_position)
#
# cv2.imshow(winname='image', mat=image)
# cv2.waitKey(0)
# height, width = image.shape[ :2]
#
# print(f'wysokosc: {height}')
# print(f'szerkosc: {width}')
#
# cv2.line(img=image, pt1=(0,0), pt2=(width,height),color=(0,255,0), thickness=5)
# cv2.imshow(winname='logo', mat=image)
# cv2.waitKey(0)








