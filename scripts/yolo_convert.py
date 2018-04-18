import cv2
import os
import sys
import glob

CONVERTED_DIRNAME = 'yolo_labels'

def convert(vals, width, height):
	newvals = [0]*5
	newvals[0] = vals[0] - 1
	newvals[1] = float(vals[1] + vals[3])/(2*width)
	newvals[2] = float(vals[2] + vals[4])/(2*height)
	newvals[3] = float(vals[3] - vals[1])/width
	newvals[4] = float(vals[4] - vals[2])/height
	return newvals

def main():
	global CONVERTED_DIRNAME
	try:
		os.mkdir(CONVERTED_DIRNAME)
	except:
		pass
	CURDIR = os.path.abspath(os.getcwd())
	img_files = glob.glob(os.path.join(CURDIR,"*.jpg"))
	for img_file in img_files:
		print("Working on ", img_file)
		(cd, fname) = os.path.split(img_file)
		fileid = fname[:-4]
		labelname = fileid + '.txt'
		boxes = []

		# Open image to get dimensions
		img = cv2.imread(img_file)
		height, width = img.shape[:2]

		# Open bbox label 
		with open(labelname, 'r') as f:
			lines = f.readlines()
			print("THE LINES ARE")
			print(lines)
			for i in range(int(len(lines)/2)):
				cls = lines[2*i+0].replace('\n', '')
				vals_str = lines[2*i+1].replace('\n', '')
				vals = [int(x) for x in vals_str.split(' ')]
				print("THE VALS IS:")
				print(vals)
				vals.insert(0, int(cls))
				boxes.append(convert(vals, width, height))

		print("BOXES:")
		print(boxes)


		# Convert bbox to yolo and write
		newfilename = os.path.join(CURDIR, CONVERTED_DIRNAME)
		newfilename = os.path.join(newfilename, labelname)
		with open(newfilename, 'w') as f:
			for box in boxes:
				line = ' '.join([str(x) for x in box])
				f.write(line + os.linesep)


if __name__ == "__main__":
	main()
