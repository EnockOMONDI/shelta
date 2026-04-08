from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_seed_initial_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.CharField(max_length=255)),
                ('author', models.CharField(default='Shelta Cost Editorial', max_length=120)),
                ('published_label', models.CharField(max_length=120)),
                ('excerpt', models.TextField()),
                ('intro', models.TextField()),
                ('body', models.TextField()),
                ('quote', models.TextField(blank=True)),
                ('quote_author', models.CharField(blank=True, max_length=120)),
                ('section_heading', models.CharField(blank=True, max_length=200)),
                ('section_body', models.TextField(blank=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={'ordering': ['sort_order', 'title']},
        ),
    ]
