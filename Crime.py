import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/jolie-mcdonnell/data_mining_project/main/Crimes_Neighborhoods.csv", header = 0)
df = pd.DataFrame(df)
df.replace('DRUGS - POSSESSION OF DRUG PARAPHANALIA', 'Drug Related', inplace = True)
df.replace(to_replace = 'DRUGS - POSSESSION/ SALE/ MANUFACTURING/ USE', value = 'Drug Related',inplace = True)
df.replace(to_replace= 'ASSAULT - AGGRAVATED', value = 'Assault',inplace = True)
df.replace(to_replace = 'ASSAULT - SIMPLE', value = 'Assault',inplace = True)
df.replace(to_replace = 'MURDER, NON-NEGLIGIENT MANSLAUGHTER', value = 'Murder',inplace = True)
df.replace(to_replace = 'BURGLARY - COMMERCAL', value = 'Burglary/Theft',inplace = True)
df.replace(to_replace = 'BURGLARY - RESIDENTIAL', value = 'Burglary/Theft',inplace = True)
df.replace(to_replace = 'LARCENY PURSE SNATCH - NO FORCE', value = "Burglary/Theft",inplace = True)
df.replace(to_replace = 'AUTO THEFT - MOTORCYCLE / SCOOTER', value = 'Burglary/Theft',inplace = True)
df.replace(to_replace = 'LARCENY PICK-POCKET', value = "Burglary/Theft",inplace = True)
df.replace(to_replace = 'LARCENY THEFT OF BICYCLE', value = 'Burglary/Theft',inplace = True)
df.replace(to_replace = 'LARCENY ALL OTHERS', value = 'Burglary/Theft',inplace = True)
df.replace(to_replace = 'LARCENY THEFT FROM BUILDING', value = "Burglary/Theft",inplace = True)
df.replace(to_replace = "LARCENY THEFT FROM MV - NON-ACCESSORY", value = "Burglary/Theft",inplace = True)
df.replace(to_replace = 'ROBBERY', value = "Burglary/Theft",inplace = True)

neighborhoods = list(set(df['Name']))

df.replace(to_replace = 'Chinatown', value = np.NaN, inplace = True)
df.replace(to_replace = 'Leather District', value = np.NaN, inplace = True)
df.replace(to_replace = 'Bay Village', value = np.NaN, inplace = True)

cleandf = df.dropna(subset = ['Name'])
print(len(set(cleandf['Name'])))

incomes = []
for i in df["Name"]:
    if i == "Allston":
        incomes.append(34149)
    elif i == "Back Bay":
        incomes.append(110667)
    elif i == "Beacon Hill":
        incomes.append(100005)
    elif i == "Brighton":
        incomes.append(41261)
    elif i == "Charlestown":
        incomes.append(75339)
    elif i == "Dorchester":
        incomes.append(29767)
    elif i == "Downtown":
        incomes.append(80557)
    elif i == "East Boston":
        incomes.append(31473)
    elif i == "Fenway":
        incomes.append(28021)
    elif i == "Hyde Park":
        incomes.append(32744)
    elif i == "Jamaica Plain":
        incomes.append(51655)
    elif i == "Longwood":
        incomes.append(7975)
    elif i == "Mattapan":
        incomes.append(28356)
    elif i == "Mission Hill":
        incomes.append(23446)
    elif i == "North End":
        incomes.append(89696)
    elif i == 'Roslindale':
        incomes.append(41252)
    elif i == "Roxbury":
        incomes.append(20978)
    elif i == 'South Boston':
        incomes.append(64745)
    elif i == 'South Boston Waterfront':
        incomes.append(129651)
    elif i == 'South End':
        incomes.append(83609)
    elif i == "West End":
        incomes.append(77069)
    elif i == 'West Roxbury':
        incomes.append(47836)

cleandf['MedianIncome'] = incomes

Murders = cleandf[cleandf['OFFENSE_DE'] == 'Murder']
Assaults = cleandf[cleandf['OFFENSE_DE'] == 'Assault']
Drugs = cleandf[cleandf['OFFENSE_DE'] == 'Drug Related']
Robbery = cleandf[cleandf['OFFENSE_DE'] == 'Burglary/Theft']

print(Assaults)

plt.hist(Robbery['MedianIncome'], bins = 15)
plt.ylabel("Robberies")
plt.xlabel("Median Income (in Dollars)")
plt.show()
