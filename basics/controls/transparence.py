from  ..services.loader import Loader
from pandas import merge, ExcelWriter
from datetime import datetime

class Transparence():



    def genere_excel_writer(self, name):
        return ExcelWriter(name +str(datetime.now().strftime("_%Y%m%d")) + '.xlsx', engine='xlsxwriter')


    def control(self):
        writer = self.genere_excel_writer("transparence")
        self.loader = Loader()

        self.loader.loadcsv()

        print(self.loader.entreprises)        
        print(self.loader.entreprises)

        ### jointure entreprise et avantage


        #calcul de la rémunération (avantage)

        #self.loader.avantages = self.loader.convert_row(self.loader.avantages, "avant_montant_ttc")
        

        #merge de la table des entreprises pour la table des avantages        
        data_merge = merge(self.loader.avantages, self.loader.entreprises, how="left", left_on=["entreprise_identifiant"], right_on="identifiant")
        data = data_merge.groupby(["secteur","entreprise_identifiant"])["avant_montant_ttc"].sum().head(50)
        data.to_excel(writer, sheet_name="Avantage")

        worksheet = writer.sheets["Avantage"]
        format_size = 'C2:C'+str(data.shape[0]+1)        
        worksheet.conditional_format(format_size, {'type': '3_color_scale'})
        worksheet.set_column('A:C', 20)
        

        

        writer.save()


        