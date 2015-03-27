# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sc1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='question_text',
            new_name='title',
        ),
    ]
