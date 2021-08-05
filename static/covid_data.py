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


def male_vaccination():
    y = [male_vaccinated, male_notvaccinated]
    label = ['Vaccinated', 'Not Vaccinated']
    fig=plt.figure()
    plt.pie(y,labels=label,autopct="%1.1f%%")
    # plt.title("Male Vaccination")
    return fig

def female_vaccination():
    y1 = [female_vaccinated, female_notvaccinated]
    label1 = ['Vaccinated', 'Not Vaccinated']
    fig=plt.figure()
    plt.pie(y1,labels=label1,autopct='%1.1f%%')
    # plt.title("Female Vaccination")
    return fig

def transgender_vaccination():
    y2 = [transgender_vaccinated, transgender_notvaccinated]
    label2 = ['Vaccinated', 'Not Vaccinated']
    fig=plt.figure()
    plt.pie(y2,labels=label2,autopct='%1.1f%%')
    # plt.title("Transgender Vaccination")
    return fig

state_data=data[['State','Updated On','Male(Individuals Vaccinated)','Female(Individuals Vaccinated)','Transgender(Individuals Vaccinated)']]
state_data.set_index('Updated On')


state_wise_population={
    
"India":1371360350,
"Uttar Pradesh":237882725,
"Maharashtra":123144223,
"Rajasthan":81032689,
"Gujarat":63872399,
"Karnataka":67562686,
"Madhya Pradesh":85358965,
"West Bengal":99609303,
"Bihar":124799926,
"Tamil Nadu":77841267,
"Andhra Pradesh":53903393,
"Kerala":35699443,
"Odisha":46356334,
"Telangana":39362732,
"Haryana":28204692,
"Chhattisgarh":29436231,
"Delhi":18710922,
"Assam":35607039,
"Jharkhand":38593948,
"Punjab":30141373,
"Jammu and Kashmir":13606320,
"Uttarakhand":11250858,
"Himachal Pradesh":7451955,
"Tripura":4169794,
"Goa":1586250,
"Meghalaya":3366710,
"Manipur":3091545,
"Mizoram":1239244,
"Arunachal Pradesh":1570458,
"Nagaland":2249695,
"Chandigarh":1158473,
"Puducherry":1413542,
"Sikkim":690251,
"Dadra and Nagar Haveli and Daman and Diu":615724,
"Ladakh":289023,
"Andaman and Nicobar Islands":417036,
"Lakshadweep":73183
    
}

df.columns = [c.replace(' ', '_') for c in df.columns]
State_wise_total_vaccinated = {}
perc_popul_vaccinated=[]
state_population=[]
for State in df.State.unique() : 
    vaccinated = 0
    for i in range(len(df)) : 
        if df.State[i] == State and df.Updated_On[i] =='02/07/2021' : 
            vaccinated = df.Total_Individuals_Vaccinated[i]
            state_population.append(state_wise_population[State])
            perc_popul_vaccinated.append(round((vaccinated*100)/state_wise_population[State],2))
            break
    State_wise_total_vaccinated[State] = vaccinated 
#     made a seperate dict from the df 
State_wise_total_vaccinated_df = pd.DataFrame.from_dict(State_wise_total_vaccinated, orient='index', columns = ['total_individuals_vaccinated_till_date'])
#     converted dict to df 

# print(len(State_wise_total_vaccinated_df.index))
# print(len(state_population))

State_wise_total_vaccinated_df['Population']=state_population
State_wise_total_vaccinated_df['%_population_vaccinated']=perc_popul_vaccinated
# State_wise_total_vaccinated_df.sort_values(by = 'total_individuals_vaccinated_till_date', ascending = False, inplace = True)
State_wise_total_vaccinated_df=State_wise_total_vaccinated_df.iloc[1:]
State_wise_total_vaccinated_df.sort_values(by = '%_population_vaccinated', ascending = False, inplace = True)

def state_1stdose():
    fig=plt.figure(figsize=(20,10))
    plt.bar(State_wise_total_vaccinated_df.index,State_wise_total_vaccinated_df["%_population_vaccinated"])

    plt.xticks(rotation=90)
    plt.ylabel('% population')
    #Most vaccinated states by %
    # plt.title("Vaccination per State")
    return fig

