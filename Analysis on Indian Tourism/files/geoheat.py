import plotly.express as px, plotly.offline as pyo
import pandas as pd
import plotly.io as pio


df = pd.read_csv("archive/Country Wise Yearly VIsitors.csv")
df["allsum"] = 0

# Histogram for getting to know about average number of tourists in total.
for i in range(len(df.index)) :
    su = 0
    for j in range(1, len(df.columns)) :
        su += int(df.iloc[i, j])
    df.loc[i, "allsum"] = su



# fig = px.choropleth(data_frame=df, locationmode="country names", locations="Country", color="allsum", color_continuous_scale="Viridis")
fig = px.choropleth(data_frame=df, locationmode="country names", locations="Country", color="allsum", color_continuous_scale="Reds")
# fig = px.choropleth(data_frame=df, locationmode="country names", locations="Country", color="allsum", color_continuous_scale="Cividis")
# fig = px.choropleth(data_frame=df, locationmode="country names", locations="Country", color="allsum")
fig.update_layout(coloraxis_colorbar=dict(title=None))
fig.update_layout({"plot_bgcolor" : "rgba(0,0,0,0)", "paper_bgcolor" : "rgba(0,0,0,0)"})
# fig.write_image("image/geomap.png")
pio.write_image(fig, 'image/geomap.png', format='png', width=1200, height=800, scale=2) 
# pyo.plot(fig)

