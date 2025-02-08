import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style


# Getting to know about the data without actually opening it
df = pd.read_csv("student_sleep_patterns.csv")

print("Shape :", df.shape)
print("Columns :", list(df.columns))
print("\n", df.head())

# Checking for missing values (if any)
print(df.isnull().values.any())

# Plotting donut chart of average sleep duration per gender
male_avg = df.query("Gender=='Male'")["Sleep_Duration"].mean()
female_avg = df.query("Gender=='Female'")["Sleep_Duration"].mean()
other_avg = df.query("Gender=='Other'")["Sleep_Duration"].mean()

# Using theme and fonts
style.use('dark_background')
font_main = {'family':'Verdana', "size":13}
font_heading = {"fontsize":18, "fontname":"Georgia"}
plt.rc('font', **font_main)

plt.pie([male_avg, female_avg, other_avg], labels=["Male", "Female", "Other"], autopct="%1.1f%%", pctdistance=0.4, colors=["#A0153E", "#4B70F5", "#433D8B"], startangle=90, explode=[0.03 for _ in range(3)])
plt.gca().add_artist(plt.Circle((0,0),0.7, fc="black"))
plt.title("Avg Sleep Duration of Each Gender Type", **font_heading)

plt.savefig("images/7.png", transparent=True, dpi=400, bbox_inches="tight")