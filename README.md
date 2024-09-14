
# DrCorr Manual and Tutorial <!-- omit in toc -->
DrCorr (Drift Correction) is a Python piece of software which allows for the robust postprocessing and quantification of SMLM data. Originally build upon the concept of drift correction of SMLM data, over time expanded into quantitave analysis such as localization precision/SMLM image resolution via NeNA ([Endesfelder et. al, 2014](https://link.springer.com/article/10.1007/s00418-014-1192-3)) approach and clustering algorithms like DBSCAN ([Ester et al., 1996](https://dl.acm.org/doi/10.5555/3001460.3001507)) and OPTICS ([Ankerst et al., 1999](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.129.6542)). It is writen purely in Python and can be run with Python 3.7 or higher.

# Table of contents <!-- omit in toc -->
- [1. Download](#1-download)
- [2. Installation](#2-installation)
- [3. Theory/software principles](#3-theorysoftware-principles)
  - [3.1 Drift correction](#31-drift-correction)
  - [3.2 NeNA](#32-nena)
  - [3.3 DBSCAN clustering](#33-dbscan-clustering)
  - [3.4 OPTICS clustering](#34-optics-clustering)
- [4. Tutorial](#4-tutorial)
  - [4.1 Drift correction](#41-drift-correction)
  - [4.2 Calculating localization precision with NeNA](#42-calculating-localization-precision-with-nena)
  - [4.3 Clustering analysis with DBSCAN](#43-clustering-analysis-with-dbscan)
  - [4.4 Clustering analysis with OPTICS](#44-clustering-analysis-with-optics)
## 1. Download
There are two ways to download DrCorr:
* This solution is advised for people who have no experience with the git version control system (VCS). Click the green code button and select “[Download ZIP](https://github.com/Endesfelder-Lab/DrCorr/archive/refs/heads/master.zip)” option. Unpack the ZIP file. The disadvantage of this solution is the lack of version control, so you have to manually download each new update and unpack it.
* For people using git. Clone the repository. VCS will constantly check whether there is a new version of the software (sometimes the user has to manually enforce it) and will inform you to pull the changes with a single click.
  
## 2. Installation
* Be sure that you have installed Python, version >3.7 and the pip library is installed. If pip is not installed, [follow the manual](https://pip.pypa.io/en/stable/installation/)
* It is highly recommended to have a separate Python virtual environment for DrCorr. This way there will be no risk that certain libraries will be overwritten with different versions, which can break the code. It is also a general good practice to use separate virtual environments for each program/project to minimize the number of issues. To create a virtual environment, [follow the manual](https://docs.python.org/3/library/venv.html). Install the virtual environment in the same folder as DrCorr. 
* Open the command line/terminal and direct it to the main DrCorr folder where ```requirements.txt``` file is located. It consists of a list of all necessary libraries. Execute the following command in the commandline/terminal:\
```pip install -r requirements.txt```
* Meanwhile open in the explorer the same folder.
* Once the installation of libraries is finished, open the ```main.py``` file in a preferred editor (e.g. VSCode or Spyder) and run it. If the installation process was successful, you should see the main window of DrCorr.\
![](https://github.com/Endesfelder-Lab/DrCorr/blob/master/manual_images/image1.png)

## 3. Theory/software principles
### 3.1 Drift correction
Drift correction in DrCorr relies on bright fiducial markers that are added to the sample. <u>DrCorr doesn't provide a cross-correlation drift correction</u>. DrCorr computes the relative position (drift) of fiducial marker localizations in frames with respect to the first frame position. Next, the average drift in each frame is computed and smoothed with the Savitzky-Golay filter ([Savitzky and Golay, 1964](https://pubs.acs.org/doi/abs/10.1021/ac60214a047)). The user can manually set the window size for the filter.
### 3.2 NeNA
Please check [Endesfelder et. al, 2014](https://link.springer.com/article/10.1007/s00418-014-1192-3) for a theoretical overview and [Malkusch and Heilemann, 2015](https://www.nature.com/articles/srep34486) from which the piece of code responsible of NeNA was adapted and expanded.

### 3.3 DBSCAN clustering
Please check [Ester et al., 1996](https://dl.acm.org/doi/10.5555/3001460.3001507) for a theoretical overview. DrCorr uses the Python implementation of DBSCAN from the [sklearn library](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)

### 3.4 OPTICS clustering
Please check [Ankerst et al., 1999](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.129.6542) for a theoretical overview. DrCorr uses the Python implementation of DBSCAN from the [sklearn library](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html)

## 4. Tutorial
**WARNING! At the moment Calculate NeNA doesn’t work for Thunderstorm files. This feature will be implemented at one point.**
* Open the ```main.py``` file in a preferred editor (e.g. VSCode or Spyder) and run it.
* Before loading the localization file into Dr. Corr, you have to determine the format of your file in the dropdown menu at the top. Currently, two formats are recognized: RapidStorm (MALK) format and ThuderStorm format.
* **Fiducial Threshold**: In most cases, markers used for correcting the drift are bright fluorophores giving a high intensity/photon count in the localization file, therefore they can be safely filtered out from other localizations in the dataset. **Only events with intensities higher than the defined threshold will be considered as potential fiducial markers.** Check in your localization file what the typical intensity for your fluorophore of interest (FOI) and fiducial marker intensity, and set the threshold between these two values, preferably close, but below the fiducial marker intensity. This will reduce the probability of random noise being considered a fiducial marker signal.
* **Load Data**: Click this button to open the explorer and select your localization file. Upon selection, the file will be loaded automatically. Keep in mind that the loading time might vary based on the file size, e.g. loading STORM data will take significantly more time. Once the file is loaded, it generates an interactive image reconstruction which can be zoomed in and out. This interactive window can be closed and then reopened with the **Select ROIs** button and is an essential part of the analysis in Dr. Corr. With the right mouse button, you can mark different regions of interest (ROIs) to select fiducial markers for drift correction or NaNA, DBSCAN and/or OPTICS analysis. Selected regions are highlighted in green and have an identifier number next to them. Selected ROIs can be deleted with the next two buttons, which are pretty self-explanatory: **Delete last ROI** and **Delete all ROIs**.
### 4.1 Drift correction
![](https://github.com/Endesfelder-Lab/DrCorr/blob/master/manual_images/image2.png)
* Before opening the drift correction analysis window (**BeadAnalyzer**) with **Dr. corr** button select fiducial markers in the interactive window. The drift correction analysis window loads selected regions during the opening, therefore upon each new region you have to close and open the window every time. To reduce the headache with it it is recommended to select all interesting regions as they can be excluded in **BeadAnalyzer** if necessary.
* BeadAnalyzer consists of the following functionalities:
  * **Checkbox menu**: here are listed all selected fiducial markers. You can select and deselect them for further analysis.
  * **Analyze** button: analyzes and performs a drift correction of beads. It generates a couple of plots showing the drift in X and Y direction over time, what is the drift of individual beads AFTER the drift correction and what is the error of the drift correction over time. Based on these plots you can decide whether you want to discard some fiducials due to their strange behavior which impacts the quality of drift correction.
  * **Apply dr. corr.** button: Once you are satisfied with the drift correction, you can finally apply it to the entire dataset. **DrCorr will export a couple of files: localization file with corrected positions, beforementioned plots, reconstruction image of the input dataset with selected fiducials highlighted, the average drift trace used for drift correction, and drift corrected beads drifts.**
### 4.2 Calculating localization precision with NeNA
![](https://github.com/Endesfelder-Lab/DrCorr/blob/master/manual_images/image3.png)
* Similar to the drift correction analysis, you have to select ROIs before opening the NeNA window. Upon clicking it will open a window where you can set a couple of parameters for the model fit, lower and upper bounds for the NeNA parameter and the initial value of the NeNA parameter to improve the fit quality. The number of rows reflects the number of selected ROIs. Each row has two buttons on the right:
  * **Reset** button, which reset set parameters to defaults.
  * **Compute** button, which will perform a fit on a respective ROI, will display a histogram with the model fit on top of it, which allows us to evaluate the quality of fit.
* At the bottom there are another two buttons: 
  * **Compute all** button, which computes all beads separately.
  * **Save all** button, which saves the histograms into a single PDF file and generates a CSV table with NeNA values.
### 4.3 Clustering analysis with DBSCAN
![](https://github.com/Endesfelder-Lab/DrCorr/blob/master/manual_images/image4.png)
* Similar to the drift correction analysis, you have to select ROIs before opening the DBSCAN analysis window. Upon clicking it will open a window where you can set two parameters:
  * **Epsilon (radius)**, which defines the upper threshold of the neighbor search.
  * **MinPts**, which defines the minimal number of points (including the analyzed point) within epsilon to define the analyzed point as a core point of the cluster.
* After defining parameters, analysis is performed after pressing **Run DBSCAN** button. The output txt files per each ROI consist of spatial coordinates of localizations and the cluster id number for that localization, where the -1 value defines no cluster assignment.
### 4.4 Clustering analysis with OPTICS
![](https://github.com/Endesfelder-Lab/DrCorr/blob/master/manual_images/image4.png)
* Similar to the drift correction analysis, you have to select ROIs before opening the OPTICS analysis window. Upon clicking it will open a window where you can set two parameters:
  * **Upper limit**, which defines the upper threshold of the neighbor search. While by definition OPTICS uses only the MinPts parameter, the Python sklearn implementation optionally allows to set up the upper limit threshold that will speed up the analysis.
  * **MinPts**, which defines the minimal number of points (including the analyzed point) within epsilon to define the analyzed point as a core point of the cluster.
* After defining parameters, analysis is performed after pressing **Run OPTICS** button. There are two kinds of output txt files generated for each ROI:
  * Reachability distances: a list of reachability distances, which are used for ordering points.
  * List of localizations: a list of spatial coordinates of localizations, the cluster id number for that localization (same as for DBSCAN) and the reachability distance.
