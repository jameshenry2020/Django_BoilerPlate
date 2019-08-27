from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help='Rename a Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='the new Django project')

    def handle(self, *args, **kwargs):
        new_project_name=kwargs['new_project_name']


        files_to_Rename=['django_project/settings/base.py', 'django_project/wsgi.py', 'manage.py']

        folder_to_Rename='django_project'

        for f in files_to_Rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata=filedata.replace(folder_to_Rename, new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_Rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('project has been renamed to %s' % new_project_name))

