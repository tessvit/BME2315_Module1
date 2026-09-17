import csv # Importing csv allows VSCode to read directly from the .csv file

class Patient:
    allPatients = [] # List to hold all patient objects

    # Constructor with attributes of sex, age, years of education, APOE genotype, cognitive status, aBeta-40, aBeta-42, tTAU, and pTAU
    def __init__(self, sex: str, age: int, yearsOfEducation: int, APOEgenotype: str, cognitiveStatus: str, aBeta40 : float, aBeta42: float, tTAU : float, pTAU : float): 
        self.sex = sex
        self.age = age
        self.yearsOfEducation = yearsOfEducation
        self.APOEgenotype = APOEgenotype
        self.cognitiveStatus = cognitiveStatus
        self.aBeta40 = aBeta40
        self.aBeta42 = aBeta42
        self.tTAU = tTAU
        self.pTAU = pTAU
        Patient.allPatients.append(self) # Adds the patient object to the allPatients list with the above data

    # Representer: defines what will be shown when a patient object is printed
    # Each variable defined in the constructor will be printed when a patient object is called, but there will be a label in front of the value so it is clear what the reader is looking at
    def __repr__(self):  
        return f"(Sex: {self.sex}: Age: ({self.age} | Years of Education: {self.yearsOfEducation} | APOE Genotype: {self.APOEgenotype} | Cognitive Status: {self.cognitiveStatus} | Amyloid Beta-40 Status: {self.aBeta40} | Amyloid Beta-42: {self.aBeta42} | Total Tau: {self.tTAU} | Phosphorylated Tau: {self.pTAU})"

    # Returns years of education when called on a patient object
    def get_yearsOfEducation(self): 
        return self.yearsOfEducation

    # Class method pulls objects from the .csv file and creates patient objects from this data
    @classmethod 
    def instantiate_from_csv(cls, filename: str):
    
        # The code below will open the .csv file and create a list of all the rows in the patient data spreadsheet
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
            
            # The code below will create a patient object for each row, with the information declared in the constructor (sex, age, years of education, APOE genotype, cognitive status, aBeta-40, aBeta-42, tTAU, and pTAU): 
            # int and float are used on the columns that have whole numbers (int) or decimal numbers (float) to ensure they come in as the proper type for comparing the data later
            for row in rows_of_patients:
                Patient(
                    sex = row['Sex'],
                    age = (int(row['Age at Death'])),
                    yearsOfEducation = (int(row['Years of education'])),
                    APOEgenotype = row['APOE Genotype'],
                    cognitiveStatus = row['Cognitive Status'],
                    aBeta40 = (float(row['ABeta40 pg/ug'])),
                    aBeta42 = (float(row['ABeta42 pg/ug'])),
                    tTAU = (float(row['tTAU pg/ug'])),
                    pTAU = (float(row['pTAU pg/ug']))
                )

    # Class method filters the list of patient objects; this is useful to print a subset of the data
    @classmethod
    # Filter method takes in the class and any variables you want to sort by
    def filter(cls, list, sex: str = "any", age: int = "any", yearsOfEducation: int = "any", APOEgenotype: str = "any", cognitiveStatus: str = "any", aBeta40 : float = "any", aBeta42: float = "any", tTAU : float = "any", pTAU : float = "any"):
            allPatients = list
            removeList = []
            attrList = ( # The following is all of the variables defined in the constructor; these are the variables that could be used for sorting
                        sex,
                        age,
                        yearsOfEducation,
                        APOEgenotype,
                        cognitiveStatus,
                        aBeta40,
                        aBeta42,
                        tTAU,
                        pTAU
                        
                        )
            attrName = ( # Below are the names of all of the variables; these will be used to compare to the variables to see which to filter
                        "sex",
                        "age",
                        "yearsOfEducation",
                        "APOEgenotype",
                        "cognitiveStatus",
                        "aBeta40",
                        "aBeta42",
                        "tTAU",
                        "pTAU"
                        )
            for attr in range(len(attrList)):
                if attrList[attr] != "any": # Iterates through the list of all the variables; the variables recieve a default value of "any", but if a variable has a value that is not any, it goes through the for loop
                    for patient in allPatients: # Iterates through patient list and adds patients whose name does not equal the variable name to the remove list (because they would then equal "any" if the user did not type a specific variable they want to examine)
                        if getattr(patient,attrName[attr]) != attrList[attr]:
                            removeList.append(patient)
                    allPatients = [patient for patient in allPatients if patient not in removeList] # allPatients list becomes all of the patients not in the removeList
                    removeList.clear() # Clears the objects in the removeList

            return allPatients # Returns the objects that were filtered for