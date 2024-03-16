from django.core.management.base import BaseCommand
from sleeptracker.data_index import index_data_to_file

class Command(BaseCommand):
    help = 'Index sleep data to a file'

    def handle(self, *args, **options):
        index_data_to_file('sleep_records.json')