State_wise_second_dose = {}
scnd_dose_perc_popul_vaccinated=[]
# state_population=[]
for State in df.State.unique() : 
    vaccinated = 0
    for i in range(len(df)) : 
        if df.State[i] == State and df.Updated_On[i] =='02/07/2021' : 
            vaccinated = df.Second_Dose_Administered[i]
            scnd_dose_perc_popul_vaccinated.append(round((vaccinated*100)/state_wise_population[State],2))
            break
    State_wise_second_dose[State] = vaccinated 
#     made a seperate dict from the df 
State_wise_second_dose_df = pd.DataFrame.from_dict(State_wise_second_dose,orient='index',columns = ['Second Dose Administered'])


State_wise_second_dose_df["Population"]=state_population
State_wise_second_dose_df['%_population_vaccinated_second_dose']=scnd_dose_perc_popul_vaccinated
State_wise_second_dose_df.sort_values(by = '%_population_vaccinated_second_dose', ascending = False, inplace = True)
State_wise_second_dose_df=State_wise_second_dose_df.iloc[1:]  

def state_2nddose():
    fig=plt.figure(figsize=(20,10))
    plt.bar(State_wise_second_dose_df.index,State_wise_second_dose_df['%_population_vaccinated_second_dose'])
    plt.xticks(rotation=90)
    plt.ylabel('% population')
    #Most vaccinated states by %
    # plt.title("Vaccination per State(Second Dose)")
    return fig


req_vaccine_data=df[["Updated_On","State",'Total_Doses_Administered',"Total_CoviShield_Administered","Total_Covaxin_Administered"]]
State_wise_covaxin_dose = {}
perc_covaxin=[]
prec_covishield=[]
total_doses=[]
for State in df.State.unique() : 
    covaxin_doses = 0
    for i in range(len(df)) : 
        if df.State[i] == State and df.Updated_On[i] =='02/07/2021' : 
            covaxin_doses = df.Total_Covaxin_Administered[i]
            break
    State_wise_covaxin_dose[State] = covaxin_doses 
    total_doses.append(df.Total_Doses_Administered[i])
#     made a seperate dict from the df 
State_wise_covaxin_dose_df = pd.DataFrame.from_dict(State_wise_covaxin_dose,orient='index',columns = ['Total_Covaxin_Administered'])

State_wise_covishield_dose = {}
perc_covaxin=[]
prec_covishield=[]
# state_population=[]
for State in df.State.unique() : 
    covishield_doses = 0
    for i in range(len(df)) : 
        if df.State[i] == State and df.Updated_On[i] =='02/07/2021' : 
            covishield_doses = df.Total_CoviShield_Administered[i]
#             scnd_dose_perc_popul_vaccinated.append(round((vaccinated*100)/state_wise_population[State],2))
            break
    State_wise_covishield_dose[State] = covishield_doses 
#     made a seperate dict from the df 
State_wise_covishield_dose_df = pd.DataFrame.from_dict(State_wise_covishield_dose,orient='index',columns = ['Total_CoviShield_Administered'])
State_wise_covishield_dose_df['Total_Covaxin_Administered']=State_wise_covaxin_dose_df['Total_Covaxin_Administered']
State_wise_covishield_dose_df['Total_doses']=total_doses
vaccine_df=State_wise_covishield_dose_df

perc_covaxin=[]
perc_covishield=[]
for i in range(len(vaccine_df)):
    a=round((vaccine_df.Total_CoviShield_Administered[i]*100)/(vaccine_df.Total_doses[i]),2)
    b=round((vaccine_df.Total_Covaxin_Administered[i]*100)/(vaccine_df.Total_doses[i]),2)    
    perc_covaxin.append(b)
    perc_covishield.append(a)

vaccine_df['%_covaxin']=perc_covaxin
vaccine_df['%_covishield']=perc_covishield
vaccine_df=vaccine_df.iloc[1:]    

def covaxin():
    vaccine_df.sort_values(by='%_covaxin',ascending=False,inplace=True)
    fig=plt.figure(figsize=(20,10))
    plt.bar(vaccine_df.index,vaccine_df['%_covaxin'])
    plt.ylabel("%_doses")
    plt.xticks(rotation=90)
    #Most vaccinated states by %
    # plt.title("Covaxin Doses")
    return fig


def covishield():
    vaccine_df.sort_values(by='%_covishield',ascending=False,inplace=True)
    fig=plt.figure(figsize=(20,10))
    plt.bar(vaccine_df.index,vaccine_df['%_covishield'])
    plt.xticks(rotation=90)
    plt.ylabel("%_doses")
    #Most vaccinated states by %
    # plt.title("Covishield Doses")
    return fig    