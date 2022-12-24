import time

from django.core.management import BaseCommand
from django.db import OperationalError, connection
from django.db.backends.dummy.base import DatabaseWrapper

connection: DatabaseWrapper = connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for db...')
        db_connection = False

        while not db_connection:
            try:
                connection.ensure_connection()
                db_connection = True
            except OperationalError:
                self.stdout.write('DataBase is unavailable, wait 1 second...')
                time.sleep(1)

        self.stdout.write('DataBase is available!!!')
