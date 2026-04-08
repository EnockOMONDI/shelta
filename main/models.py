from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    icon_class = models.CharField(max_length=100, default='flaticon-design-thinking')
    short_description = models.TextField()
    detail_heading = models.CharField(max_length=200)
    detail_intro = models.TextField()
    detail_body = models.TextField()
    detail_body_two = models.TextField()
    detail_image = models.CharField(max_length=255, blank=True)
    gallery_image_left = models.CharField(max_length=255, blank=True)
    gallery_image_right = models.CharField(max_length=255, blank=True)
    checklist = models.JSONField(default=list, blank=True)
    faq_one_question = models.CharField(max_length=255, blank=True)
    faq_one_answer = models.TextField(blank=True)
    faq_two_question = models.CharField(max_length=255, blank=True)
    faq_two_answer = models.TextField(blank=True)
    faq_three_question = models.CharField(max_length=255, blank=True)
    faq_three_answer = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['sort_order', 'title']

    def __str__(self):
        return self.title


class Project(models.Model):
    sector = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=255)
    client_type = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    summary = models.TextField()
    detail_heading = models.CharField(max_length=200)
    detail_intro = models.TextField()
    detail_body = models.TextField()
    detail_body_two = models.TextField()
    gallery_image_left = models.CharField(max_length=255, blank=True)
    gallery_image_right = models.CharField(max_length=255, blank=True)
    checklist = models.JSONField(default=list, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['sort_order', 'title']

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=255)
    author = models.CharField(max_length=120, default='Shelta Cost Editorial')
    published_label = models.CharField(max_length=120)
    excerpt = models.TextField()
    intro = models.TextField()
    body = models.TextField()
    quote = models.TextField(blank=True)
    quote_author = models.CharField(max_length=120, blank=True)
    section_heading = models.CharField(max_length=200, blank=True)
    section_body = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['sort_order', 'title']

    def __str__(self):
        return self.title
