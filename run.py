#pip install -r requirements.txt
from flask import Flask, jsonify, render_template
import csv
import pandas as pd
import numpy as np

app = Flask(__name__)

#supervivientes del titanic
crimes_df = pd.read_csv("static\data\Crimes.csv")
crimes_sel = crimes_df[(crimes_df['District']==22) & (crimes_df["Arrest"].notnull())]

@app.route('/')
def index():
    return render_template('home.html')

def calculate_percentage(val, total):
    """calcula los procentajes del total"""
    percent = np.divide(val, total)
    return percent

@app.route('/get_piechart_data')
def get_piechart_data():
    class_labels = ['ARSON', 'ASSAULT', 'BATTERY','BURGLARY', 'BURGLARY', 'CONCEALED CARRY LICENSE VIOLATION', 'CRIM SEXUAL ASSAULT', 'CRIMINAL DAMAGE', 'CRIMINAL SEXUAL ASSAULT', 'CRIMINAL TRESPASS', 'DECEPTIVE PRACTICE','GAMBLING','HOMICIDE','HUMAN TRAFFICKING','INTERFERENCE WITH PUBLIC OFFICER','INTIMIDATION','KIDNAPPING','LIQUOR LAW VIOLATION','MOTOR VEHICLE THEFT','NARCOTICS','NON-CRIMINAL','OBSCENITY','OFFENSE INVOLVING CHILDREN','OTHER NARCOTIC VIOLATION','OTHER OFFENSE','PROSTITUTION ','PUBLIC INDECENCY ','PUBLIC PEACE VIOLATION ','ROBBERY ','SEX OFFENSE','STALKING','THEFT','WEAPONS VIOLATION']
    pclass_percent = calculate_percentage(crimes_sel.groupby('Primary Type').size().values, crimes_sel['ID'].count())*100
    pieChartData = []
    for index, item in enumerate(pclass_percent):
        eachData = {}
        eachData['category'] = class_labels[index]
        eachData['measure'] =  round(item,1)
        pieChartData.append(eachData)

    return jsonify(pieChartData)

