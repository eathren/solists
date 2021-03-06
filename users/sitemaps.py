from django.contrib.sitemaps import Sitemap

from .models import CustomUser

class UserSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.3

    def items(self):
            return CustomUser.objects.all()

    # def lastmod(self, obj):
    #         return obj.updated_at