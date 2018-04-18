'''
Written by Richard Ahn

How to Use:
Place this file into the annotations folder of the hand dataset. Run this script, and
it will make a subfolder that contains bbox labels. 
'''

import scipy.io as sio
import sys
import os
import glob

CONVERTED_DIRNAME = 'bbox_labels'

def convert(box):
	minX = sys.maxsize
	minY = sys.maxsize
	maxX = -1
	maxY = -1
	for corner in box:
		x = corner[0]
		y = corner[1]
		if x < minX:
			minX = x
		if x > maxX:
			maxX = x
		if y < minY:
			minY = y
		if y > maxY:
			maxY = y

	# Round the values to integers
	minX = int(round(minX))
	minY = int(round(minY))
	maxX = int(round(maxX))
	maxY = int(round(maxY))
	return [minX, minY, maxX, maxY]


def convert_mat(filename):

	# Read and convert contents
	mat_contents = sio.loadmat(filename)
	boxes = mat_contents['boxes'][0]
	new_boxes = []
	for box in boxes:
		# Get rid of wrapping arrays
		box = box[0][0]

		# Obtain the corners
		corner1 = box[0][0]
		corner2 = box[1][0]
		corner3 = box[2][0]
		corner4 = box[3][0]

		# Convert the corners into bbox format
		box = [corner1, corner2, corner3, corner4]
		new_box = convert(box)
		new_boxes.append(new_box)

	return new_boxes


def main():
	# Write contents into BBox format
	global CONVERTED_DIRNAME
	try:
		os.mkdir(CONVERTED_DIRNAME)
	except:
		pass

	# Get all the .mat files in the current directory
	wd = os.path.abspath(os.getcwd())
	files = glob.glob(os.path.join(wd, "*.mat"))
	for file in files:
		print("Converting ", file)

		# Obtain the bbox from the .mat file
		bbox = convert_mat(file)

		# Create a new bbox annotation label
		(cd, fname) = os.path.split(file)
		file_name = fname[:-4]
		converted_file_name = os.path.join(wd, CONVERTED_DIRNAME)
		converted_file_name = os.path.join(converted_file_name, file_name + '.txt')
		with open(converted_file_name, 'w') as f:
			for box in bbox:
				print("Writing box...")
				print(box)
				f.write(str(0) + os.linesep)
				box_line = "{} {} {} {}".format(box[0], box[1], box[2], box[3])
				f.write(box_line + os.linesep)

		print()

if __name__ == "__main__":
	main()