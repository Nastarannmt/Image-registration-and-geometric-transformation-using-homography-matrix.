import os
import time
from comtypes.client import CreateObject

# path to raw images captured with over head camera
path = "/Users/nastaran/Documents/Python/Input_data/raw_image/DSC_0001.jpg"
output_path = os.path.join(os.path.dirname(path), "corrected_image")

# Create output directory if it doesn't exist
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Initialize Photoshop Application
psApp = CreateObject("Photoshop.Application")

# Ensure that Photoshop becomes visible
psApp.Visible = True

# Define constants (these are provided by Photoshop's Scripting API)
psDoNotSaveChanges = 2
psJPEGSaveOptions = CreateObject("Photoshop.JPEGSaveOptions")

# You can set the quality of JPEG here (1 to 12, 12 being the best)
psJPEGSaveOptions.Quality = 12

# Iterate through all files in the folder
for img_file in os.listdir(path):
    img_path = os.path.join(path, img_file)

    print("Opening:", img_path)  # <-- this should be here, inside the loop

    if os.path.isfile(img_path) and img_file.lower().endswith(('.jpg')):
        try:
            # Open the image in Photoshop
            doc = psApp.Open(img_path)

            # Apply the "Lens Correction" action
            psApp.DoAction("Lens Correction", "Default Actions")

            # Save and close the modified image
            corrected_image_path = os.path.join(output_path, img_file)
            doc.SaveAs(corrected_image_path, psJPEGSaveOptions, True, psDoNotSaveChanges)
            doc.Close(psDoNotSaveChanges)
            
            # Pause for a second to make sure Photoshop can keep up
            time.sleep(1)
        except Exception as e:
            print(f"Error processing {img_file}. Reason: {e}")

# Close Photoshop Application
psApp.Quit()
