# Generated by Django 2.2.7 on 2019-11-27 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaria', '0002_auto_20191127_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_demands', to='pizzaria.Client'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_demands', to='pizzaria.Employee'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_demands', to='pizzaria.Pizza'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='progress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_demands', to='pizzaria.Progress'),
        ),
    ]
