from  ..services.loader import Loader
from pandas import merge

class Transparence():

    def control(self):
        self.loader = Loader()

        self.loader.loadcsv()

        print(self.loader.entreprises)        
        print(self.loader.entreprises)

        ### jointure entreprise et avantage


        #calcul de la rémunération (avantage)

        self.loader.avantages = self.loader.convert_row(self.loader.avantages, "avant_montant_ttc")
        

        #merge de la table des entreprises pour la table des avantages

        print(self.loader.avantages[["entreprise_identifiant"]])
        print(self.loader.entreprises[["identifiant"]])
        data_merge = merge(self.loader.avantages, self.loader.entreprises, how="left", left_on=["entreprise_identifiant"], right_on="identifiant")
        print(data_merge)

        data = data_merge.groupby(["secteur","entreprise_identifiant"])["avant_montant_ttc"].sum()
        print(data)


        