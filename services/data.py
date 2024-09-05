import pandas as pd
import pprint
import json

def fetch_data():
    df = pd.read_csv('services/climatiq_data2.csv')
    df = df.fillna('None')
    return df.to_dict(orient='records')
    # unique_values = {col: df[col].unique().tolist() for col in df.columns}
    
    # return unique_values

# with open('data_columns.json','w') as json_data:
#     json_data.write(fetch_data('columns'))
# json_data = json.dumps(fetch_unique_column_vals(), indent=2)
    
#     # Save the JSON data to a file
# json_file_path = 'unique_values.json'
# with open(json_file_path, 'w') as json_file:
#     json_file.write(json_data)