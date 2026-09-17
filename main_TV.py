# AI Statement: AI was not used to generate any code for this assignment. Instead, it was used to help determine the cause of an error message in my scatter plot code that I could not figure out. (I had a capital Patient when it should have been lowercase)

from patient_TV import *

# Imports necessary libraries
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics

# Creates patient objects directly from the .csv file without having to manually type them in
Patient.instantiate_from_csv("C:/Users/tmvit/OneDrive/Desktop/BME 2315/Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv")

# Sorts patient objects that were just created from the csv file by years of education (least to greatest)
Patient.allPatients.sort(key=Patient.get_yearsOfEducation, reverse=False)
for patient in Patient.allPatients:
    print(patient) # Prints the sorted patient objects

# Filters and prints subset of patient objects who have dementia (cognitive status) and who have the APOE genotype of 3_3 (most common in the general population)
dementia33Patient = Patient.filter(Patient.allPatients, cognitiveStatus = "Dementia", APOEgenotype = "3_3")
print(dementia33Patient)




# Making bar graph below
# Lists for bar graph: one for tTAU concentration in females with dementia and one for males with dementia
tTAUFemale = []
tTAUMale = []

# Filling bar graph lists with data from dataset: evaluating tTAU concentration in females and males with dementia
# tTAU levels for each gender go in separate lists to analyze later
for patient in Patient.filter(Patient.allPatients, sex = "Female", cognitiveStatus = "Dementia"):
    tTAUFemale.append(patient.tTAU)
for patient in Patient.filter(Patient.allPatients, sex = "Male", cognitiveStatus = "Dementia"):
    tTAUMale.append(patient.tTAU)

# Assigns the mean of the tTAU concentration for both male and female patients to separate variables which will be visible on the bar graph
x_tTAUbarF = (statistics.mean(tTAUFemale))
x_tTAUbarM = (statistics.mean(tTAUMale))

# Assigns the standard deviation of the tTAU concentration for both the male and female patients to separate variables
tTAUbarF_stdev = (statistics.stdev(tTAUFemale))
tTAUbarM_stdev = (statistics.stdev(tTAUMale))

# Prints the mean and standard deviation of both the female and male groups for the graph
print(f'x_tTAUbarF = {x_tTAUbarF}, tTAUbarF_stdev {tTAUbarF_stdev}')
print(f'x_tTAUbarM = {x_tTAUbarM}, tTAUbarM_stdev {tTAUbarM_stdev}')

patientSex_cols = ['Female', 'Male'] # Defines the columns as female and male
mean_tTAU = [x_tTAUbarF, x_tTAUbarM] # Calculates the mean between the two variables
std_tTAU = [tTAUbarF_stdev, tTAUbarM_stdev] # Calculates the standard deviation between the two variables
yerr = [np.zeros(len(mean_tTAU)), std_tTAU] # Creates vertical error values

# Plots the bar graph using the columns and mean tTAU previously defined in blue and orange color
plt.bar(patientSex_cols, mean_tTAU, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("tTAU Levels in Female vs Male Patients with Dementia") # Main title of the graph
plt.xlabel("Sex") # X-axis label on graph
plt.ylabel("tTAU (pg/ug)") # Y-axis label on graph
plt.show() # Creates bar graph



# Making scatter plot below
# Lists for scatter plot: one for patient age at death and one for pTAU concentration
patientAge = []
patientpTAU = []

# Filling scatter plot lists with data from dataset to analyze age at death vs pTAU concentration
# Patient age at death gets its own list and so does pTAU concentration to analyze in the scatter plot
for patient in Patient.allPatients:
    patientAge.append(patient.age)
for patient in Patient.allPatients:
    patientpTAU.append(patient.pTAU)

# X variable becomes the data stored in patient age at death, and y variable becomes the data stored in pTAU concentration
X = [patientAge]  # Independent variable
y = [patientpTAU]   # Dependent variable

# Plots the scatter plot with the previously defined x and y variables in the color blue
plt.scatter(X, y, color='blue')
plt.xlabel('Age at Death') # X axis label
plt.ylabel('pTAU (pg/ug)') # Y axis label
plt.title('Scatter Plot of Age at Death vs pTAU Concentration') # Main title of scatter plot
plt.show() # Prints the scatter plot