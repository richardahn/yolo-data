'''
Written by Richard Ahn
'''

import sys, glob, os, shutil

def main():
	'''
		Argument Structure: "python order_class_labels.py dir1 dir2 dir3 ... "
		Orders classes based on order of arguments.
	'''
	classes = sys.argv[1:]
	print(classes)
	for cls in classes:
		print("Revising directory ", cls)
		cls_id = classes.index(cls)

		# Get txt files from directory
		directory = os.path.abspath(cls)

		for file in os.listdir(directory):
			if file.endswith(".txt"):
				# Open txt file
				print("Opening file ", file)
				txt_file_loc = "{}/{}".format(directory, file)
				with open(txt_file_loc, 'r+') as txt_file:
					# Modify line
					lines = txt_file.readlines()
					print(lines)
					new_lines = []
					for line in lines:
						print(line)
						t = list(line)
						t[0] = str(cls_id)
						new_line = "".join(t)
						print("into ", new_line)
						new_lines.append(new_line)

					print(new_lines)
					# Write new line
					txt_file.seek(0)
					for new_line in new_lines:
						txt_file.write(new_line)
					txt_file.truncate()
				print()


if __name__ == "__main__":
	main()