import pandas as pd 
import ast
import datetime as dt
import numpy as np


#M1 = pd.read_csv('location_data_31072020_copy.csv')
#M2 = M1["params"]

#M2  = M1[M1["speed"].eq(0)]    #to know the vehicle not moving = idle case
#
#M3 = M1[M1["acc"].eq(1)]       #to know the vehicle when the engine is on
#
# M1["Match"] = np.where(M1['speed'] == M1['acc'], 'move or off', 'idle')
 
 

#M2 = M2.apply(lambda x: ast.literal_eval(x))
#M2 = M2.apply(pd.Series)

#M3 = pd.concat([M1, M2], axis=1)

 
 

#conditions  = [ (M3["speed"] >= 1)&(M3["acc"] == 1), (M3["speed"] == 0)&(M3["acc"] == 1), (M3["speed"] == 0)&(M3["acc"] == 0)]
#choices     = [ "moving", 'idle', 'off' ]
#
#M1["statues"] = np.select(conditions, choices, default=np.nan)
#
#M3.to_csv('Location_data.csv', index=False)
#print(M3["acc"].dtype)




M1 = pd.read_csv('/Users/rakesh/Desktop/ded/location_data_31072020.csv')
M2 = M1["params"]                 #taking only params column
M2 = M2.apply(lambda x: ast.literal_eval(x))     #seperating the dictionary type in the column to seperate columns
M2 = M2.apply(pd.Series)                         #seperating the dictionary type in the column to seperate columns and keeping in series

M3 = pd.concat([M1, M2], axis=1)                 #merging the original dataset with seperated columns
M3 = M3.drop_duplicates()                        #removing the duplicates

M3["acc"] = M3["acc"].astype(float)              #converting the object type to float
M3["speed"] = M3["speed"].astype(float)          #converting the object type to float
M3["pump"] = M3["pump"].astype(float)            #converting the object type to float
M3["track"] = M3["track"].astype(float)          #converting the object type to float
M3["bats"] = M3["bats"].astype(float)            #converting the object type to float
M3["batl"] = M3["batl"].astype(float)            #converting the object type to float

conditions  = [ ((M3["speed"] >= 1)&(M3["acc"] == 1)), ((M3["speed"] == 0)&(M3["acc"] == 1)), ((M3["speed"] == 0)&(M3["acc"] == 0))]   #determaining the condition for statues of the vehicle
choices     = [ "moving", 'idle', 'off' ]        #determaining the variables for statues of the vehicle
M3["statues"] = np.select(conditions, choices, default=np.nan)   #determaining the statues of the vehicle



M3["shift_statues"] = M3["statues"].shift(-1) #shifting the statues column by 1


M3['statues_result_moving'] = np.where(((M3["statues"] == "moving")&(M3["shift_statues"] == "moving"))|((M3["statues"] == "moving")&(M3["shift_statues"] == "idle")) | ((M3["statues"] == "moving")&(M3["shift_statues"] == "off")) | ((M3["statues"] == "off")&(M3["shift_statues"] == "moving")) |((M3["statues"] == "idle")&(M3["shift_statues"] == "moving")), 'active', 'non_active')     #condition for active hours

M3['statues_result_moving_idle'] = np.where(((M3["statues"] == "moving")&(M3["shift_statues"] == "moving"))|((M3["statues"] == "moving")&(M3["shift_statues"] == "idle")) | ((M3["statues"] == "moving")&(M3["shift_statues"] == "off")) | ((M3["statues"] == "off")&(M3["shift_statues"] == "moving")) |((M3["statues"] == "idle")&(M3["shift_statues"] == "moving")|((M3["statues"] == "idle")&(M3["shift_statues"] == "off"))|((M3["statues"] == "off")&(M3["shift_statues"] == "idle"))|((M3["statues"] == "idle")&(M3["shift_statues"] == "idle"))), 'active', 'non_active')    #condition for rough active hours      


#M5 = M3[M3['statues'] == 'moving']
#M6 = M3[M3['statues'] == 'idle']
#M7 = M3[M3['statues'] == 'off']



M11 = M3
M11['dt_tracker'] = pd.to_datetime(M3['dt_tracker'], format='%Y-%m-%d %H:%M:%S')    # converting dt_tracker column from object to timestamps
M11['dt_tracker_IST'] = M3['dt_tracker'].dt.tz_localize("GMT").dt.tz_convert('Asia/Calcutta').dt.tz_localize(None)  #converting the time from UTC to IST

M11['tracker_date'] = pd.to_datetime(M3['dt_tracker_IST'], format='%Y-%m-%d %H:%M:%S').dt.date  #removing date from date-time
M11['tracker_date'] = pd.to_datetime(M3['tracker_date'], format='%Y-%m-%d')                     #removing date from date-time




M11 = M11.drop_duplicates()           #removing the duplicate from the dataset

M11["shift_time"] = M11["dt_tracker_IST"].shift(-1)       #shifting the dt_tracker_IST
M11["DIFFERENCE"] = M11['dt_tracker_IST'] - M11["shift_time"]  #taking difference of the t[i+1] - t[i]

M11['DIFFERENCE']= M11["DIFFERENCE"]/np.timedelta64(1,'h')     #changing the time from sec to hrs

M12 = M11[M11['statues_result_moving'] == 'active']     #taking the dataset having active variable in statues_result_moving
Total_active = M12['DIFFERENCE'].sum()                  #taking the sum of the column

M11.to_csv('Location_data_test.csv', index=False)      #keeping in the csv file





M13 = M11[M11['tracker_date'] == '2020-07-27']    # filtering the data of  paticular date

M13 = M13.drop(M13.index[len(M13)-1])             #  removing the last row because - it will take the difference with the previous day

M13.to_csv('Location_data_test1.csv', index=False) 

M14 = M13[M13['statues_result_moving'] == 'active']    #filtering the data of active to paticular date for moving
Total_active_day = M14['DIFFERENCE'].sum()             #taking the sum of the column of active in particular day for moving

M15 = M13[M13['statues_result_moving_idle'] == 'active']  #filtering the data of active to paticular date for moving and idle
Total_active_day_with_idle = M15['DIFFERENCE'].sum()      #taking the sum of the column of active in particular day for moving and idle

