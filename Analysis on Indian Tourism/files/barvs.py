import matplotlib.pyplot as plt, pandas as pd, seaborn as sns, numpy as np

df = pd.read_csv("archive/General Data 2014-2020.csv")

tick = np.arange(len(df.year))

plt.figure(figsize=(8,3))
plt.bar(tick, df.noftaii, width=0.4, color="#d6b4d0")
plt.bar(tick+0.4, df.noindfi, width=0.4, color="#d934bb")

plt.xticks(tick+0.2, labels=df.year)
plt.yticks([10, 20, 30])


plt.ylabel("Tourists (in million)")
plt.show()
# plt.savefig("image/random.png", transparent=True, dpi=400, bbox_inches="tight")