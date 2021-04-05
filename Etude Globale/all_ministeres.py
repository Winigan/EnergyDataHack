import pandas as pd
from matplotlib import pyplot as plt

name = 'Vague1Lot2' + '.csv' #TODO

df1 = pd.read_csv(name)
df_reg = pd.read_csv('code-postal.csv')

#avant de merge, les code postaux doivent avoir le mm type
df1[['CODE POSTAL']] = df1[['CODE POSTAL']].apply(pd.to_numeric)
df_reg[['CODE POSTAL']] = df_reg[['CODE POSTAL']].apply(pd.to_numeric)

df_join = pd.merge(df1, df_reg, how='left').drop_duplicates()

#save csv qui contient code postal associé à leur région: (pr etre sur que chaque ministere a bien une région associée, car csv de région ne contient pas tt les codes postaux)
df_to_save = df_join[['Ministère (Client)', 'CODE POSTAL','Région']]
df_to_save.to_csv('ministere_region99.csv', sep='\t') #99


#df2= pd.read_csv('ministère_region99.csv') #99
#df_final = pd.merge(df1, df2)
#df_join.to_csv('V1L2Final.csv', sep='\t') #TODO


df11 = pd.read_csv('V1L1F.csv')
df12 = pd.read_csv('V1L2F.csv')
df_V1 = pd.concat([df11, df12])
#df_V1.to_csv('Vague1.csv', sep='\t')


#nb de ministeres par catégories:
print(df_V1.groupby('Ministère (Client)').size())

#nb ministeres (vague1) par région:
region = df_V1.groupby('Région')

groupregion = region.size().reset_index(name='Size')
size = groupregion['Size'].to_numpy()
array_size = [data for data in size]

name = groupregion['Région'].to_numpy()
array_region = [data for data in name]
#plt.bar(array_region, array_size)
#plt.ylabel('Nombre de Ministères')
#plt.xlabel('Régions')
#plt.title('Répartitions des Ministères par région')
#plt.gca().xaxis.set_ticklabels(array_region, rotation=45, fontsize=8)
#plt.show()


#conso totale par région
conso = region.sum()['TOTAL '].to_numpy()

array_conso = [data for data in conso]
#plt.bar(array_region, array_conso)
#plt.ylabel('Consommation totale (KWh)')
#plt.xlabel('Régions')
#plt.title('Consommation totale des ministères par région en 2014 (en KWh)')
#plt.gca().xaxis.set_ticklabels(array_region, rotation=45, fontsize=8)
#plt.show()


#nb denergie verte par région
array_vert = []
for reg in array_region:
    vert = region['Electricité 100% verte (oui/non)'].value_counts().reset_index(name = 'Count')
    subvert = vert[(vert.Région == reg)]
    nb_oui = subvert[(subvert['Electricité 100% verte (oui/non)'] == 'OUI')].Count
    nb_non = subvert[(subvert['Electricité 100% verte (oui/non)'] == 'NON')].Count

    if nb_non.shape[0] == 0:
        val = 1
    else:
        val = nb_oui.iloc[0] / (nb_oui.iloc[0] + nb_non.iloc[0])

    array_vert.append(val*100)
array_vert = [data for data in array_vert]
print(array_vert)
plt.bar(array_region, array_vert)
plt.ylabel('Pourcentage du nombre de ministères possédant une éléctricité 100% verte')
plt.xlabel('Régions')
plt.title('Proportion d\'électricité 100% verte par région')
plt.gca().xaxis.set_ticklabels(array_region, rotation=45, fontsize=8)
plt.show()

#df_V1['souscription totale'] = df_V1['P'] + df_V1['HPH'] + df_V1['HCH'] + df_V1['HPE'] + df_V1['HCE'] + df_V1['HH (EJP)'] + df_V1['P (EJP)']
#print(df_V1.head())

