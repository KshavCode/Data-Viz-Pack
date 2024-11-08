import matplotlib.pyplot as plt, seaborn as sns, pandas as pd, numpy as np
from matplotlib import style


# Let's pick out a random country and check their details about which state airport they preferred the most every year
df = pd.read_csv("archive/Country Wise Yearly Visitors.csv")

subdf = df.query("Country=='Sri Lanka'")
print(subdf)
totallis = subdf.loc[49, "2019"]
lis = [totallis, 21800000]


plt.pie(lis, colors=["#63a692", "#768a84"], explode=[0.2, 0], labels=["1.49", ""], textprops={"fontsize":14})
# plt.savefig("image/piesri.png", transparent=True, dpi=400)
plt.show()





