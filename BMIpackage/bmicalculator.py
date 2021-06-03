import pandas as pd
import json

def read_json(filepath = "BMIpackage/data.json"):
    # reading the file if nor specified then default will be used
    with open((filepath), "r") as f:
        json_request = f.read()
        # string recieved. converted to json
        # function call to add columns to table and calculate bmi
        
        success_dic = bmical(json.loads(json_request))
        if not success_dic['error']:
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(success_dic['df'])
    return success_dic


def bmical(data):
    # converting json to dataframe
    df = pd.DataFrame(data)
    success_dic = {
        'error' : '',
        'df': '',
        'overweight': ''
    }
    # converting height to centimeter
    if ('HeightCm' in df.columns and not df['HeightCm'].isnull().values.any()) or ('HeightCm' in df.columns and not df['WeightKg'].isnull().values.any()):
        df['HeightCm'] = df['HeightCm']/100

        # calculating bmi
        df['bmi'] = df['WeightKg']/df['HeightCm']
        df['bmi'] = df['bmi'].round(decimals=2)

        # calculating bmi category using lambda function
        df['bmi category'] = df['bmi'].apply(
            lambda x: 'Underweight' if x < 18.5 else 
                    ("Normal weight" if 18.5 <= x < 25.0 else (
                    "Overweight" if 25.0 <= x < 30.0 else (
                    "Moderately obese" if 30.0 <= x < 35.0 else (
                    "Severely obese" if 35.0 <= x < 40.0 else 
                    "Very severely obese")))))
        # calculating health risk using lambda function
        df['health risk'] = df['bmi'].apply(
            lambda x: 'Malnutrition risk' if x < 18.5 else 
                    ("Low risk" if 18.5 <= x < 25.0 else (
                    "Enhanced risk" if 25.0 <= x < 30.0 else (
                    "Medium risk" if 30.0 <= x < 35.0 else (
                    "High risk" if 35.0 <= x < 40.0 else 
                    "Very high risk")))))
        # getting overweight count based on new columns added
        overweight_people = overweight_count(df)
        success_dic.update({
            'df': df,
            'overweight': overweight_people
        })
    else:
        success_dic.update({
            'error': 'Data is not correct'
        })
    return success_dic

# calculating total no. of overweights
def overweight_count(data):
    # getting the rows which have category overweight
    overweight = data[data["bmi category"] == "Overweight"]
    return len(overweight)