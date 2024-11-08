import pandas as pd, matplotlib.pyplot as plt, seaborn as sns

df = pd.read_csv("archive/Country Wise Yearly VIsitors.csv")
df["allsum"] = 0

# Histogram for getting to know about average number of tourists in total.
for i in range(len(df.index)) :
    su = 0
    for j in range(1, len(df.columns)) :
        su += int(df.iloc[i, j])
    df.loc[i, "allsum"] = su

countrylist = list(df["Country"])
totval = list(df["allsum"])

for i in range(len(totval)) :
    # Changing to (in millions)
    totval[i] /= 1000000

sns.histplot(totval, kde=True, bins=10)
plt.xlabel("No. of Visitors (in millions)")
plt.ylabel("No. of Countries", labelpad=10)
# plt.savefig("image/img2.png", transparent=True, dpi=400)
plt.show()