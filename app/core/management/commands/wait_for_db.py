"""
Django command to wait for database to be available
"""

from django.core.management import BaseCommand
from psycopg2 import OperationalError as Psycopg2OpError
from django.db import OperationalError
import time


class Command(BaseCommand):
    """Django command to wait foe db"""

    def handle(self, *args, **options):
        """Entry point"""
        self.stdout.write('Waiting for database...')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, \
                     waiting for 1 second...')
                time.sleep(1000)

        self.stdout.write(self.style.SUCCESS('Database available'))
