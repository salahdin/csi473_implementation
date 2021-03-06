# Generated by Django 2.2 on 2019-11-02 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='rent_from',
            field=models.DateTimeField(verbose_name='date rented'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='rent_to',
            field=models.DateField(verbose_name='date returned'),
        ),
        migrations.CreateModel(
            name='ReturnVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOR', models.DateField(verbose_name='date returned')),
                ('condition', models.CharField(max_length=200)),
                ('mileage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='return_Customer_id', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='return_vehicle_id', to='core.Vehicle')),
            ],
        ),
    ]
