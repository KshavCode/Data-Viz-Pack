import matplotlib.pyplot as plt, seaborn as sns, pandas as pd, numpy as np
from matplotlib import style

# Let's pick out a random country and check their details about which state airport they preferred the most every year
df = pd.read_csv("archive/Country Wise Yearly Visitors.csv")

subdf = df.drop("Country", axis=1)

avlist = []
for i in range(len(subdf.columns)) :
    s = 0
    for j in range(len(subdf.index)) :
        s += float(subdf.iloc[j, i])/1000000
        
    avlist.append(s)

year = [2000+x for x in range(14, 21)]

plt.plot(year, avlist, marker="d", c="r")
plt.ylabel("No. of Tourists (in millions)")
plt.tight_layout()
# plt.savefig("image/img7.png", transparent=True, dpi=400)
plt.show()




