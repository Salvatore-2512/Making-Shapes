import cv2 as cv 
import numpy as np

img = np.zeros((518,518,3),np.uint8)

print (img)
img[:] = 255,255,255

cv.rectangle(img,(400,400),(300,300),(255,0,0),cv.FILLED)

new_triangle_vertices = np.array([[50, 200], [150, 50], [250, 200]], np.int32)
new_triangle_vertices = new_triangle_vertices.reshape((-1, 1, 2))

cv.polylines(img, [new_triangle_vertices], isClosed=True, color=(255, 255, 255), thickness=6)
cv.fillPoly(img, [new_triangle_vertices], color=(0, 0, 255))

hexagon_vertices = np.array([[50, 250], [150, 250], [200, 350], [150, 450], [50, 450], [0, 350]], np.int32)


hexagon_vertices = hexagon_vertices.reshape((-1, 1, 2))



cv.polylines(img, [hexagon_vertices], isClosed=True, color=(255, 255, 255), thickness=6)
cv.fillPoly(img, [hexagon_vertices], color=(0, 128, 0))

pentagon_vertices = np.array([[250,300], [250, 200], [350, 100], [400, 200], [400, 300]], np.int32)

pentagon_vertices = pentagon_vertices.reshape((-1, 1, 2))

cv.polylines(img, [pentagon_vertices], isClosed=True, color=(255, 255, 255), thickness=2)
cv.fillPoly(img, [pentagon_vertices], color=(128, 0, 128))




cv.imshow("Image", img)

cv.waitKey(0)
