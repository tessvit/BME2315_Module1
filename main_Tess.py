# AI Statement: AI was not used to generate any code for this assignment. Instead, it was used to help determine the cause of an error message in my scatter plot code that I could not figure out. (I had a capital Patient when it should have been lowercase)

from patient_Tess import *

# Imports necessary libraries
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics
import pandas as pd
from sklearn.linear_model import LinearRegression

# import pandas as pd
# df = pd.read_csv("C:/Users/tmvit/OneDrive/Desktop/BME 2315/Module 0/BME2315_Module1/Metadata and Protein Data for Module 1.csv")

# for header in df.columns:
#     print(header)

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

# Code below creates T-test statistic using the female and male tTAU concentrations
t_stat, p_val = stats.ttest_ind(tTAUFemale, tTAUMale)
print(f't_stat = {t_stat}, p_val = {p_val}')

# # One-way ANOVA test code -- in this case I can't use this code since I only compare two sets of data on my bar graph; this is used for 3 or more variables
# f_stat, p_value = stats.f_oneway(ABeta42_health_fem_vals, ABeta42_health_male_vals, ABeta42_diseased_fem_vals, ABeta42_diseasd_male_vals)
# print("F-statistic:", f_stat)
# print("p-value:", p_value)
# plt.text(1.5, 380, f"One-Way-ANOVA: p = {p_value:.3f}",
# ha='right', va='top', fontsize=12)

# Plots the bar graph using the columns and mean tTAU previously defined in blue and orange color
plt.bar(patientSex_cols, mean_tTAU, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("tTAU Levels in Female vs Male Patients with Dementia") # Main title of the graph
plt.xlabel("Sex") # X-axis label on graph
plt.ylabel("tTAU (pg/ug)") # Y-axis label on graph
# Below is the code for the text on the graph
plt.text(
        0.5, 700, # This establishes where the code will be on the graph: 0.5 on x-axis (middle) and maximum y value on y-axis
        f"t = {t_stat:.2f}\np = {p_val:.3e}", # This brings the statistics and tells the system to round to 2 or 3 decimals
        ha = 'center', # Centers text horizontally at the x value
        va = 'bottom' # Centers bottom of text vertically at the y value
        )
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

# Below reshapes the X and y values into an array for analyzing the slope and intercept of the line of best fit.
X = np.array(patientAge).reshape(-1,1)
y = np.array(patientpTAU)

# Establishes the Linear Regression model fit
model = LinearRegression()
model.fit(X,y)

# The slope, intercept, and r2 value variables are defined and assigned their values
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)

# The equation is formed and then plotted on the scatter plot in the top right corner
equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"
plt.text(X.max(), y.max(), equation, color="red", fontsize=12, verticalalignment='top') # Fix placement of text!!!

# Plots the scatter plot with the previously defined x and y variables in the color blue
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color="red")
plt.xlabel('Age at Death') # X axis label
plt.ylabel('pTAU (pg/ug)') # Y axis label
plt.title('Scatter Plot of Age at Death vs pTAU Concentration') # Main title of scatter plot
plt.plot(X, model.predict(X), color="red")
plt.show() # Prints the scatter plot