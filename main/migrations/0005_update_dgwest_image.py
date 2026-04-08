from django.db import migrations


def update_dgwest_image(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(
        slug='dg-west-serviced-apartments-westlands'
    ).update(
        image='assets/img/portfolio/dgwest.jpeg',
        gallery_image_right='assets/img/portfolio/dgwest.jpeg',
    )


def revert_dgwest_image(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(
        slug='dg-west-serviced-apartments-westlands'
    ).update(
        image='assets/img/portfolio/portfolio-1.jpg',
        gallery_image_right='assets/img/portfolio/portfolio-8.jpg',
    )


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0004_seed_blogposts'),
    ]

    operations = [
        migrations.RunPython(update_dgwest_image, revert_dgwest_image),
    ]
