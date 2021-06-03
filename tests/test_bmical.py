
from BMIpackage import bmicalculator

def test_file_path_empty():
    result = bmicalculator.read_json()
    assert result['error'] == ''

# Checking if all columns exist
def test_col_exists():
    result = bmicalculator.read_json()
    df = result['df']
    assert 'Gender' in df.columns
    assert 'HeightCm' in df.columns
    assert 'WeightKg' in df.columns
    assert 'bmi' in df.columns
    assert 'bmi category' in df.columns
    assert 'health risk' in df.columns

# Checking if there is any null value generated in the output
def test_null_in_col():
    result = bmicalculator.read_json()
    df = result['df']
    assert not df['Gender'].isnull().values.any()
    assert not df['HeightCm'].isnull().values.any()
    assert not df['WeightKg'].isnull().values.any()
    assert not df['bmi'].isnull().values.any()
    assert not df['bmi category'].isnull().values.any()
    assert not df['health risk'].isnull().values.any()

# Checking values for already generated values
def test_for_bmi_values():
    result = bmicalculator.read_json()
    df = result['df']
    assert df['bmi'].to_list() == [56.14, 52.8, 42.78, 37.35, 46.67, 49.1]
    assert df['bmi category'].to_list() == ['Very severely obese','Very severely obese','Very severely obese','Severely obese','Very severely obese', 'Very severely obese']
    assert df['health risk'].to_list() == ['Very high risk', 'Very high risk', 'Very high risk', 'High risk', 'Very high risk', 'Very high risk',]

# Checking if the category and risk are calculated correctly on basis of bmi
def test_accuracy():
    result = bmicalculator.read_json()
    df = result['df']
    
    df_1 = df[df['bmi'] > 40]
    assert (df_1['bmi category'] == 'Very severely obese').all()
    assert (df_1['health risk'] == 'Very high risk').all()

    df_2 = df[df['bmi'].between(35.0,40.0)]
    assert (df_2['bmi category'] == 'Severely obese').all()
    assert (df_2['health risk'] == 'High risk').all()

    df_3 = df[df['bmi'].between(30.0,35.0)]
    assert (df_3['bmi category'] == 'Moderately obese').all()
    assert (df_3['health risk'] == 'Medium risk').all()

    df_4 = df[df['bmi'].between(25.0,30.0)]
    assert (df_4['bmi category'] == 'Overweight').all()
    assert (df_4['health risk'] == 'Enhanced risk').all()

    df_5 = df[df['bmi'].between(18.5,25.0)]
    assert (df_5['bmi category'] == 'Normal weight').all()
    assert (df_5['health risk'] == 'Low risk').all()

    df_6 = df[df['bmi'] < 18.5]
    assert (df_6['bmi category'] == 'Underweight').all()
    assert (df_6['health risk'] == 'Malnutrition risk').all()
        