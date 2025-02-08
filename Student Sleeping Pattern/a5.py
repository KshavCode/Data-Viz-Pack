import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('dark_background')
font_main = {'family': 'Verdana', "size": 10}
plt.rcParams['text.color'] = "white"
plt.rc('font', **font_main)
font_heading = {"fontsize": 18, "fontname": "Georgia", "color": "white"}
df = pd.read_csv("cleaned_data.csv")
df1 = df.groupby(by="Age")
maledf = df1.get_group(18).query("Gender=='Male'").sum()

plt.plot(maledf["Caffeine_Intake"], maledf["Sleep_Quality"])
plt.show()