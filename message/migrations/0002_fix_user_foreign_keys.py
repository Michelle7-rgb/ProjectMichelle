# Generated manually to correct broken foreign keys in the message app.

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='locataire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations_locataire', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='proprietaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations_proprietaire', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='expediteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
