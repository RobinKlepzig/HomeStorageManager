#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HomeStorageManager.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":

    # Copy initial db files if empty
    srcdb = './db-initial/db.sqlite3'
    dstdb = './db/'
    cmddb = f'cp -r -n {srcdb} {dstdb}'
    os.system(cmddb)

    # Copy initial media files if empty
    srcmedia = './media-initial/images'
    dstmedia = './media/'
    cmdmedia = f'cp -r -n {srcmedia} {dstmedia}'
    os.system(cmdmedia)

    main()
