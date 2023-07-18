import csv
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Imports movies from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        i = 0
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                i += 1
                title, genres = row
                main_genre = genres.split('|')[0]
                movie = Movie.objects.create(title=title, genre=main_genre)
                self.stdout.write(self.style.SUCCESS(f'Successfully imported movie: {movie}'))
        self.stdout.write(self.style.SUCCESS(f'{i} movies imported'))

