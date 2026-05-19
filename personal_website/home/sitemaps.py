from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from home import models


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return ['home-home', 'home-resume', 'home-projects']

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return models.Project.objects.all()

    def location(self, obj):
        return reverse('home-individual-project', kwargs={'slug': obj.slug})
