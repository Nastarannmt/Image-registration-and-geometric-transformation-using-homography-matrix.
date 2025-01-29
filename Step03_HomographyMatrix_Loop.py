import cv2
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# Function to compute mean reprojection error
def compute_reprojection_error(src_pts, dst_pts, H):
    projected_pts = cv2.perspectiveTransform(src_pts.reshape(-1, 1, 2), H)
    errors = np.sum((projected_pts - dst_pts.reshape(-1, 1, 2))**2, axis=2).ravel()
    return np.sqrt(np.mean(errors))

output_directory = "/Users/nastaran/Documents/Python/output/transformed_image"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

orthophoto_coordinates_csv = pd.read_csv("/Users/nastaran/Documents/Python/output/matching_points_coordinates/Ortho_im_coordinates.csv")
corrected_im_coordinates_csv = pd.read_csv("/Users/nastaran/Documents/Python/output/matching_points_coordinates/corrected_im_coordinates.csv")

orthophoto_coordinates = orthophoto_coordinates_csv.values.astype('float32')
corrected_im_coordinates = corrected_im_coordinates_csv.values.astype('float32')

H, mask = cv2.findHomography(corrected_im_coordinates, orthophoto_coordinates, cv2.RANSAC)
orthophoto = cv2.imread('/Users/nastaran/Documents/Python/Input_data/Ortho_image_fantable.tif')
height, width, channels = orthophoto.shape

directory_path = "/Users/nastaran/Documents/Python/output/corrected_image"

for filename in os.listdir(directory_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filepath = os.path.join(directory_path, filename)
        
        corrected_im = cv2.imread(filepath)
        corrected_im_transformed = cv2.warpPerspective(corrected_im, H, (width, height))
        
        # Calculate mean reprojection error
        error = compute_reprojection_error(corrected_im_coordinates, orthophoto_coordinates, H)
        print(f"Mean Reprojection Error for {filename}: {error:.4f} pixels")
        
        # Create an overlay of the images
        overlay = cv2.addWeighted(orthophoto, 1, corrected_im_transformed, 0.5, 0)
        
        # Use matplotlib to display the overlay
        #plt.imshow(cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB))
        #plt.title(f"Overlay of {filename}")
        #plt.show()
        
        # Save the output image
        output_path = os.path.join(output_directory, filename)
        cv2.imwrite(output_path, corrected_im_transformed)
