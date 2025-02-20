#!/usr/bin/env python
""" 
! _____  _____  _____  __ ___ __  __  _____  ____  _____
!/  _  \/  _  \/  _  \|  |  //  \/  \/  _  \/    \/   __\
!|  _  <|  |  ||  |  ||  _ < |  \/  ||  _  |\-  -/|   __|
!\_____/\_____/\_____/|__|__\\__ \__/\__|__/ |__| \_____/


"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmate.settings')
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
