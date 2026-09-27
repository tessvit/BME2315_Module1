import csv

class Donor:
    all_donors = []

    def __init__(
        self,
        donor_id: str,
        age_at_death: float,
        fresh_brain_weight: float,
        primary_study_name: str = "n/a",
        cognitive_status: str = "n/a",
        sex: str = "n/a",
        abeta42: float = 0,
        ptau: float = 0
    ):
        self.donor_id = donor_id
        self.age_at_death = age_at_death
        self.fresh_brain_weight = fresh_brain_weight
        self.primary_study_name = primary_study_name
        self.cognitive_status = cognitive_status
        self.sex = sex
        self.abeta42 = abeta42
        self.ptau = ptau

        Donor.all_donors.append(self)

    def __repr__(self):
        return f"{self.primary_study_name}: ({self.donor_id} | {self.cognitive_status} | {self.age_at_death} | {self.fresh_brain_weight})"

    def get_age_at_death(self):
        return self.age_at_death

    @classmethod
    def sum_ages(cls):
        total = 0
        for donor in Donor.all_donors:
            total += donor.age_at_death
        return total

    @classmethod
    def instantiate_from_csv(cls, filename: str):

        # the code below will open the .csv file and create a list of all the rows in your spreadsheet
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_donors = list(reader)

        # the code below will create a donor object for each row, based on the data
        for row in rows_of_donors:
            Donor(
                donor_id=row['Donor ID'],
                age_at_death=float(row['Age at Death']),
                fresh_brain_weight=float(row['Fresh Brain Weight']) if row['Fresh Brain Weight'] != "Unavailable" else 0,
                primary_study_name=row['Primary Study Name'],
                cognitive_status=row['Cognitive Status'],
                sex=row['Sex'],
                abeta42=float(row['ABeta42 pg/ug']) if row['ABeta42 pg/ug'] != "Unavailable" else 0,
                ptau=float(row['pTAU pg/ug']) if row['pTAU pg/ug'] != "Unavailable" else 0
            )

    @classmethod
    def get_donor(cls, donor_id):
        for donor in Donor.all_donors:
            if donor_id == donor.donor_id:
                return donor

    @classmethod
    def filter(
        cls,
        list,
        donor_id: str = "any",
        age_at_death: int = "any",
        fresh_brain_weight: int = "any",
        primary_study_name: str = "any",
        cognitive_status: str = "any",
        sex: str = "any"
    ):
        all_donors = list
        remove_list = []

        attr_list = (
            donor_id,
            age_at_death,
            fresh_brain_weight,
            primary_study_name,
            cognitive_status,
            sex
        )

        attr_name = (
            "donor_id",
            "age_at_death",
            "fresh_brain_weight",
            "primary_study_name",
            "cognitive_status",
            "sex"
        )

        for attr in range(len(attr_list)):
            if attr_list[attr] != "any":
                for donor in all_donors:
                    if getattr(donor, attr_name[attr]) != attr_list[attr]:
                        remove_list.append(donor)

                all_donors = [
                    donor for donor in all_donors
                    if donor not in remove_list
                ]

                remove_list.clear()

        return all_donors