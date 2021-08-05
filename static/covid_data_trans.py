import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import csv
#actual_data-->dataframe
from pathlib import Path

actual_data=pd.read_csv("static/cowin_vaccine_data_statewise.csv")
actual_data['Updated On']=pd.to_datetime(actual_data['Updated On'])
df=pd.read_csv("static/cowin_vaccine_data_statewise.csv")
# df['Updated On']=pd.to_datetime(df['Updated On'])
data=actual_data.drop(['Total Sessions Conducted','Total Sites ','Total Sputnik V Administered','AEFI','18-45 years (Age)','45-60 years (Age)','60+ years (Age)'],axis=1)

req_data=data.set_index('State')
req_data=req_data.loc["India"]

gender_data=req_data[['Updated On','Male(Individuals Vaccinated)','Female(Individuals Vaccinated)','Transgender(Individuals Vaccinated)']]

male_population=717100000
female_population=662900000
transgender_population=490000

male_vaccinated=gender_data.iloc[167].loc['Male(Individuals Vaccinated)']
male_notvaccinated=male_population-male_vaccinated
female_vaccinated=gender_data.iloc[167].loc['Female(Individuals Vaccinated)']
female_notvaccinated=female_population-female_vaccinated
transgender_vaccinated=gender_data.iloc[167].loc['Transgender(Individuals Vaccinated)']
transgender_notvaccinated=transgender_population-transgender_vaccinated


def transgender_vaccination():
    y2 = [transgender_vaccinated, transgender_notvaccinated]
    label2 = ['Vaccinated', 'Not Vaccinated']
    fig2=plt.figure()
    plt.pie(y2,labels=label2,autopct='%1.1f%%')
    plt.title("Transgender Vaccination")
    return fig2