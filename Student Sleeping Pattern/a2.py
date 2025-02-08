import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_csv("student_sleep_patterns.csv")

data = dict(df.groupby(["Age"])["Sleep_Duration"].mean())
print(df)

# Using theme and fonts
style.use('dark_background')
font_main = {'family':'Verdana', "size":10}
plt.rcParams['text.color'] = "black"
plt.rc('font', **font_main)
font_heading = {"fontsize":18, "fontname":"Georgia", "color":"white"}

plt.pie(list(data.values()), labels=list(data.keys()), autopct="%1.1f%%", pctdistance=0.6, startangle=90, explode=[0.03 for _ in data], radius=0.75)
plt.legend(labels=list(data.keys()), facecolor="white", loc="upper right")
# plt.gca().add_artist(plt.Circle((0,0),0.7, fc="black"))
plt.title("Avg Sleep Duration of Students per Age", **font_heading)
plt.show()

# plt.savefig("images/7.png", transparent=True, dpi=400, bbox_inches="tight")
