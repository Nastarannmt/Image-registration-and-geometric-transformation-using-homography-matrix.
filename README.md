Image Registration and Geometric Transformation

This repository contains Python scripts and resources for correcting lens distortion, calculating homography matrices, and performing image registration on aerial (overhead) imagery. The workflow aims to produce spatially consistent images for analyzing changes in experimental alluvial fan. Please refer to "Apendix01_LensDistortionCorrectio_ImageRegistration.pdf" for more detailed info.

Step01_DistortionCorrection.py: Script to correct radial distortion using metadata and lens profiles.

Step02_Image_Matchingpoints_Selection.py: Script to manually or semi-automatically select corresponding key reference points.

Step03_HomographyMatrix.py: Script to calculate and apply the homography matrix, aligning images with the orthophoto.

Regirements

Python 3.7+, OpenCV (version 4.x or higher), NumPy, Matplotlib (optional, used for plotting and visualizing results), Adobe Photoshop (for lens correction steps; optional if you choose to replicate or automate lens correction differently)
