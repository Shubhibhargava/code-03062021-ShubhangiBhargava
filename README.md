# code-03062021-ShubhangiBhargava
BMI Calculator

get a clone of this

run cmnd to create a virtual env:

"virtualenv venv"

now traverse to requirement file using:

"cd /BMIcalculator/BMIpackage"

run cmnd to install all requirement:

"pip install -r requirements.txt"

traverse to BMIcalculator:

"cd /BMIcalculator"

go to the pyhton shellby writing python

then import the package:

"from BMIpackage import bmicalculator"

then call the function to execute:

"bmicalculator.read_json()"

In the read_json() you can pass the path of the file , If no path is passed the default file i.e data.json will be used.

you can pass path like:

"bmicalculator.read_json('/bmi_data.json')"

run this cmnd to execute the test cases:

"python -m pytest -v tests/test_bmical.py"
