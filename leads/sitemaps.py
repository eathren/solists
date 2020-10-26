from django.contrib.sitemaps import Sitemap

from .models import Lead

class LeadSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def title(self):
        return Lead.objects.all().title

    def items(self):
            return Lead.objects.all()

    def lastmod(self, obj):
            return obj.updated_at