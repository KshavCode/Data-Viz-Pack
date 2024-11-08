import pandas as pd, numpy as np, matplotlib.pyplot as plt 

df = pd.read_csv("archive/Country Wise Age Group.csv")

ukdf = df.query("`Country of Nationality` =='Sri Lanka'")

ukdf['Young 2014'] = ukdf['2014 0-14'] + ukdf['2014 15-24'] 
ukdf['Middle 2014'] = ukdf['2014 25-34'] + ukdf['2014 35-44'] + ukdf['2014 35-44'] + ukdf['2014 45-54']
ukdf['Senior 2014'] = ukdf['2014 55-64'] + ukdf['2014 65 AND ABOVE'] 

yo = []
mid = []
sn= []

for i in range(14, 21) :
    a1 = float(ukdf[f'20{i} 0-14']) + float(ukdf[f'20{i} 15-24'])
    a2 = float(ukdf[f'20{i} 25-34']) + float(ukdf[f'20{i} 35-44']) + float(ukdf[f'20{i} 35-44']) + float(ukdf[f'20{i} 45-54'])
    a3 = float(ukdf[f'20{i} 55-64']) + float(ukdf[f'20{i} 65 AND ABOVE'])
    yo.append(a1)
    mid.append(a2)
    sn.append(a3)


plt.ylabel("No. of Tourists (in million)")
plt.fill_between([2000+x for x in range(14, 21)], yo, label="Young (0-24)", alpha=0.3)
plt.fill_between([2000+x for x in range(14, 21)], mid, label="Middle (25-54)", alpha=0.3)
plt.fill_between([2000+x for x in range(14, 21)], sn, label="Senior (55 & ABOVE)", alpha=0.3)
plt.legend(loc="center", fontsize=9, ncol=3)
plt.tight_layout()
plt.savefig("image/areasri.png", transparent=True, dpi=400)
# plt.show()




