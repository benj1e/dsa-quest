from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
import os


class Command(BaseCommand):
    help = "Generates a SECRET_KEY for the Django settings file when necessary."

    def handle(self, *args, **options):
        new_secret_key = get_random_secret_key()
        env_path = os.path.join(os.getcwd(), ".env")
        if os.path.exists(env_path):
            lines = []
            with open(env_path, "r") as f:
                lines = f.readlines()

            with open(env_path, "w", newline="\n") as f:
                updated = False
                for line in lines:
                    if line.startswith("SECRET_KEY="):
                        f.write(f'SECRET_KEY="{new_secret_key}"\n')
                        updated = True
                    else:
                        f.write(line)

                if not updated:
                    f.write(f'SECRET_KEY="{new_secret_key}"\n')

            self.stdout.write(self.style.SUCCESS("SECRET_KEY has been rotated."))
        else:
            with open(env_path, "w", newline="\n") as f:
                f.write("")
            self.stdout.write(self.style.ERROR(".env file not found."))
