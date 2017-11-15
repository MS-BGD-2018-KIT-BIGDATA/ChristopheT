import pandas as pd
# telechargement des données
# http://www.data.drees.sante.gouv.fr/TableViewer/tableView.aspx?ReportId=2489

data = pd.read_csv('rpps-medecins.csv', sep=',', header = 3, encoding='latin_1')

