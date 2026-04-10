from django.conf import settings
from django.db import models


def asset_url(path):
    if not path:
        return ''
    if path.startswith(('http://', 'https://', '/')):
        return path
    normalized_path = path.removeprefix('assets/').lstrip('/')
    return f'{settings.STATIC_URL.rstrip("/")}/{normalized_path}'


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

    @property
    def image_url(self):
        return asset_url(self.image)

    @property
    def gallery_image_left_url(self):
        return asset_url(self.gallery_image_left)

    @property
    def gallery_image_right_url(self):
        return asset_url(self.gallery_image_right)


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


class CompanyProfile(models.Model):
    title = models.CharField(max_length=200, default='Shelta Cost Company Profile')
    download_url = models.URLField(
        default='https://example.com/secure/company-profile.pdf',
        help_text='Temporary secure download URL. Replace later with the Uploadcare-backed file URL.',
    )
    uploadcare_file_id = models.CharField(
        max_length=255,
        blank=True,
        help_text='Optional Uploadcare file UUID or CDN reference.',
    )
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_active', '-updated_at', '-created_at']

    def __str__(self):
        return self.title


class ProfileDownloadLead(models.Model):
    email = models.EmailField()
    source = models.CharField(max_length=120, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email
