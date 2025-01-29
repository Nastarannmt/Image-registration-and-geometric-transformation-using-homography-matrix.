"""
Script: select_points.py

Description:
    This script allows the user to interactively select coordinates in a displayed image 
    and save those coordinates to a CSV file. The image displayed here is the 
    "corrected image" output from Step 01 in our lens correction workflow. 
    However, you can also run this script on the reference image (Ortho_image_fantable.tif) to collect 
    matching points in both images.

"""

import matplotlib.pyplot as plt  # For creating plots
import pandas as pd              # For creating .csv file

# Path to the image (change this for reference vs. corrected image)
image_path = '/Users/nastaran/Documents/Python/output/DSC_0001_corrected.jpg'
output_csv = 'corrected_im_coordinates.csv'

# List to save coordinates that we click on the image
coords = []

def onclick(event):
    """Callback function that is called when an image is clicked."""
    global coords
    coords.append((event.xdata, event.ydata))
    
    # Clear the previous annotations
    ax.clear()
    
    # Display the image
    ax.imshow(image)
    
    # Add annotations for each selected point
    for x, y in coords:
        ax.scatter(x, y, color='red', marker='o')
    
    # Refresh the plot
    plt.draw()

# Read the image from the specified path
image = plt.imread(image_path)

# Display the image
fig, ax = plt.subplots()
ax.imshow(image)

# Connect the callback function to mouse click event
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Show the image with the interface to select points
plt.show()

# Convert the coordinates to a pandas DataFrame
df = pd.DataFrame(coords, columns=['x', 'y'])

# Write the DataFrame to a .csv file
df.to_csv(output_csv, index=False)
print(f"Coordinates saved to {output_csv}")
