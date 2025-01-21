import time
from django.core.management.base import BaseCommand
# from django.db import connections
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """Entrypoint for command."""
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                # connections['default'].cursor()
                # needed while running test separately
                #  docker-compose run --rm app sh -c 'python manage.py wait_for_db'
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))