
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')
font_main = {'family': 'Verdana', "size": 10}
plt.rcParams['text.color'] = "white"
plt.rc('font', **font_main)
font_heading = {"fontsize": 18, "fontname": "Georgia", "color": "white"}
df = pd.read_csv("cleaned_data.csv")
df1 = df.groupby(by="Age")
maledf = df1.get_group(18).query("Gender=='Male'").sum()

file_path = r'cleaned_data.csv'
df = pd.read_csv(file_path)


# Categorize sleep quality
df['Sleep_Quality_Category'] = pd.cut(df['Sleep_Quality'], bins=[0, 5, 7, 8, 10],
                                      labels=['Poor', 'Fair', 'Good', 'Excellent'])

# Calculate daily average caffeine intake (assuming 'Total_Caffeine' column)
df['Avg_Daily_Caffeine'] = df['Caffeine_Intake'] / 7

# Bin caffeine intake
df['Caffeine_Level'] = pd.cut(df['Caffeine_Intake'], bins=[0, 2, 5, np.inf], labels=['Low', 'Medium', 'High'])

# Distribution of Sleep Quality Categories
plt.figure(figsize=(8, 6))
sns.countplot(x='Sleep_Quality_Category', data=df, palette='Set2', hue='Sleep_Quality_Category')
plt.title('Distribution of Sleep Quality Categories')
plt.xlabel('Sleep Quality Category')
plt.ylabel('Count')
plt.savefig("images/10.png", transparent=True, dpi=400, bbox_inches="tight")


# Plot Caffeine Level vs Sleep Quality
plt.figure(figsize=(8, 6))
sns.countplot(x='Caffeine_Level', hue='Sleep_Quality_Category', data=df, palette='coolwarm')
plt.title('Caffeine Level vs Sleep Quality')
plt.xlabel('Caffeine Level')
plt.ylabel('Count')

plt.savefig("images/11.png", transparent=True, dpi=400, bbox_inches="tight")



# Plot Average Daily Caffeine Intake vs Sleep Quality
plt.figure(figsize=(8, 6))
sns.boxplot(x='Sleep_Quality_Category', y='Avg_Daily_Caffeine', data=df, palette='coolwarm', hue='Sleep_Quality_Category')
plt.title('Average Daily Caffeine Intake vs Sleep Quality')
plt.xlabel('Sleep Quality Category')
plt.ylabel('Average Daily Caffeine Intake')
plt.savefig("images/12.png", transparent=True, dpi=400, bbox_inches="tight")

# Scatter plot of GPA vs. Sleep Duration
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Sleep_Duration', y='GPA', data=df)
plt.title('Sleep Duration vs Academic Performance')
plt.savefig("images/13.png", transparent=True, dpi=400, bbox_inches="tight")





