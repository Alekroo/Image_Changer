#!/usr/bin/python3
import cv2
import os
import numpy as np

def grayscale_image(input_file, output_file=None):
	"""
	Changes an image to grayscale by the use of the numpy implementation

	Args:
		input_file (String): name of the file to be changed.
		output_file (String, optional): name of the file to be saved as after applying the filter.

	Returns:
		3d numpy array of the image.
		In addition it saves the newly created image as output_file if it is given.
		If input_file is not found, it warns the the user about it and quits.
		
	"""
	if(os.path.isfile(input_file)):
		image = cv2.imread(input_file)
		b = image[:, :, 0]
		g = image[:, :, 1]
		r = image[:, :, 2]

		img = ((b* 0.07) + (g* 0.72) + (r * 0.21))

		for y in range(3):	
			image[:,:,y] = img
	
		image = image.astype("uint8")
		if(output_file != None):
			cv2.imwrite(output_file, image)
		return image
	else:
		print("Could not find inputed file: '" + input_file + "'")
		quit()

def sepia_image(input_file, output_file=None):

	"""
	Changes an image to sepia by the use of the numpy implementation

	Args:
		input_file (String): name of the file to be changed.
		output_file (String, optional): name of the file to be saved as after applying the filter.

	Returns:
		3d numpy array of the image.
		In addition it saves the newly created image as output_file if it is given.
		If input_file is not found, it warns the the user about it and quits.
		
	"""

	if(os.path.isfile(input_file)):
		image = cv2.imread(input_file)
		new_img = np.empty((image.shape[0],image.shape[1],image.shape[2]))
		
		b = image[:,:,0]
		g = image[:,:,1]
		r = image[:,:,2]

		blue = r * 0.272 + g * 0.534 + b * 0.131
		green = r * 0.349 + g * 0.686 + b * 0.168
		red = r * 0.393 + g * 0.769 + b * 0.189

		new_img[:,:,0] = blue
		new_img[:,:,1] = green
		new_img[:,:,2] = red

		new_img[np.where(new_img>255)] = 255
		new_img = new_img.astype("uint8")
		if(output_file != None):
			cv2.imwrite(output_file, new_img)
		return new_img
	else:
		print("Could not find inputed file: '" + input_file + "'")
		quit()
