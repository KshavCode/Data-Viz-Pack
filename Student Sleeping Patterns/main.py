import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (12, 6)
file_path = 'cleaned_data.csv'
df = pd.read_csv(file_path)

from matplotlib import style 
style.use("dark_background")
font_main = {'family':'Verdana', "size":13}
font_heading = {"fontsize":18, "fontname":"Georgia"}
plt.rc('font', **font_main)

plt.figure()
sns.histplot(df['Sleep_Duration'], kde=True, bins=10, color="Teal")
plt.title('Distribution of Sleep Duration')
plt.xlabel('Hours')
plt.ylabel('Frequency')

plt.savefig("images/1.png", transparent=True, dpi=400, bbox_inches="tight")


plt.figure()
sns.boxplot(x='Gender', y='Sleep_Duration', data=df, color="green")
plt.title('Sleep Duration by Gender')
plt.savefig("images/2.png", transparent=True, dpi=400, bbox_inches="tight")


numeric_data = df.select_dtypes(include=['float64', 'int64'])
corr = numeric_data.corr()

plt.figure()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.savefig("images/3.png", transparent=True, dpi=400, bbox_inches="tight")


plt.figure()
sns.barplot(x='University_Year', y='Sleep_Quality', data=df, estimator = lambda x: x.mean(), hue = "Gender")
plt.title('Average Sleep Quality by University Year')
plt.savefig("images/4.png", transparent=True, dpi=400, bbox_inches="tight")


plt.figure()
sns.boxplot(x='Gender', y='Caffeine_Intake', data=df)
plt.title('Caffeine Intake by Gender')
plt.savefig("images/5.png", transparent=True, dpi=400, bbox_inches="tight")


# Calculating difference in sleep duration
df['Weekend_vs_Weekday'] = df['Weekend_Sleep_End'] - df['Weekday_Sleep_End']

plt.figure()
sns.histplot(df['Weekend_vs_Weekday'], kde=True, color="red")
plt.title('Difference in Sleep Duration: Weekends vs Weekdays')
plt.xlabel('Difference (Hours)')
plt.savefig("images/6.png", transparent=True, dpi=400, bbox_inches="tight")






