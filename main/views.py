from django.shortcuts import get_object_or_404, redirect, render

from .models import BlogPost, Project, Service


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
