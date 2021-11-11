# Generated by Django 3.1.4 on 2021-06-23 16:40

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_revision.revision_field
import edc_base.model_fields.custom_fields
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.model_validators.date
import edc_base.sites.managers
import edc_base.utils
import edc_protocol.validators
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalDeathReport',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('subject_identifier', models.CharField(max_length=50)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Death Report',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalChildOffStudy',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(db_index=True, max_length=50, verbose_name='Subject Identifier')),
                ('offschedule_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Date and time subject taken off schedule')),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('offstudy_date', models.DateField(validators=[edc_protocol.validators.date_not_before_study_start, edc_base.model_validators.date.date_not_future], verbose_name='Off-study Date')),
                ('reason_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If Other, specify ...')),
                ('comment', models.TextField(blank=True, max_length=250, null=True, verbose_name='Comment')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.", validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date')),
                ('reason', models.CharField(choices=[('moving', 'Participant stated she will be moving out of the study area or unable to stay in study area'), ('ltfu', 'Participant lost to follow-up/ unable to locate'), ('lost_no_contact', 'Participant lost to follow-up, contacted but did not come to study clinic'), ('child_withdrew', 'Child/Adolescent changed mind and withdrew consent'), ('withdrew_by_father', 'Father of the infant/child/adolescent refused to participate and therefore participant withdrew consent'), ('withdrew_by_family', 'Other family member refused the study and therefore participant withdrew consent '), ('hiv_pos', 'Infant/child/adolescent found to be HIV-infected'), ('death', 'Infant/child/adolescent Death (complete the Infant Death Report Form)'), ('complete', ' Completion of protocol required period of time for observation (see Study Protocol for definition of Completion.) [skip to end of form]'), ('incarcerated', 'Adolescent is incarcerated'), ('OTHER', ' Other')], max_length=115, verbose_name='Please code the primary reason the participant is being taken off the study')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Child Off-Study',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCaregiverOffStudy',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(db_index=True, max_length=50, verbose_name='Subject Identifier')),
                ('offschedule_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Date and time subject taken off schedule')),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('offstudy_date', models.DateField(validators=[edc_protocol.validators.date_not_before_study_start, edc_base.model_validators.date.date_not_future], verbose_name='Off-study Date')),
                ('reason_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If Other, specify ...')),
                ('comment', models.TextField(blank=True, max_length=250, null=True, verbose_name='Comment')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.", validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date')),
                ('reason', models.CharField(choices=[('multiple_vialble_gestations', 'Multiple (2 or more) viable gestations seen on ultrasound'), ('unable_to_determine_ga', 'Unable to confirm GA by Ultrasound.'), ('miscarriage_or_arbotion', 'Miscarriage or abortion'), ('fetal_death_gt_20wks', 'fetal Death at >= 20weeks GA (IUFD) or still born'), ('took_art_less_than_4weeks', 'Biological mother took ART for less than 4 weeks during pregnancy'), ('caregiver_death', 'Caregiver death (complete the Death Report Form AF005)'), ('moving_out_of_study_area', 'Participant stated that they will be moving out of the study area or unable to stay in study area'), ('loss_to_followup', 'Participant lost to follow-up/unable to locate'), ('loss_to_followup_contacted', 'Participant lost to follow-up, contacted but did not come to study clinic'), ('caregiver_withdrew_consent', 'Caregiver changed mind and withdrew consent'), ('father_refused', 'Father of the infant/child/adolescent refused to participate and therefore participant withdrew consent '), ('family_member_refused', 'Other family member refused the study and therefore participant withdrew consent'), ('caregiver_hiv_infected', 'Caregiver was found to be HIV-infected and the date of infection cannot be determined prior to the birth of their child'), ('infant_hiv_infected', 'Infant/Child/Adolescent found to be HIV-infected'), ('infant_death', 'Infant/Child/Adolescent death (complete Infant Death Report Form)'), ('protocol_completion', 'Completion of protocol required period of time for observation (see Study Protocol for definition of "Completion") (skip to end of form)'), ('enrolled_erroneously', 'Enrolled erroneously – did not meet eligibility criteria'), ('incarcerated', 'Participant is incarcerated'), ('OTHER', 'Other')], max_length=115, verbose_name='Please code the primary reason participant taken off-study')),
                ('offstudy_point', models.CharField(blank=True, choices=[('prior_to_del', 'Prior to Delivery'), ('post_del', 'Post Delivery')], help_text='For pregnant women enrolled in Cohort A', max_length=50, null=True, verbose_name='At what point did the mother go off study')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Caregiver Off Study',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='DeathReport',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('slug', models.CharField(db_index=True, default='', editable=False, help_text='a field used for quick search', max_length=250, null=True)),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('subject_identifier', models.CharField(max_length=50)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'Death Report',
            },
        ),
        migrations.CreateModel(
            name='ChildOffStudy',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, unique=True, verbose_name='Subject Identifier')),
                ('offschedule_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Date and time subject taken off schedule')),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('offstudy_date', models.DateField(validators=[edc_protocol.validators.date_not_before_study_start, edc_base.model_validators.date.date_not_future], verbose_name='Off-study Date')),
                ('reason_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If Other, specify ...')),
                ('comment', models.TextField(blank=True, max_length=250, null=True, verbose_name='Comment')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.", validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date')),
                ('reason', models.CharField(choices=[('moving', 'Participant stated she will be moving out of the study area or unable to stay in study area'), ('ltfu', 'Participant lost to follow-up/ unable to locate'), ('lost_no_contact', 'Participant lost to follow-up, contacted but did not come to study clinic'), ('child_withdrew', 'Child/Adolescent changed mind and withdrew consent'), ('withdrew_by_father', 'Father of the infant/child/adolescent refused to participate and therefore participant withdrew consent'), ('withdrew_by_family', 'Other family member refused the study and therefore participant withdrew consent '), ('hiv_pos', 'Infant/child/adolescent found to be HIV-infected'), ('death', 'Infant/child/adolescent Death (complete the Infant Death Report Form)'), ('complete', ' Completion of protocol required period of time for observation (see Study Protocol for definition of Completion.) [skip to end of form]'), ('incarcerated', 'Adolescent is incarcerated'), ('OTHER', ' Other')], max_length=115, verbose_name='Please code the primary reason the participant is being taken off the study')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'Child Off-Study',
                'verbose_name_plural': 'Child Off-Study',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='CaregiverOffStudy',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, unique=True, verbose_name='Subject Identifier')),
                ('offschedule_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Date and time subject taken off schedule')),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('offstudy_date', models.DateField(validators=[edc_protocol.validators.date_not_before_study_start, edc_base.model_validators.date.date_not_future], verbose_name='Off-study Date')),
                ('reason_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If Other, specify ...')),
                ('comment', models.TextField(blank=True, max_length=250, null=True, verbose_name='Comment')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.", validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date')),
                ('reason', models.CharField(choices=[('multiple_vialble_gestations', 'Multiple (2 or more) viable gestations seen on ultrasound'), ('unable_to_determine_ga', 'Unable to confirm GA by Ultrasound.'), ('miscarriage_or_arbotion', 'Miscarriage or abortion'), ('fetal_death_gt_20wks', 'fetal Death at >= 20weeks GA (IUFD) or still born'), ('took_art_less_than_4weeks', 'Biological mother took ART for less than 4 weeks during pregnancy'), ('caregiver_death', 'Caregiver death (complete the Death Report Form AF005)'), ('moving_out_of_study_area', 'Participant stated that they will be moving out of the study area or unable to stay in study area'), ('loss_to_followup', 'Participant lost to follow-up/unable to locate'), ('loss_to_followup_contacted', 'Participant lost to follow-up, contacted but did not come to study clinic'), ('caregiver_withdrew_consent', 'Caregiver changed mind and withdrew consent'), ('father_refused', 'Father of the infant/child/adolescent refused to participate and therefore participant withdrew consent '), ('family_member_refused', 'Other family member refused the study and therefore participant withdrew consent'), ('caregiver_hiv_infected', 'Caregiver was found to be HIV-infected and the date of infection cannot be determined prior to the birth of their child'), ('infant_hiv_infected', 'Infant/Child/Adolescent found to be HIV-infected'), ('infant_death', 'Infant/Child/Adolescent death (complete Infant Death Report Form)'), ('protocol_completion', 'Completion of protocol required period of time for observation (see Study Protocol for definition of "Completion") (skip to end of form)'), ('enrolled_erroneously', 'Enrolled erroneously – did not meet eligibility criteria'), ('incarcerated', 'Participant is incarcerated'), ('OTHER', 'Other')], max_length=115, verbose_name='Please code the primary reason participant taken off-study')),
                ('offstudy_point', models.CharField(blank=True, choices=[('prior_to_del', 'Prior to Delivery'), ('post_del', 'Post Delivery')], help_text='For pregnant women enrolled in Cohort A', max_length=50, null=True, verbose_name='At what point did the mother go off study')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'Caregiver Off Study',
                'verbose_name_plural': 'Caregiver Off Study',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]