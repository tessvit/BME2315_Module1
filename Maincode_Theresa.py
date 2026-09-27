from Donor_Theresa import *
from scipy import stats
import csv
import matplotlib.pyplot as plt
import numpy as np
import statistics


with open("C:/Users/Thill/Documents/BME 2315/MOD 1/Metadata and Protein Data for Module 1.csv", newline="") as f:
    reader = csv.reader(f)
    headers = next(reader) # Get the first row

    for h in headers:
        print(h)


Donor.instantiate_from_csv("C:/Users/Thill/Documents/BME 2315/MOD 1/Metadata and Protein Data for Module 1.csv")
print(Donor.get_donor("H19.33.004"))


Donor.all_donors.sort(key=Donor.get_age_at_death, reverse=False)

for donor in Donor.all_donors:
    print(donor)


female = range(len(Donor.filter(Donor.all_donors, sex="Female")))

print(f'Number of Female donors = {len(female)}')

male = range(len(Donor.filter(Donor.all_donors, sex="Male")))

print(f'Number of Male donors = {len(male)}')


age_female = []
age_male = []

for donor in Donor.filter(Donor.all_donors, sex="Female"):
    age_female.append(donor.age_at_death)

for donor in Donor.filter(Donor.all_donors, sex="Male"):
    age_male.append(donor.age_at_death)


x_female_bar = statistics.mean(age_female)
x_male_bar = statistics.mean(age_male)

age_female_stdev = statistics.stdev(age_female)
age_male_stdev = statistics.stdev(age_male)


print(f'x_female_bar = {x_female_bar}, age_female_stdev {age_female_stdev}')
print(f'x_male_bar = {x_male_bar}, age_male_stdev {age_male_stdev}')


Donor_sex_cols = ['Female', 'Male']
mean_sex = [x_female_bar, x_male_bar]
stdev_sex = [age_female_stdev, age_male_stdev]
yerr = [np.zeros(len(mean_sex)), stdev_sex]

t_stat, p_val = stats.ttest_ind(age_female, age_male)
print(f't_stat = {t_stat}, p_val = {p_val}')

plt.bar(Donor_sex_cols, mean_sex, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Age at Death by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Age at Death")
plt.text( 
        0.5, 90,
        f"t = {t_stat:.2f}\np = {p_val:.3e}",
        ha='center',
        va='bottom'
    )  
plt.show()

donor_age = []
donor_abeta42 = []

for donor in Donor.all_donors:
    donor_age.append(donor.age_at_death)

for donor in Donor.all_donors:
    donor_abeta42.append(donor.abeta42)


X = donor_age
y = donor_abeta42

plt.scatter(X, y, color='blue')
plt.xlabel('Age at Death')
plt.ylabel('ABeta42 pg/ug')
plt.title('Age at Death vs ABeta42')
plt.show()

plt.bar(age_female, age_female, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Lifespan of Breedgroups")
plt.xlabel("Breedgroup")
plt.ylabel("Average Lifespan (age)")
y_max = max(age_female) + max(age_female) * .4

# AI assistance: ChatGPT was used to help come up with variable names, and
# troubleshoot errors.