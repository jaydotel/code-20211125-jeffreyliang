# BMI Calculator

BMI (Body Mass Index) Calculator is a tool that allows users to calculate a patient's BMI and determine their BMI Category and Health Risk.

The patient's weight and height is read into the application in the form of JSON and as a result, a modified version of the JSON and the number of patients in the Overweight category is printed to the Command Line.

**Note:** The Number of overweight patients is based on patients in the Overweight BMI category rather than patients which are considered overweight (i.e. The combination of categories Overweight, Moderately obese, Severely obese and Very severely obese).

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of `Python 3.8`, `pip` and `pipenv`.
* You have set up your operating system to run Python applications. The below set of instructions has only been tested on Linux and cannot be guaranteed the same will work for Windows or Mac.

## Installing BMI Calculator

To run BMI Calculator, follow these steps in your preferred terminal:

1. Clone the repository onto your local machine

    `git clone https://github.com/jaydotel/code-20211125-jeffreyliang.git`

2. (Optional) If you will be developing on this project, navigate to the root folder and install development packages:
    
    `pipenv install --dev`

## Using BMI Calculator

To use BMI Calculator, follow these steps:

1. Add your own patient data own into `[rootdir]/data/patient-data.json`, ensuring your data is in the same format as the sample data pre-existing in the file. Alternatively, use the sample data provided if you'd like the test the application)
2. Run BMI Calculator

    `python -m bmicalculator.bmi_calculator`

3. You will see your patient data with three new columns, `BMI`, `BMI Category` and `Health Risk`. You'll also see the total number of patients which belong to the Overweight category.

## Running Unit Tests

From the project's root directory run:

    `python -m unittest`