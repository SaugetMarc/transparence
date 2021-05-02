from  ..services.loader import Loader
from pandas import merge, ExcelWriter
from datetime import datetime

class Transparence():



    def genere_excel_writer(self, name):
        return ExcelWriter(name +str(datetime.now().strftime("_%Y%m%d")) + '.xlsx', engine='xlsxwriter')


    def control(self, nb_entreprise, light):
        writer = self.genere_excel_writer("transparence")
        self.loader = Loader()

        self.loader.load_avantages(light)
        

        data_avantages  = self.loader.avantages[['entreprise_identifiant', 'avant_montant_ttc']]

        print(data_avantages)

        #calcul de la rémunération (avantage)      
        data = data_avantages.groupby(["entreprise_identifiant"])["avant_montant_ttc"].sum().sort_values(ascending=False).head(nb_entreprise)


        ### jointure entreprise et avantage
        self.loader.load_entreprises()
        data_merge = merge(data, self.loader.entreprises, how="left", left_on=["entreprise_identifiant"], right_on="identifiant")

        data_merge.to_excel(writer, sheet_name="Avantage")

       
        worksheet = writer.sheets["Avantage"]
        format_size = 'B2:C'+str(data.shape[0]+1)        
        worksheet.conditional_format(format_size, {'type': '3_color_scale'})
        worksheet.set_column('A:C', 20)
        
        writer.save()


        