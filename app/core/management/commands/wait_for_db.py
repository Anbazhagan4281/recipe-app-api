"""
Django Command Wait for the Database is Available
"""

import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Django command wait for db avilable
    """

    def handle(self, *args, **options):
        self.stdout.write("Waiting for Database Connection")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2Error, OperationalError):
                self.stdout.write("Database Unabile to connect 1s")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database is avilable"))
