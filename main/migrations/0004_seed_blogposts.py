from django.db import migrations


def seed_blog_posts(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')

    posts = [
        {
            'title': 'Top Mistakes to Avoid During Home Renovation',
            'slug': 'top-mistakes-to-avoid-during-home-renovation',
            'image': 'assets/img/blog/blog-3.jpg',
            'author': 'Shelta Cost Editorial',
            'published_label': '13, March 2025',
            'excerpt': 'Poor planning, weak cost controls and late design decisions can turn a renovation into an avoidable budget problem.',
            'intro': 'Renovation projects often go wrong because early assumptions are not tested against real cost, scope and delivery conditions. Once works start, those weak assumptions become expensive variations, programme slips and procurement stress.',
            'body': 'Clients can avoid many renovation problems by defining scope early, checking cost exposure before procurement and using disciplined contract administration during implementation. Strong reporting and measured change control reduce the risk of surprises once site activity is underway.',
            'quote': 'Clear planning and disciplined reporting are usually the difference between a manageable renovation and a chaotic one.',
            'quote_author': 'Shelta Cost Editorial',
            'section_heading': 'Why Early Coordination Matters',
            'section_body': 'Better planning, better documentation and better reporting improve procurement outcomes and site delivery. These are the same principles Shelta Cost applies in quantity surveying, contract administration and project monitoring.',
            'sort_order': 1,
            'featured': True,
        },
        {
            'title': 'How to Choose the Perfect Construction Company',
            'slug': 'how-to-choose-the-perfect-construction-company',
            'image': 'assets/img/blog/blog-2.jpg',
            'author': 'Shelta Cost Editorial',
            'published_label': '09, March 2025',
            'excerpt': 'The right delivery partner is not just about price. It is about capability, reporting discipline and proven sector experience.',
            'intro': 'Choosing a construction company or consultancy partner should begin with evidence of capability in projects similar to yours. Price matters, but it should sit alongside programme reliability, reporting clarity, contract discipline and sector-specific experience.',
            'body': 'A strong partner will show how they manage cost, time and quality together rather than treating them as separate problems. Clients should look for teams that can explain procurement strategy, change control, risk reporting and stakeholder communication in practical terms.',
            'quote': 'The best partner is rarely the one with the lowest number. It is the one with the clearest delivery discipline.',
            'quote_author': 'Shelta Cost Editorial',
            'section_heading': 'What Clients Should Look For',
            'section_body': 'Relevant experience, dependable cost management, timely reporting and disciplined contract administration are the foundations of better project outcomes. Without those, even a strong design intent can drift off course.',
            'sort_order': 2,
            'featured': True,
        },
        {
            'title': 'How Weather Can Impact a Construction Project',
            'slug': 'how-weather-can-impact-a-construction-project',
            'image': 'assets/img/blog/blog-1.jpg',
            'author': 'Shelta Cost Editorial',
            'published_label': '31, December 2025',
            'excerpt': 'Rainfall, site conditions and seasonal patterns can affect programme, safety and material performance more than many clients expect.',
            'intro': 'Weather is one of the most underestimated project risks. Rainfall, wind and prolonged wet conditions can affect excavation, concrete works, roofing, logistics and overall programme performance.',
            'body': 'Projects that account for weather early are better positioned to manage site productivity, safety and material protection. Procurement sequencing, realistic programme allowances and strong reporting help teams respond without losing control of cost and time outcomes.',
            'quote': 'Weather should never be treated as a surprise risk on a live site. It needs to be priced, planned and monitored.',
            'quote_author': 'Shelta Cost Editorial',
            'section_heading': 'Why Programme Risk Needs Realistic Allowances',
            'section_body': 'A realistic programme is not just a scheduling document. It is a commercial control tool. When weather disruption is ignored, clients often feel the impact later through claims, extension requests and avoidable cost movement.',
            'sort_order': 3,
            'featured': False,
        },
    ]

    for post in posts:
        BlogPost.objects.update_or_create(slug=post['slug'], defaults=post)


def unseed_blog_posts(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    BlogPost.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_blogpost'),
    ]

    operations = [
        migrations.RunPython(seed_blog_posts, unseed_blog_posts),
    ]