@app.route('/get_barchart_data')
def get_barchart_data():
    com_labels = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016', '2017', '2018', '2019', '2020', '2021']
    crimes_sel["com_labels"] = pd.cut(crimes_sel.Year, range(2001,2023,1) , right=False, labels=com_labels)
    crimes_sel[['com_labels', 'Primary Type']]

    crimes1 = crimes_sel[crimes_sel['Primary Type']=='ARSON']
    crimes2 = crimes_sel[crimes_sel['Primary Type']=='ASSAULT']
    crimes3 = crimes_sel[crimes_sel['Primary Type']=='BATTERY']
    crimes4 = crimes_sel[crimes_sel['Primary Type']=='BURGLARY']
    crimes5 = crimes_sel[crimes_sel['Primary Type']=='CONCEALED CARRY LICENSE VIOLATION']
    crimes6 = crimes_sel[crimes_sel['Primary Type']=='CRIM SEXUAL ASSAULT']
    crimes7 = crimes_sel[crimes_sel['Primary Type']=='CRIMINAL DAMAGE']
    crimes8 = crimes_sel[crimes_sel['Primary Type']=='CRIMINAL SEXUAL ASSAULT']
    crimes9 = crimes_sel[crimes_sel['Primary Type']=='CRIMINAL TRESPASS']
    crimes10 = crimes_sel[crimes_sel['Primary Type']=='DECEPTIVE PRACTICE']
    crimes11 = crimes_sel[crimes_sel['Primary Type']=='GAMBLING']
    crimes12 = crimes_sel[crimes_sel['Primary Type']=='HOMICIDE']
    crimes13 = crimes_sel[crimes_sel['Primary Type']=='HUMAN TRAFFICKING']
    crimes14 = crimes_sel[crimes_sel['Primary Type']=='INTERFERENCE WITH PUBLIC OFFICER']
    crimes15 = crimes_sel[crimes_sel['Primary Type']=='INTIMIDATION']
    crimes16 = crimes_sel[crimes_sel['Primary Type']=='KIDNAPPING']
    crimes17 = crimes_sel[crimes_sel['Primary Type']=='LIQUOR LAW VIOLATION']
    crimes18 = crimes_sel[crimes_sel['Primary Type']=='MOTOR VEHICLE THEFT']
    crimes19 = crimes_sel[crimes_sel['Primary Type']=='NARCOTICS']
    crimes20 = crimes_sel[crimes_sel['Primary Type']=='NON-CRIMINAL']
    crimes21 = crimes_sel[crimes_sel['Primary Type']=='OBSCENITY']
    crimes22 = crimes_sel[crimes_sel['Primary Type']=='OFFENSE INVOLVING CHILDREN']
    crimes23 = crimes_sel[crimes_sel['Primary Type']=='OTHER NARCOTIC VIOLATION']
    crimes24 = crimes_sel[crimes_sel['Primary Type']=='OTHER OFFENSE']
    crimes25 = crimes_sel[crimes_sel['Primary Type']=='PUBLIC INDECENCY']
    crimes26 = crimes_sel[crimes_sel['Primary Type']=='PUBLIC PEACE VIOLATION']
    crimes27 = crimes_sel[crimes_sel['Primary Type']=='ROBBERY']
    crimes28 = crimes_sel[crimes_sel['Primary Type']=='SEX OFFENSE']
    crimes29 = crimes_sel[crimes_sel['Primary Type']=='STALKING']
    crimes30 = crimes_sel[crimes_sel['Primary Type']=='THEFT']
    crimes31 = crimes_sel[crimes_sel['Primary Type']=='WEAPONS VIOLATION']

    percentAll = calculate_percentage(crimes_sel.groupby('Year').size().values,crimes_sel['ID'].count())*100
    percent1 = calculate_percentage(crimes1.groupby('Year').size().values,crimes1['ID'].count())*100
    percent2 = calculate_percentage(crimes1.groupby('Year').size().values,crimes2['ID'].count())*100
    percent3 = calculate_percentage(crimes1.groupby('Year').size().values,crimes3['ID'].count())*100
    percent4 = calculate_percentage(crimes1.groupby('Year').size().values,crimes4['ID'].count())*100
    percent5 = calculate_percentage(crimes1.groupby('Year').size().values,crimes5['ID'].count())*100
    percent6 = calculate_percentage(crimes1.groupby('Year').size().values,crimes6['ID'].count())*100
    percent7 = calculate_percentage(crimes1.groupby('Year').size().values,crimes7['ID'].count())*100
    percent8 = calculate_percentage(crimes1.groupby('Year').size().values,crimes8['ID'].count())*100
    percent9 = calculate_percentage(crimes1.groupby('Year').size().values,crimes9['ID'].count())*100
    percent10 = calculate_percentage(crimes1.groupby('Year').size().values,crimes10['ID'].count())*100
    percent11 = calculate_percentage(crimes1.groupby('Year').size().values,crimes11['ID'].count())*100
    percent12 = calculate_percentage(crimes1.groupby('Year').size().values,crimes12['ID'].count())*100
    percent13 = calculate_percentage(crimes1.groupby('Year').size().values,crimes13['ID'].count())*100
    percent14 = calculate_percentage(crimes1.groupby('Year').size().values,crimes14['ID'].count())*100
    percent15 = calculate_percentage(crimes1.groupby('Year').size().values,crimes15['ID'].count())*100
    percent16 = calculate_percentage(crimes1.groupby('Year').size().values,crimes16['ID'].count())*100
    percent17 = calculate_percentage(crimes1.groupby('Year').size().values,crimes17['ID'].count())*100
    percent18 = calculate_percentage(crimes1.groupby('Year').size().values,crimes18['ID'].count())*100
    percent19 = calculate_percentage(crimes1.groupby('Year').size().values,crimes19['ID'].count())*100
    percent20 = calculate_percentage(crimes1.groupby('Year').size().values,crimes20['ID'].count())*100
    percent21 = calculate_percentage(crimes1.groupby('Year').size().values,crimes21['ID'].count())*100
    percent22 = calculate_percentage(crimes1.groupby('Year').size().values,crimes22['ID'].count())*100
    percent23 = calculate_percentage(crimes1.groupby('Year').size().values,crimes23['ID'].count())*100
    percent24 = calculate_percentage(crimes1.groupby('Year').size().values,crimes24['ID'].count())*100
    percent25 = calculate_percentage(crimes1.groupby('Year').size().values,crimes25['ID'].count())*100
    percent26 = calculate_percentage(crimes1.groupby('Year').size().values,crimes26['ID'].count())*100
    percent27 = calculate_percentage(crimes1.groupby('Year').size().values,crimes27['ID'].count())*100
    percent28 = calculate_percentage(crimes1.groupby('Year').size().values,crimes28['ID'].count())*100
    percent29 = calculate_percentage(crimes1.groupby('Year').size().values,crimes29['ID'].count())*100
    percent30 = calculate_percentage(crimes1.groupby('Year').size().values,crimes30['ID'].count())*100
    percent31 = calculate_percentage(crimes1.groupby('Year').size().values,crimes31['ID'].count())*100

    barChartData = []
    for index, item in enumerate(percentAll):
        eachBarChart = {}
        eachBarChart['group'] = "All"
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(percent1):
        eachBarChart = {}
        eachBarChart['group'] = 'ARSON'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent1):
        eachBarChart = {}
        eachBarChart['group'] = 'ASSAULT'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent2):
        eachBarChart = {}
        eachBarChart['group'] = 'BATTERY'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(percent3):
        eachBarChart = {}
        eachBarChart['group'] = 'BURGLARY'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent4):
        eachBarChart = {}
        eachBarChart['group'] = 'CRIMINAL DAMAGE'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent5):
        eachBarChart = {}
        eachBarChart['group'] = 'CRIM SEXUAL ASSAULT'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent6):
        eachBarChart = {}
        eachBarChart['group'] = 'CRIMINAL TRESPASS'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent7):
        eachBarChart = {}
        eachBarChart['group'] = 'DECEPTIVE PRACTICE'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(percent8):
        eachBarChart = {}
        eachBarChart['group'] = 'GAMBLING'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent9):
        eachBarChart = {}
        eachBarChart['group'] = 'HOMICIDE'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent10):
        eachBarChart = {}
        eachBarChart['group'] = 'HUMAN TRAFFICKING'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent12):
        eachBarChart = {}
        eachBarChart['group'] = 'INTIMIDATION'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(percent13):
        eachBarChart = {}
        eachBarChart['group'] = 'KIDNAPPING'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent14):
        eachBarChart = {}
        eachBarChart['group'] = 'LIQUOR LAW VIOLATION'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent15):
        eachBarChart = {}
        eachBarChart['group'] = 'MOTOR VEHICLE THEFT'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent16):
        eachBarChart = {}
        eachBarChart['group'] = 'NARCOTICS'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent17):
        eachBarChart = {}
        eachBarChart['group'] = 'NON-CRIMINAL'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent18):
        eachBarChart = {}
        eachBarChart['group'] = 'OBSCENITY'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent19):
        eachBarChart = {}
        eachBarChart['group'] = 'OFFENSE INVOLVING CHILDREN'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent20):
        eachBarChart = {}
        eachBarChart['group'] = 'OTHER NARCOTIC VIOLATION'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent21):
        eachBarChart = {}
        eachBarChart['group'] = 'OTHER OFFENSE'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent22):
        eachBarChart = {}
        eachBarChart['group'] = 'PROSTITUTION'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(percent23):
        eachBarChart = {}
        eachBarChart['group'] = 'PUBLIC INDECENCY '
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(percent24):
        eachBarChart = {}
        eachBarChart['group'] = 'PUBLIC PEACE VIOLATION '
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent25):
        eachBarChart = {}
        eachBarChart['group'] = 'ROBBERY '
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
        
    for index, item in enumerate(percent26):
        eachBarChart = {}
        eachBarChart['group'] = 'SEX OFFENSE'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(percent27):
        eachBarChart = {}
        eachBarChart['group'] = 'STALKING'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(percent28):
        eachBarChart = {}
        eachBarChart['group'] = 'THEFT'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)

    for index, item in enumerate(percent29):
        eachBarChart = {}
        eachBarChart['group'] = 'WEAPONS VIOLATION'
        eachBarChart['category'] = com_labels[index]
        eachBarChart['measure'] = round(item,1)
        barChartData.append(eachBarChart)
    
    return jsonify(barChartData)


if __name__ == '__main__':
      app.run(debug=True)