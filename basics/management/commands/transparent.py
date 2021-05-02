from django.core.management.base import BaseCommand, CommandError
from ...controls.transparence import Transparence

class Command(BaseCommand):
    help = 'Génére excel formater à partir de la base transparence'

    def add_arguments(self, parser):
        parser.add_argument('nb_entreprise', nargs='+', type=int)
        parser.add_argument('light', nargs='+', type=int)

    def handle(self, *args, **options):

        self.controls = Transparence()
        print(options['nb_entreprise'])
        self.controls.control(options['nb_entreprise'][0], options['light'][0])

        

        self.stdout.write(self.style.SUCCESS('Fichier géneré'))

