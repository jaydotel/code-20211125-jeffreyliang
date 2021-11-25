"""BMI Calculator"""

import logging
import json

_LOGGER = logging.getLogger(__name__)
_PATIENT_DATA_DIR = './data/patient_data.json'


class BMICalculator:
    """Represents a BMI (Body Mass Index) calculator and calculates BMI related information"""

    def run(self, patients: list = None):
        """Runs the main functionality of the BMI calculator

        1. Loads patient data
        2. Calculates BMI for a patient given height and weight
        3. Determines the patient's BMI Category and Health Risk
        4. Counts how many patients fit within the Overweight category

        Args:
            patients (list, optional): A list of patients can optionally be passed in
            otherwise, it'll be loaded from a file at `_PATIENT_DATA_DIR`

        Returns:
            (tuple): The modified patient data (3 new columns added)
            and number of "Overweight" patients.
        """

        patients = patients or self.load_patient_data()
        num_overweight_patients = 0

        # Calculate and add BMI data for each patient
        for patient in patients:

            # Ensure data exists and isn't 0/missing
            if (weight := int(patient.get('WeightKg', 0))) and (height := int(patient.get('HeightCm', 0))):
                height_in_m = height/100

                bmi = self.calculate_bmi(weight, height_in_m)
                patient['BMI'] = bmi

                patient_info = self.determine_category_and_health_risk(bmi)
                patient.update({
                    'BMI Category': patient_info[0],
                    'Health Risk': patient_info[1]
                })

                if patient_info[0] == 'Overweight':
                    num_overweight_patients += 1
            else:
                _LOGGER.error(
                    f'Data is missing, failed to calculate BMI! {weight=} '
                    f'{height=}'
                )

        return patients, num_overweight_patients

    @staticmethod
    def load_patient_data():
        """Loads patient JSON data from a file

        Returns:
            (list): List of patient data
        """

        with open(_PATIENT_DATA_DIR, encoding='UTF-8') as patient_data:
            return json.load(patient_data)

    @staticmethod
    def calculate_bmi(mass: int, height: int) -> int:
        """Calculates the BMI (Body Mass Index) rounded to 1DP

        Args:
            mass (int): mass of the patient
            height (int) height of the patient

        Returns:
            (int): BMI of the patient rounded to 1DP
        """

        return round(mass/height, 1)

    @staticmethod
    def determine_category_and_health_risk(bmi: int) -> tuple:
        """Calculates the BMI Category and Health Risk of the patient based on BMI

        Args:
            bmi (int): BMI of the patient

        Returns:
            (tuple):
                (str): BMI Category
                (str): Health risk
        """

        if bmi <= 18.4:
            return 'Underweight', 'Malnutrition risk'
        if 18.5 <= bmi <= 24.9:
            return 'Normal weight', 'Low risk'
        if 25 <= bmi <= 29.9:
            return 'Overweight', 'Enhanced risk'
        if 30 <= bmi <= 34.9:
            return 'Moderately obese', 'Medium risk'
        if 35 <= bmi <= 39.9:
            return 'Severely obese', 'High risk'
        return 'Very severely obese', 'Very high risk'

if __name__ == "__main__":
    logging.basicConfig(
        filename='bmi_calculator.python_error.log',
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s'
    )
    
    bmi_calculator = BMICalculator()
    patient_info = bmi_calculator.run()

    # Output modified json data to stdout
    print(f'Modified JSON: {json.dumps(patient_info[0], indent=2)}')

    # Output total number of overweight patients to stdout
    print(f'Number of overweight patients: {patient_info[1]}')
