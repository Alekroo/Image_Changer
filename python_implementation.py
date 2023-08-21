#!/usr/bin/python3	
import os
import numpy as np
import cv2

def grayscale_image(input_file, output_file=None):

	"""
	Changes an image to grayscale by the use of the pure python implementation

	Args:
		input_file (String): name of the file to be changed.
		output_file (String, optional): name of the file to be saved as after applying the filter.

	Returns:
		3d numpy array of the image.
		In addition, it saves the newly created image as output_file if it is given.
		If input_file is not found, it warns the the user about it and quits.
		
	"""

	if(os.path.isfile(input_file)):
		image = cv2.imread(input_file)
		height = image.shape[0]
		width = image.shape[1]
		for x in range(height):
			for y in range(width):
				image[x][y] = (image[x][y][0] * 0.07) + (image[x][y][1] * 0.72) + (image[x][y][2] * 0.21) 
		image = image.astype("uint8")
		if(output_file != None):
			cv2.imwrite(output_file, image)
		return image
	else:
		print("Could not find inputed file: '" + input_file + "'")
		quit()

def sepia_image(input_file, output_file=None):
	
	"""
	Changes an image to sepia by the use of the pure python implementation

	Args:
		input_file (String): name of the file to be changed.
		output_file (String, optional): name of the file to be saved as after applying the filter.

	Returns:
		3d numpy array of the image.
		In addition, it saves the newly created image as output_file if it is given.
		If input_file is not found, it warns the the user about it and quits.
		
	"""

	if(os.path.isfile(input_file)):
		image = cv2.imread(input_file)
		height = image.shape[0]
		width = image.shape[1]
		
		for x in range(height):
			for y in range(width):
				b,g,r = image[x][y]
				blue = int(r * 0.272 + g * 0.534 + b * 0.131)
				green = int(r * 0.349 + g * 0.686 + b * 0.168)
				red = int(r * 0.393 + g * 0.769 + b * 0.189)
				if blue > 255:
					blue = 255
				if green > 255:
					green = 255
				if red > 255:
					red = 255
				image[x][y] = blue, green, red
		image = image.astype("uint8")
		if(output_file != None):
			cv2.imwrite(output_file, image)
		return image
	else:
		print("Could not find inputed file: '" + input_file + "'")
		quit()
