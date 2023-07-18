import csv
from django.core.management.base import BaseCommand
from movies.models import Movie
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Imports movies from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        insert_count = 0
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                title, genres = row
                main_genre = genres.split('|')[0]
                try:
                    movie = Movie.objects.create(title=title, genre=main_genre)
                except IntegrityError:
                    self.stderr.write(self.style.ERROR(f'Skip, {movie} is already in the database'))
                    continue
                else:
                    insert_count += 1
                    # self.stdout.write(self.style.SUCCESS(f'Successfully imported movie: {movie}'))
        self.stdout.write(self.style.SUCCESS(f'{insert_count} movies imported'))

