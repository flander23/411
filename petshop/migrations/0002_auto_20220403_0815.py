# Generated by Django 3.2.5 on 2022-04-03 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contains',
            options={'ordering': ['contains_id']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'last_name', 'username']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['shop__shop_name', 'item_name']},
        ),
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['type', 'breed']},
        ),
        migrations.AlterModelOptions(
            name='porder',
            options={'ordering': ['order_id']},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ['shop_name']},
        ),
        migrations.AlterField(
            model_name='contains',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contains', to='petshop.item'),
        ),
        migrations.AlterField(
            model_name='contains',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contains', to='petshop.porder'),
        ),
        migrations.AlterField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='petshop.shop'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='customer',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='petshop.customer'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='petshop.shop'),
        ),
        migrations.AlterField(
            model_name='porder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='petshop.customer'),
        ),
    ]
