from django.conf import settings
from pandas import DataFrame, read_csv, read_excel, ExcelWriter



class Loader():

    def loadcsv(self):
        #fichier entreprise
        print(settings.DATA)
        self.entreprises  = read_csv(settings.DATA['entreprise'], header=0, delimiter=';', encoding='iso-8859-15', dtype=str, error_bad_lines=False)
        self.avantages  = read_csv(settings.DATA['avantage'], header=0, delimiter=';', encoding='iso-8859-15', dtype=str, error_bad_lines=False)
        self.conventions  = read_csv(settings.DATA['convention'], header=0, delimiter=';', encoding='iso-8859-15', dtype=str, error_bad_lines=False)
        self.remunerations  = read_csv(settings.DATA['remuneration'], header=0, delimiter=';', encoding='iso-8859-15', dtype=str, error_bad_lines=False)

        return true
