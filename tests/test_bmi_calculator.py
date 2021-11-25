"""Unit tests for BMI Calculator"""

from unittest import TestCase

from bmicalculator.bmi_calculator import BMICalculator


class BMICalculatorTestCase(TestCase):
    """Unit tests for BMI Calculator"""

    @classmethod
    def setUpClass(cls):
        cls.bmi_calculator = BMICalculator()

    def test_patient_data_updated_succcessfully(self):
        """Tests that patient data is successfully updated with BMI, BMI
        Category and Health Risk"""

        sample_patient_info =   [{
            "HeightCm": 171,
            "WeightKg": 96
        },
        {
            "HeightCm": 161,
            "WeightKg": 85,
        }]

        expected_modified_patient_info = [
            {
                "HeightCm": 171,
                "WeightKg": 96,
                "BMI": 56.1,
                "BMI Category": "Very severely obese",
                "Health Risk": "Very high risk"
            },
            {
                "HeightCm": 161,
                "WeightKg": 85,
                "BMI": 52.8,
                "BMI Category": "Very severely obese",
                "Health Risk": "Very high risk"
            }
        ]

        self.assertListEqual(
            self.bmi_calculator.run(sample_patient_info)[0],
            expected_modified_patient_info
        )

    def test_determine_bmi_calculator(self):
        """Test that the correct BMI Category and Health Risk is returned
        for each sample_bmi_value"""

        sample_bmi_values = [18, 20, 27, 32, 37, 40]
        expected_bmi_info = [
            ('Underweight', 'Malnutrition risk'),
            ('Normal weight', 'Low risk'),
            ('Overweight', 'Enhanced risk'),
            ('Moderately obese', 'Medium risk'),
            ('Severely obese', 'High risk'),
            ('Very severely obese', 'Very high risk'),
        ]

        for idx, sample_bmi_value in enumerate(sample_bmi_values):
            self.assertTupleEqual(
                self.bmi_calculator.determine_category_and_health_risk(sample_bmi_value),
                expected_bmi_info[idx]
            )
