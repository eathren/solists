from django.contrib.sitemaps import Sitemap
from .models import Lead

class LeadSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
            return Lead.objects.filter(status=1)

    def lastmod(self, obj):
            return obj.updated_at