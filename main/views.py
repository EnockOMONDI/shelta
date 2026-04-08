from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils import timezone

from .forms import CompanyProfileRequestForm
from .models import BlogPost, CompanyProfile, ProfileDownloadLead, Project, Service


def home(request):
    context = {
        'featured_services': Service.objects.filter(featured=True)[:4],
        'featured_projects': Project.objects.filter(featured=True)[:4],
    }
    return render(request, 'index-6.html', context)


def about(request):
    return render(request, 'about.html')


def history(request):
    return render(request, 'history.html')


def services(request):
    return render(request, 'services.html', {'services': Service.objects.all()})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    context = {
        'service': service,
        'services': Service.objects.all(),
    }
    return render(request, 'services-details.html', context)


def legacy_service_detail(request):
    first_service = Service.objects.order_by('sort_order', 'title').first()
    if not first_service:
        return redirect('services')
    return redirect('service_detail', slug=first_service.slug)


def portfolio(request):
    return render(request, 'gallery.html', {'projects': Project.objects.all()})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
        'projects': Project.objects.all()[:6],
    }
    return render(request, 'portfolio-details.html', context)


def legacy_project_detail(request):
    featured_project = Project.objects.filter(featured=True).order_by('sort_order', 'title').first()
    if not featured_project:
        featured_project = Project.objects.order_by('sort_order', 'title').first()
    if not featured_project:
        return redirect('portfolio')
    return redirect('project_detail', slug=featured_project.slug)


def contact(request):
    return render(request, 'contact.html')


def request_quote(request):
    return render(request, 'request-quote.html')


def company_profile(request):
    profile = CompanyProfile.objects.filter(is_active=True).first() or CompanyProfile.objects.first()
    form = CompanyProfileRequestForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        lead = ProfileDownloadLead.objects.create(
            email=form.cleaned_data['email'],
            source='company-profile-page',
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:1000],
        )

        download_url = profile.download_url if profile else 'https://example.com/secure/company-profile.pdf'
        email_sent = send_company_profile_email(lead.email, download_url)
        if email_sent:
            lead.sent_at = timezone.now()
            lead.save(update_fields=['sent_at'])

        request.session['company_profile_success'] = {
            'email': lead.email,
            'download_url': download_url,
            'email_sent': email_sent,
        }
        return redirect('company_profile_success')

    return render(
        request,
        'company-profile.html',
        {
            'form': form,
            'profile': profile,
        },
    )


def company_profile_success(request):
    payload = request.session.pop('company_profile_success', None)
    if not payload:
        return redirect('company_profile')
    return render(request, 'company-profile-success.html', payload)


def blog_standard(request):
    posts = BlogPost.objects.all()
    recent_posts = BlogPost.objects.all()[:3]
    return render(request, 'blog-standard.html', {'posts': posts, 'recent_posts': recent_posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    recent_posts = BlogPost.objects.exclude(pk=post.pk)[:3]
    return render(request, 'blog-details.html', {'post': post, 'recent_posts': recent_posts})


def legacy_blog_detail(request):
    first_post = BlogPost.objects.order_by('sort_order', 'title').first()
    if not first_post:
        return redirect('blog_standard')
    return redirect('blog_detail', slug=first_post.slug)


def static_page(request, template_name):
    return render(request, template_name)


def get_client_ip(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        return forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


def send_company_profile_email(email, download_url):
    if settings.EMAIL_BACKEND == 'django.core.mail.backends.console.EmailBackend':
        return False

    if not settings.EMAIL_HOST or not settings.DEFAULT_FROM_EMAIL:
        return False

    subject = 'Your Shelta Cost Company Profile'
    text_message = (
        'Shelta Cost Solutions Ltd\n\n'
        'Thank you for requesting our company profile.\n\n'
        f'Access the profile here:\n{download_url}\n\n'
        'If you need commercial, project or cost advisory support, our team will be glad to assist.\n\n'
        'Shelta Cost Solutions Ltd'
    )
    html_message = render_to_string(
        'emails/company-profile-email.html',
        {
            'download_url': download_url,
        },
    )

    try:
        message = EmailMultiAlternatives(
            subject,
            text_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
        )
        message.attach_alternative(html_message, 'text/html')
        message.send(fail_silently=False)
        return True
    except Exception:
        return False
