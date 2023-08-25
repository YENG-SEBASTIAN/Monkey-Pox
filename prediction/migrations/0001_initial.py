# Generated by Django 4.2.2 on 2023-08-02 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import prediction.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Predict',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/', validators=[prediction.models.validate_image_size])),
                ('note', models.CharField(blank=True, max_length=50, null=True)),
                ('result', models.CharField(blank=True, max_length=20, null=True)),
                ('confidence', models.PositiveIntegerField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploads', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-uploaded_at',),
            },
        ),
    ]
