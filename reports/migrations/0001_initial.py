# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSCReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('omt_id', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(b'^[0-9a-zA-Z]*$', b'Only alphanumeric characters are allowed.')])),
                ('vle_name', models.CharField(max_length=50, null=True, blank=True)),
                ('gaon_panchayat_name', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('mobile_number', models.CharField(max_length=12)),
                ('infra_details', models.CharField(max_length=100, null=True, blank=True)),
                ('connectivity_modes', models.CharField(max_length=2, choices=[(b'B', b'Broadband'), (b'3G', b'3G Dongle'), (b'4G', b'4G Dongle')])),
                ('num_g2c_and_g2g_services', models.IntegerField()),
                ('num_g2b_and_other_services', models.IntegerField()),
                ('remarks', models.CharField(max_length=100, null=True, blank=True)),
                ('district', models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DigitalLiteracyReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lac_name', models.CharField(max_length=50, null=True, blank=True)),
                ('num_training_centres', models.IntegerField()),
                ('num_examination_centres_near_gp', models.CharField(max_length=100, null=True, blank=True)),
                ('num_beneficiaries_registered', models.IntegerField()),
                ('num_beneficiaries_under_training', models.IntegerField()),
                ('num_beneficiaries_trained', models.IntegerField()),
                ('num_beneficiaries_appeared_in_exam', models.IntegerField()),
                ('num_beneficiaries_passed_in_exam', models.IntegerField()),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='HardwareReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hardware_nm', models.CharField(max_length=20, choices=[(b'Desktop', b'Desktop'), (b'Laptop', b'Laptop'), (b'Printers', b'Printers'), (b'Scanner', b'Scanner'), (b'UPS', b'UPS'), (b'Switch', b'Switch'), (b'Server Computer', b'Server Computer')])),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=60)),
                ('hw_in_stock', models.CharField(max_length=60)),
                ('is_amc_avaialable', models.CharField(max_length=60)),
                ('remarks', models.CharField(max_length=60)),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ManpowerReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=20)),
                ('organization', models.CharField(max_length=40)),
                ('work_location', models.CharField(max_length=60)),
                ('mobile_number', models.CharField(max_length=12)),
                ('email_id', models.EmailField(max_length=254)),
                ('district', models.CharField(blank=True, max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NOFNReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gp_name', models.CharField(max_length=50, null=True, blank=True)),
                ('block_name', models.CharField(max_length=50, null=True, blank=True)),
                ('is_fibre_layered_upto_gp', models.BooleanField(default=False)),
                ('is_gpon_installed_at_block', models.BooleanField(default=True)),
                ('is_gpon_termination_done_at_GP', models.BooleanField(default=True)),
                ('nofn_pop_build_at', models.CharField(max_length=4, choices=[(b'GP', b'GP'), (b'Block', b'Block')])),
                ('is_network_access_available_at_village', models.BooleanField(default=True)),
                ('remarks', models.CharField(max_length=100, null=True, blank=True)),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appl_nm', models.CharField(max_length=15, choices=[(b'Dharitree', b'Dharitree'), (b'ePanjeeyan', b'ePanjeeyan'), (b'eSetu', b'eSetu'), (b'CCTNS', b'CCTNS'), (b'Vahan', b'Vahan')])),
                ('appl_owner', models.CharField(max_length=30)),
                ('appl_objective', models.CharField(max_length=100)),
                ('stakeholder_details', models.CharField(max_length=100)),
                ('date_of_commisioning', models.CharField(max_length=12)),
                ('name_of_application_developer', models.CharField(max_length=60)),
                ('appl_platform_details', models.CharField(max_length=60)),
                ('future_roadmap', models.CharField(max_length=100)),
                ('support_requirements', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SWANReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pop_names', models.CharField(max_length=50, null=True, blank=True)),
                ('distance_from_hq', models.CharField(max_length=10, null=True, blank=True)),
                ('offices_connected_with_pop', models.CharField(max_length=100, null=True, blank=True)),
                ('distance_from_pop', models.CharField(max_length=100, null=True, blank=True)),
                ('connectivity_types', models.CharField(max_length=4, choices=[(b'UTP', b'UTP'), (b'WiFi', b'WiFi'), (b'OFC', b'Optical Fibre')])),
                ('internet_bandwidth', models.CharField(max_length=50, null=True, blank=True)),
                ('is_functional', models.BooleanField(default=False)),
                ('when_last_up', models.CharField(max_length=15, null=True, blank=True)),
                ('pop_manpower', models.CharField(max_length=50, null=True, blank=True)),
                ('reasons_for_not_working', models.CharField(default=b'NA', max_length=50, null=True, blank=True)),
                ('remarks', models.CharField(max_length=100, null=True, blank=True)),
                ('district', models.CharField(max_length=30, choices=[(b'BK', b'Baksa'), (b'BP', b'Barpeta'), (b'BS', b'Biswanath'), (b'BO', b'Bongaigaon'), (b'CA', b'Cachar'), (b'CD', b'Charaideo'), (b'CH', b'Chirang'), (b'DR', b'Darrang'), (b'DM', b'Dhemaji'), (b'DU', b'Dhubri'), (b'DI', b'Dibrugarh'), (b'GP', b'Goalpara'), (b'GG', b'Golaghat'), (b'HA', b'Hailakandi'), (b'HJ', b'Hojai'), (b'JO', b'Jorhat'), (b'KM', b'Kamrup Metropolitan'), (b'KU', b'Kamrup'), (b'KG', b'Karbi Anglong'), (b'KR', b'Karimganj'), (b'KJ', b'Kokrajhar'), (b'LA', b'Lakhimpur'), (b'MJ', b'Majuli'), (b'MA', b'Morigaon'), (b'NN', b'Nagaon'), (b'NB', b'Nalbari'), (b'NC', b'Dima Hasao'), (b'SV', b'Sivasagar'), (b'ST', b'Sonitpur'), (b'SM', b'South Salmara-Mankachar'), (b'TI', b'Tinsukia'), (b'UD', b'Udalguri'), (b'WK', b'West Karbi Anglong')])),
                ('updated_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='swanreport',
            unique_together=set([('pop_names', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='softwarereport',
            unique_together=set([('appl_nm', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='nofnreport',
            unique_together=set([('gp_name', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='manpowerreport',
            unique_together=set([('person_name', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='hardwarereport',
            unique_together=set([('hardware_nm', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='digitalliteracyreport',
            unique_together=set([('lac_name', 'updated_date', 'district')]),
        ),
        migrations.AlterUniqueTogether(
            name='cscreport',
            unique_together=set([('omt_id', 'updated_date', 'district')]),
        ),
    ]
