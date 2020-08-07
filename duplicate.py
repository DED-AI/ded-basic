import pandas as pd 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import time
from math import sin, cos, sqrt, atan2, radians
import ast
import json

#def calculate_distance(lat, lng, lat1, lng1):
#    R = 6373.0
#    lat = radians(lat)
#    lng = radians(lng)
#    lat1 = radians(lat1)
#    lng1 = radians(lng1)
#
#    dlon = lng1 - lng
#    dlat = lat1 - lat
#
#    a = sin(dlat / 2)**2 + cos(lat) * cos(lat1) * sin(dlon / 2)**2
#    c = 2 * atan2(sqrt(a), sqrt(1 - a))
#
#    return R * c

data = pd.read_json('https://gpstracker.net.in/gs3.3/api/api.php?api=user&ver=1.0&key=947CD241C16C051&cmd=OBJECT_GET_LOCATIONS,AP16FJ0278')   #read from api_key 
data['columns'] = data.index    #shifting the index
data.reset_index(drop = True)   #changing the index with numbers
data.columns                    #to know how many columns are there

D1 = data[['columns','358657100328207']].reset_index(drop = True)     #removing mahaMining from the dataset
    
D2 = D1.transpose().reset_index(drop = True)    #transpose the dataset

D2.columns = D2.iloc[0]                         # making the headers name with 0 row
D2 = D2.iloc[1:].reset_index(drop = True)       # making the headers name with 0 row
D3 = pd.read_csv('Location_data.csv')           # creating an empty data file

D4 = pd.concat([D2,D3]).reset_index(drop=True)  # merging the empty datafile with the dataset


D4["params"] = D4["params"].astype("str")

#D4["params"] = D4["params"].apply(ast.literal_eval)

#D4['params'].apply(pd.Series)
#D4 = pd.concat([D4.drop(['params'], axis=1), D4['params'].apply(pd.Series)], axis=1)
D4 = pd.concat([D4.drop('params', axis=1), pd.DataFrame(D4['params'].tolist())], axis=1)
#D4 = D4.drop('0', 1)

#D4 = D4.drop_duplicates()
D4.to_csv('Location_data.csv', index=False)    #storing the new dataset in csv file
print(D4)