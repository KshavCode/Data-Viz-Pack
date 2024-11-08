import matplotlib.pyplot as plt, seaborn as sns, pandas as pd
from matplotlib import style

style.use("fivethirtyeight")


df = pd.read_csv("archive/General Data 2014-2020.csv")

sns.lineplot(data=df, x="year", y="noftaiiagr", label="Foreign Arrivals", c="red")
sns.lineplot(data=df, x="year", y="noindfiagr", label="Indian Departures", c="darkblue")
plt.ylabel("Annual Growth (in %)")
plt.xlabel("")
plt.legend(loc="center left")
plt.tight_layout()
plt.show()
# plt.savefig("image/random2.png", transparent=True, dpi=400, bbox_inches="tight")