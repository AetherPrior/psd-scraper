import pandas as pd 
import numpy as np
from pandas.io.json import json_normalize

## Selecting  a PS station
print("Enter a ps station (or a part). Multiple stations can be separated by | , no spaces")
Name = str(input())
## Select branch filter
print("Enter space separated branch code list")
branches = str.split(str(input()))
branches.append('Any')

df = pd.read_json(r'full.json')
df.drop(['StationId','AccomodationDesc','stipendforpg','Scholarship','CompanyId','stipend'],axis=1)
def matcher(x):
    for i in branches:
        if x.find(i) != -1:
            return i
    else:
            return np.NaN

df2 = df[df['Tags'].apply(matcher).notna()].dropna(axis=0)
df2 = df2[df2['CompanyName'].str.contains(Name,case=False)]
print(df2)
Projects = df2['projs']
Project = []
for i in Projects.tolist():
    for j in i:
        Project.append(j['details'])
df = []
df2 = []
for j in Project:
    dftemp = json_normalize(j).loc[:,['ProjectId','TotalReqdStudents','projectTitle','PBDescription']]
    df.append(dftemp[dftemp['PBDescription'].notna()][
            'PBDescription'
        ].tolist())
    df2.append(dftemp[dftemp['projectTitle'].notna()][
            'projectTitle'
        ].tolist())
##stuff highly customized here, you'll need to recode
print(df)
print(df2)
