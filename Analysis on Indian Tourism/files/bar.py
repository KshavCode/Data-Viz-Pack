import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import style
from scipy.interpolate import make_interp_spline, BSpline

style.use("ggplot")

df = pd.read_csv("archive/General Data 2014-2020.csv")

plt.figure(figsize= (12, 2))
plt.bar(df.year, df.feeftust, color="green")

plt.ylabel("USD (in Billions)")
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.tight_layout()
# plt.savefig("image/test.png", transparent=True, dpi=400)
plt.show()