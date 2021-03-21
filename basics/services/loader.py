from django.conf import settings
from pandas import DataFrame, read_csv, read_excel, ExcelWriter



class Loader():
    def convert_to_float(self, val):
        try:
            val = float(val.replace(",", "."))
        except Exception:
            return 0
        return val

    def loadcsv(self):
        #fichier entreprise
        print(settings.DATA)
        self.entreprises  = read_csv(settings.DATA['entreprise'], header=0, delimiter=';', encoding='iso-8859-15', dtype=str, error_bad_lines=False)
        self.avantages  = read_csv(settings.DATA['avantage'], header=0, delimiter=';', encoding='iso-8859-15', dtype=str, error_bad_lines=False)
        self.conventions  = read_csv(settings.DATA['convention'], header=0, delimiter=';', encoding='iso-8859-15', dtype=str, error_bad_lines=False)
        self.remunerations  = read_csv(settings.DATA['remuneration'], header=0, delimiter=';', encoding='iso-8859-15', dtype=str, error_bad_lines=False)

        return True

    def convert_row(self, df, cols):
        df[cols] = df.apply(lambda x : self.convert_to_float(x[cols]), axis=1)
        return df

