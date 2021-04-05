import numpy as np
import sys
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd 
import pylab
from pandas.plotting import register_matplotlib_converters
import os

def construct_dataset(filepath):
    dataset=pd.read_csv(filepath,delimiter="\s+", names=["date","time","0min","10min","20min","30min","40min","50min"],parse_dates=["date","time"])
    dataset["hourValue"] = dataset["0min"] + dataset["10min"] + dataset["20min"] + dataset["30min"] + dataset["40min"] + dataset["50min"]
    dataset["weekNum"] = dataset["date"].dt.week
    dataset["datetime"] = dataset["time"].dt.hour 
    dataset["dayOfWeek"] = dataset.date.dt.dayofweek

    return dataset

files = []
if len(sys.argv) == 1:
    print("Aide: le script prend en argument soit juste le chemin du fichier que vous voulez utiliser soit un dossier avec le paramettre -dir avant le chemin du dossier")

if len(sys.argv) > 2 and sys.argv[1] == "-dir":
    for file in os.listdir(sys.argv[2]):
        files.append(sys.argv[2] + file)
if len(sys.argv) == 2:
    files.append(sys.argv[1])

print(files)

for filepath in files:

    print("Affichae du fichier: " + filepath)

    dataset = construct_dataset(filepath)
    fig, axs = plt.subplots(figsize=(12, 4))
    dataset.groupby(dataset["time"].dt.hour)["hourValue"].mean().plot(kind='bar', rot=0, ax=axs)
    plt.xlabel("Heure")

    fig, axs = plt.subplots()
    averageWeek = dataset.groupby(['dayOfWeek','datetime']).hourValue.mean()
    averageWeek.plot(x="datetime",y="hourValue")
    axs.set_xlabel("(Jour de la semaine, heure)")
        
    pylab.show()