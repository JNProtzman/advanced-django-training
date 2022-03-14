import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until db is ready"""

    def handle(self, *args, **options):
        while True:
            self.stdout.write('Waiting for database...')
            try:
                db_conn = connections['default']
                if not db_conn:
                    continue
                self.stdout.write(self.style.SUCCESS('Database available!'))
                break
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
