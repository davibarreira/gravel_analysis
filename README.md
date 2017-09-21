# MLND - Capstone Project
Capstone project for Udacity's Machine Learning Engineer Nanodegree

## Problem Statement
In this project, a Convolutional Neural Network is used to estimate the texture index of aggregates. As input, the model uses images, while the output is the texture index obtained using the Aggregate Image Measurement System (AIMS) equipment.

## Dataset
The images and respective texture indexes were provided by the Department of Transport Engineering (DET) of the Federal University of Ceara (UFC).
The DataPreparation.ipynb notebook contains the code responsible for preparing the data in the right format to be run in the other notebooks.
The ExtractionData.ipynb notebook is not necessary. It was previously used to get the data from the original folders and organize them in the current repository.

## Requisits
The project uses Python 3.5, and the following libraries need to be installed:
- Numpy
- Pandas
- matplotlib
- Seaborn
- scikit-learn
- tensorflow
- Pillow
- scipy

To find which version is being used, check the *requirements.txt* file.


## Notebooks
- DateExtraction: This Notebook was used to adjust the original data format. The files are already properly organized in the repository, so this Notebook doesn't need to be run.
- DataPreparation: This Notebook is used to remove images that are erros, adjust the quality of the images, save them as a numpy array, leaving the data prepared to be used in Keras.
- DataExploration: This Notebook produces some statistics and visualizations of the original dataset, such as the distribution of the Texture Index.
- CNN_Model: This Notebook is used to train the CNNs and evaluate their results. It also contains the image quality analysis.

## Report
The *proposal.pdf* contains the Project Proposal.
The actual project report is in the file *report.pdf*.
