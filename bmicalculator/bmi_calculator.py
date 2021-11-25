"""BMI Calculator"""

_PATIENT_DATA_DIR = './data/patient_data.json'


class BMICalculator:
    """Represents a BMI (Body Mass Index) calculator and calculates BMI related information"""

    def run(self, patients: list = None):

        patients = patients or self.load_patient_data()

    @staticmethod
    def load_patient_data():
        """Loads patient JSON data from a file

        Returns:
            (list): List of patient data
        """

        with open(_PATIENT_DATA_DIR, encoding='UTF-8') as patient_data:
            return json.load(patient_data)

if __name__ == "__main__":
    bmi_calculator = BMICalculator()
    patient_info = bmi_calculator.run()
