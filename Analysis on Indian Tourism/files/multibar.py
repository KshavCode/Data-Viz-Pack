import pandas as pd, numpy as np, matplotlib.pyplot as plt
from matplotlib import style

style.use("bmh")

df = pd.read_csv("archive/Country Quater Wise Visitors.csv")

can = df.query("`Country of Nationality`== 'Sri Lanka'")
print(can)
can = can.drop("Country of Nationality", axis=1)
columnlist = [2000+x for x in range(14, 21)]
info = list(can.loc[49])
one = [float(info[x]) for x in range(0, len(info), 4)]
two = [float(info[x]) for x in range(1, len(info), 4)]
three = [float(info[x]) for x in range(2, len(info), 4)]
four = [float(info[x]) for x in range(3, len(info), 4)]

width = 0.2
tick = np.arange(len(columnlist))

plt.bar(tick, one, width=width, label="1st (Jan-March)")
plt.bar(tick+width, two, width=width, label="2nd (Apr-June)")
plt.bar(tick+width+width, three, width=width, label="3rd (July-Sep)")
plt.bar(tick+width+width+width, four, width=width, label="4th (Oct-Dec)")
plt.xticks(tick+0.3, labels=columnlist, fontsize=13)
plt.yticks([x for x in range(0, 101, 20)],fontsize=15)

# plt.title("No. of Visitors from Canada In Each Quarter")
plt.ylabel("Number of Tourists (in million)", labelpad=15, fontsize=15)
plt.legend(loc="upper center", fontsize=11, ncol=2, labelcolor="blue", fancybox=True, shadow=True, facecolor="#d8f2e8", edgecolor="red", title="Legends")
# plt.savefig("image/Srimultibar.png", transparent=True, dpi=400, bbox_inches="tight")
plt.show()