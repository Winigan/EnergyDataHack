import pandas as pd

def xls_to_csv(xls_name, vague_nb, lot_nb):
    xls = xls_name + '.xls'
    read_file = pd.read_excel(xls)
    csv = 'Vague' + str(vague_nb) + 'Lot' + str(lot_nb) + '.csv'
    read_file.to_csv(csv, index=None, header=True)

for i in [1, 2, 3]:
    for j in [1, 2]:
        xls_name = 'Vague ' + str(i) + ' - Lot ' + str(j) + ' - Consommation annuelle d\'électricité'
 #       xls_to_csv(xls_name, i, j)

xls_to_csv('V1L2modif', 1, 2)
