import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the points from the CSVs
orthophoto_coordinates_csv = pd.read_csv("/Users/nastaran/Documents/Python/output/matching_points_coordinates/Ortho_im_coordinates.csv")
corrected_im_coordinates_csv = pd.read_csv("/Users/nastaran/Documents/Python/output/matching_points_coordinates/corrected_im_coordinates.csv")

# Assuming your points are in the format (x, y) for each image
orthophoto_coordinates = orthophoto_coordinates_csv.values.astype('float32')
corrected_im_coordinates = corrected_im_coordinates_csv.values.astype('float32')

# Compute the homography matrix
H, mask = cv2.findHomography(corrected_im_coordinates, orthophoto_coordinates, cv2.RANSAC)

# Use this matrix to transform the corrected image to the orthophoto perspective
orthophoto = cv2.imread('/Users/nastaran/Documents/Python/Input_data/Ortho_image_fantable.tif')
corrected_im = cv2.imread('/Users/nastaran/Documents/Python/output/Corrected_image.jpg')
height, width, channels = orthophoto.shape
corrected_im_transformed = cv2.warpPerspective(corrected_im, H, (width, height))

# Save the output image
cv2.imwrite('corrected_im_transformed.jpg', corrected_im_transformed)

# Overlay the transformed corrected image on the orthophoto
overlay = cv2.addWeighted(orthophoto, 0.5, corrected_im_transformed, 0.5, 0)
# Show the orthophoto and the overlay side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.imshow(cv2.cvtColor(orthophoto, cv2.COLOR_BGR2RGB))
#ax1.set_title('Orthophoto')
ax1.axis('off')
ax2.imshow(cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB))
#ax2.set_title('Overlay of Corrected Image Transformed on Orthophoto')
ax2.axis('off')
plt.show()
9