import matplotlib.pyplot as plt, seaborn as sns, pandas as pd, numpy as np
from matplotlib import style
import random

style.use("ggplot")

# Let's pick out a random country and check their details about which state airport they preferred the most every year
df = pd.read_csv("archive/Country Wise Airport.csv")
countrylist = list(df["Country of Nationality"])
place = countrylist.index("Sri Lanka")

subdf = df.query("`Country of Nationality`=='Sri Lanka'")
subdf = subdf.drop("Country of Nationality", axis=1)
totallis = list(subdf.loc[place])
delhi = sum([float(totallis[x]) for x in range(0, len(totallis), 8)])
mumb = sum([float(totallis[x]) for x in range(1, len(totallis), 8)])
chen = sum([float(totallis[x]) for x in range(2, len(totallis), 8)])
cali = sum([float(totallis[x]) for x in range(3, len(totallis), 8)])
kol = sum([float(totallis[x]) for x in range(5, len(totallis), 8)])
hyd = sum([float(totallis[x]) for x in range(6, len(totallis), 8)])
cochin = sum([float(totallis[x]) for x in range(7, len(totallis), 8)])
tot = [delhi, hyd, mumb, chen, cali, kol]
lab = ["Delhi", "Hyderabad", "Mumbai", "Chennai", "Calicut", "Kolkata"]

plt.figure(figsize=(8, 2))
plt.bar(lab, tot, color="#bdaa20")
# plt.savefig("image/airportsri.png", transparent=True, dpi=400)
plt.show()




