#!/usr/bin/python3

import os
import numpy as np
import cv2
from numba import jit
import sys

import python_implementation as pi
import numba_implementation as nbi
import numpy_implementation as npi



def change_image_grayscale(input_file = "test.jpg", output_file = "gray_test.jpg", implementation_type = "numpy", scale_factor = 100):
	
	"""
	Changes an image to grayscale based on given arguments.

	Args:
		input_file (String): name of the file to be changed.
		output_file (String): name of the file to be saved as after applying the filter.
		implementation_type (String): specifies the implementation type to be used to change the image.
		scale_factor (int): number specifying how much percentage the image is supposed to be resized.	

	Returns:
		3d numpy array of the image.
		In addition it saves the newly created image as output_file
	"""

	image = None
	if(implementation_type == "numpy"):
		image = npi.grayscale_image(input_file)
	elif(implementation_type == "numba"):
		image = nbi.grayscale_image(input_file)
	elif(implementation_type == "python"):
		image = pi.grayscale_image(input_file)

	image = image.astype("uint8")
	if(scale_factor != None):
		width = int(image.shape[1] * int(scale_factor) / 100)
		height = int(image.shape[0] * int(scale_factor) / 100)
		new_size = (width, height)
		image = cv2.resize(image, new_size)
	if(output_file):
		cv2.imwrite(output_file, image)
	print("Done.")
	return image

def change_image_sepia(input_file = "test.jpg", output_file = "sepia_test.jpg", implementation_type = "numpy", scale_factor = 100):
	
	"""
	Changes an image to grayscale based on given arguments.

	Args:
		input_file (String): name of the file to be changed.
		output_file (String): name of the file to be saved as after applying the filter.
		implementation_type (String): specifies the implementation type to be used to change the image.
		scale_factor (int): number specifying how much percentage the image is supposed to be resized.	

	Returns:
		3d numpy array of the image.
		In addition it saves the newly created image as output_file
	"""

	image = None
	if(implementation_type == "numpy"):
		image = npi.sepia_image(input_file)
	elif(implementation_type == "numba"):
		image = nbi.sepia_image(input_file)
	elif(implementation_type == "python"):
		image = pi.sepia_image(input_file)
	image = image.astype("uint8")
	if(scale_factor != None):
		width = int(image.shape[1] * int(scale_factor) / 100)
		height = int(image.shape[0] * int(scale_factor) / 100)
		new_size = (width, height)
		image = cv2.resize(image, new_size)
	if(output_file):
		cv2.imwrite(output_file, image)
	print("Done.")
	return image



if __name__ == "__main__":

    change_image_sepia()
    change_image_grayscale()