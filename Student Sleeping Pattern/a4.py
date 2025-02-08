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
df1 = df.sort_values(by="Screen_Time", ascending=False)
df1 = df1.iloc[:, :7]

# Calculate mean Screen_Time for each Gender and University_Year
inner_means = df1.groupby(["Gender", "University_Year"])["Screen_Time"].mean()
outer_counts = df1.groupby("Gender").size()

# Define colors for each University_Year
year_colors = {
    '1st Year': '#66c2a5',
    '2nd Year': '#fc8d62',
    '3rd Year': '#8da0cb',
    '4th Year': '#e78ac3'
}

# Assign colors to inner pie chart based on University_Year
inner_colors = [year_colors[year] for year in inner_means.index.get_level_values(1)]
outer_colors = ["#bb3d2e", "#36a41e", "#187bea"]

fig, ax = plt.subplots(figsize=(12, 8))
size = 0.3

# Outer pie chart (Gender breakdown)
ax.pie(outer_counts, radius=1, labels=outer_counts.index, autopct='%1.1f%%', pctdistance=0.85,
       labeldistance=1.05, wedgeprops=dict(width=size, edgecolor='w'), colors=outer_colors)

# Inner pie chart (Mean Screen Time by University Year within Gender)
mean_labels = [f'{mean:.1f} hrs' for year, mean in zip(inner_means.index.get_level_values(1), inner_means)]
ax.pie(inner_means, radius=1 - size, labels=mean_labels, colors=inner_colors, labeldistance=0.7,
       wedgeprops=dict(width=size, edgecolor='w'), textprops={'color': 'black'})

ax.set(aspect="equal", title='Screen Time Breakdown by Gender and University Year')
plt.title("Screen Time Breakdown by Gender and University Year", fontsize=font_heading["fontsize"],
          fontname=font_heading["fontname"], color=font_heading["color"])
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10)
           for color in year_colors.values()]
labels = year_colors.keys()
plt.legend(handles, labels, title="University Year", loc="upper left")


plt.savefig("images/6.png", transparent=True, dpi=400, bbox_inches="tight")
