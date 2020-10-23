import pandas as pd
import plotly.express as px
import datetime
import streamlit as st

st.title('Inetum Coffee Analytics with Streamlit')


data_coffee = pd.read_csv("./dataset.csv")

data_coffee["prix_total_sum"] = data_coffee.groupby("validation_date")["prix_total"].transform("sum")

dates = [2019,2020]

for date in dates : 
    df_grouped_prix_total = data_coffee.groupby("validation_date", as_index=False)["validation_date", "prix_total"].sum()
    df_grouped_prix_total["years"] = df_grouped_prix_total["validation_date"].map(lambda x: datetime.datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S').year)
    df_grouped_prix_total = df_grouped_prix_total[df_grouped_prix_total['years'] == date]
    st.subheader(date)
    st.write('Total des ventes de café en ',date, ' : ',df_grouped_prix_total['prix_total'].sum(), '€')
    st.write('Ventes moyenne mensuelle de café en ',date, ' : ',df_grouped_prix_total['prix_total'].sum()/df_grouped_prix_total['prix_total'].count(), '€')
    
df_grouped_prix_total = data_coffee.groupby("validation_date", as_index=False)["validation_date", "prix_total"].sum()
df_grouped_prix_total["years"] = df_grouped_prix_total["validation_date"].map(lambda x: datetime.datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S').year)

fig = px.bar(df_grouped_prix_total, x=df_grouped_prix_total.validation_date, y=df_grouped_prix_total.prix_total, text=df_grouped_prix_total.prix_total)
fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_layout(transition_duration=500)
fig