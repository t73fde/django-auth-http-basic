#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test dummy to allow tests with Django environment.

:copyright: (c) 2016 by Detlef Stern
:license: Apache 2.0, see LICENSE
"""

import sys

if __name__ == "__main__":
    from django.conf import settings
    from django.core.management import execute_from_command_line

    settings.configure()
    settings.INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
    )
    settings.DATABASES = {
        'default': {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "temp.db",
        }
    }
    execute_from_command_line(sys.argv)
