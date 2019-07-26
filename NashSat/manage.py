#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import datetime


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NashSat.settings')

    # Creating directories to store images by year
    current_year = datetime.datetime.now().year
    print('The year is', str(current_year))
    image_dir = os.path.join('posts', 'static', 'media', 'fulls', str(current_year))
    thumb_dir = os.path.join('posts', 'static', 'media', 'thumbs', str(current_year))

    # if it is 2019 and the folder 2019 doesnt exist it will create it
    if not os.path.exists(image_dir):
        os.mkdir(os.path.join(image_dir))
    if not os.path.exists(thumb_dir):
        os.mkdir(thumb_dir)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)



if __name__ == '__main__':
    main()
