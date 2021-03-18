from  ..services.loader import Loader

class Transparence():

    def control(self):
        self.loader = Loader()

        self.loader.loadcsv()
        print("toto")