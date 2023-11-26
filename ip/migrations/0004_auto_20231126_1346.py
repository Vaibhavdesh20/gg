# Generated by Django 3.2.22 on 2023-11-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0003_rename_ip_iplist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iplist',
            name='group',
            field=models.CharField(choices=[('IP_filter_bw_open', 'IP_filter_bw_open'), ('GIMA_IT', 'GIMA_IT'), ('Lan', 'Lan'), ('GIMA_Mohotas', 'GIMA_Mohotas'), ('Gima_mac_filter_bw_open', 'Gima_mac_filter_bw_open'), ('MAC_users_512_login', 'MAC_users_512_login'), ('MAC_users_256_login', 'MAC_users_256_login'), ('gima_wireless_macs', 'gima_wireless_macs')], max_length=120),
        ),
        migrations.AlterField(
            model_name='iplist',
            name='mac_address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='iplist',
            name='site',
            field=models.CharField(choices=[('HGT', 'HGT'), ('WANI', 'WANI'), ('WVG', 'WVG'), ('WVG-OE', 'WVG-OE'), ('GIMABIO', 'GIMABIO'), ('BELA-SPG', 'BELA-SPG'), ('Yerla', 'Yerla'), ('Wander', 'Wander'), ('HITPL', 'HITPL')], max_length=50),
        ),
    ]