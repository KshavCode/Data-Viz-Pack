import pandas as pd, numpy as np, matplotlib.pyplot as plt


# STYLING MUST 
from matplotlib import style
style.use('dark_background')
font_main = {'family':'Verdana', "size":10}
plt.rcParams['text.color'] = "black"
plt.rc('font', **font_main)
font_heading = {"fontsize":18, "fontname":"Georgia", "color":"white"}

df1 = pd.read_csv("cleaned_data.csv")


# Grouping into University Year
s = df1.query("University_Year=='3rd Year'")
print(s)
df1 = df1.groupby(by="University_Year")
onedf = df1.get_group("1st Year")
twodf = df1.get_group("2nd Year")
threedf = df1.get_group("3rd Year")
fourdf = df1.get_group("4th Year")

tick = np.array(list(range(1, 5)))

# Plotting a bar chart for Year differentiated ScreenTime VS SleepDuration
width = 0.2
plt.bar(onedf.loc[:, "Screen_Time"].astype(int), onedf.loc[:, "Sleep_Duration"], width=width, label="1st Year")
plt.bar(twodf.loc[:, "Screen_Time"].astype(int)+width, twodf.loc[:, "Sleep_Duration"], width=width, label="2nd Year")
plt.bar(threedf.loc[:, "Screen_Time"].astype(int)+width*2, threedf.loc[:, "Sleep_Duration"], width=width, label="3rd Year")
plt.bar(fourdf.loc[:, "Screen_Time"].astype(int)+width*3, fourdf.loc[:, "Sleep_Duration"], width=width, label="4th Year")
plt.xlabel("Screen_Time")
plt.ylabel("Sleep_Duration")

# Arranging xticks to the center
plt.xticks(ticks=tick+width*1.5, labels=tick)
plt.yticks(ticks=np.concatenate((tick, np.arange(5, 11))))
plt.legend(facecolor="#cc200c", labelcolor="white")
plt.show()

# plt.savefig("images/8.png", transparent=True, dpi=400, bbox_inches="tight")
