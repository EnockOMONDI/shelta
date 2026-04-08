from django.db import migrations


def seed_company_profile(apps, schema_editor):
    CompanyProfile = apps.get_model('main', 'CompanyProfile')
    if CompanyProfile.objects.exists():
        return

    CompanyProfile.objects.create(
        title='Shelta Cost Solutions Profile 2024',
        download_url='https://example.com/secure/company-profile.pdf',
        uploadcare_file_id='',
        is_active=True,
    )


def reverse_seed_company_profile(apps, schema_editor):
    CompanyProfile = apps.get_model('main', 'CompanyProfile')
    CompanyProfile.objects.filter(title='Shelta Cost Solutions Profile 2024').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_companyprofile_profiledownloadlead'),
    ]

    operations = [
        migrations.RunPython(seed_company_profile, reverse_seed_company_profile),
    ]
