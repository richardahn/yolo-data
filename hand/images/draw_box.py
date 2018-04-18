import cv2
import numpy as np

def main():
	img = cv2.imread('VOC2010_1000.jpg')
	with open('VOC2010_1000.txt') as f:
		content = f.readlines()
		h, w = img.shape[:2]
		for box in content:
			box = box.split()
			xCenter = float(box[1])
			yCenter = float(box[2])
			width = float(box[3])
			height = float(box[4])

			xCenter = xCenter * w
			yCenter = yCenter * h
			width = width * w
			height = height * h


			p1x = int(xCenter - width/2)
			p1y = int(yCenter - height/2)
			p2x = int(xCenter + width/2)
			p2y = int(yCenter + height/2)
			# BUG, SWITCH THE Y AND X
			# BUG 2, hand sizes for our original images are off
			cv2.rectangle(img, (p1x, p1y), (p2x, p2y), (255,0,0), 5)

		cv2.imshow('image', img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

if __name__ == '__main__':
	main()