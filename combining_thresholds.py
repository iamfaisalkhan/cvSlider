
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle

def abs_sobel_thresh(img, orient='x', sobel_kernel=(1, 15), thresh=(0, 255)):
    # 1) Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 2) Take the derivative in x or y given orient = 'x' or 'y'
    orient_mask = [1, 0]
    if orient == 'y':
        orient_mask = [0, 1]
    
    sobel = cv2.Sobel(gray, cv2.CV_64F, orient_mask[0], orient_mask[1])
    # 3) Take the absolute value of the derivative or gradient
    
    abs_sobel = np.absolute(sobel)
    # 4) Scale to 8-bit (0 - 255) then convert to type = np.uint8
    scaled = np.uint8(255 * abs_sobel / np.max(abs_sobel) )
    # 5) Create a mask of 1's where the scaled gradient magnitude 
            # is > thresh_min and < thresh_max
    binary_output = np.zeros_like(scaled)
    # 6) Return this mask as your binary_output image
    binary_output[(scaled >= thresh[0]) & (scaled <= thresh[1])] = 1
    
    return binary_output

def mag_thresh(img, sobel_kernel=(1, 12), mag_thresh_min=(0, 255), mag_thresh_max = (0, 255) ):
        # Apply the following steps to img
    # 1) Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 2) Take the gradient in x and y separately
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    # 3) Calculate the magnitude 
    
    sobelxy = np.sqrt(sobelx**2 + sobely**2)
    # 4) Scale to 8-bit (0 - 255) and convert to type = np.uint8
    
    scaled_sobelxy = np.uint8(255 * sobelxy / np.max(sobelxy) )
    # 5) Create a binary mask where mag thresholds are met
    mask =  ((scaled_sobelxy >= mag_thresh_min) & (scaled_sobelxy <= mag_thresh_max) )
    # 6) Return this mask as your binary_output image
    binary_output = np.zeros_like(scaled_sobelxy)
    binary_output[mask] = 1
    
    return binary_output

def dir_threshold(img, sobel_kernel=(1,15), min_value=(0, np.pi), max_value=(0, np.pi) ):
	    # Apply the following steps to img
    # 1) Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 2) Take the gradient in x and y separately
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    # 3) Take the absolute value of the x and y gradients
    abs_sobelx = np.absolute(sobelx)
    abs_sobely = np.absolute(sobely)
    # 4) Use np.arctan2(abs_sobely, abs_sobelx) to calculate the direction of the gradient 
    gradient_dir = np.arctan2(abs_sobely, abs_sobelx)
    
    # 5) Create a binary mask where direction thresholds are met
    # 6) Return this mask as your binary_output image
    binary_output = np.zeros_like(abs_sobelx, dtype=np.uint8)
    binary_output[(gradient_dir >= min_value) & (gradient_dir <= max_value)] = 1
    
    return binary_output

def abs_sobel_threshx(image, sobel_kernel=(1, 15), min_val=(0, 255), max_val=(0, 255)):
    return abs_sobel_thresh(image, 'x', sobel_kernel, (min_val, max_val))

def abs_sobel_threshy(image, sobel_kernel=(1, 15), min_val=(0, 255), max_val=(0, 255)):
    return abs_sobel_thresh(image, 'y', sobel_kernel, (min_val, max_val))

def combined_threshold(image, sobel_kernel=(3, 15), 
                               sobelx_min=(0, 255),
                               sobelx_max=(0, 255),
                               sobely_min=(0, 255),
                               sobely_max=(0, 255),
                               mag_thresh_min=(0, 255),
                               mag_thresh_max=(0, 255),
                               dir_thresh_min=(0.0, np.pi),
                               dir_thresh_max=(0.0, np.pi)):

    # Choose a Sobel kernel size
    ksize = 9 # Choose a larger odd number to smooth gradient measurements

    # Apply each of the thresholding functions
    gradx = abs_sobel_threshx(image, ksize, sobelx_min, sobelx_max)
    grady = abs_sobel_threshy(image, ksize, sobely_min, sobely_max)
    mag_binary = mag_thresh(image, ksize, mag_thresh_min, mag_thresh_max)
    dir_binary = dir_threshold(image, ksize, dir_thresh_min, dir_thresh_max)

    combined = np.zeros_like(dir_binary)
    combined[((gradx == 1) & (grady == 1)) | ((mag_binary == 1) & (dir_binary == 1))] = 1

    return combined

if __name__ == "__main__":

    image = mpimg.imread('signs_vehicles_xygrad.png')
	# Choose a Sobel kernel size
    ksize = 9 # Choose a larger odd number to smooth gradient measurements

    combined = combined_threshold(image, ksize, 0, 100, 0, 100, 0, 100, 0, np.pi/2)

    plt.imshow(combined, cmap='gray')
    plt.show()

    # combined = np.zeros_like(dir_binary)
    #combined[((gradx == 1) & (grady == 1)) | ((mag_binary == 1) & (dir_binary == 1))] = 1

