# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliavel', '0003_avaliavel_beta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliavel_beta',
            name='endereco_beta',
            field=models.OneToOneField(null=True, blank=True, to='core.Endereco_Beta'),
            preserve_default=True,
        ),
    ]
