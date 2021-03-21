from  ..services.loader import Loader

class Transparence():

    def control(self):
        self.loader = Loader()

        self.loader.loadcsv()

        print(self.loader.entreprises)        
        print(self.loader.entreprises)

        ### jointure entreprise et avantage


        #calcul de la rémunération (avantage)

        self.loader.avantages = self.loader.convert_row(self.loader.avantages, "avant_montant_ttc")
        data = self.loader.avantages.groupby(["entreprise_identifiant"])["avant_montant_ttc"].sum()
        print(data)


        