from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from newpmpro.models import PmUser, ProjectIdeas, UserSources, PartnerDetails, ProjectData, ProjectRequests, Article, \
    Categories, Tags, HyperLinks

# admin.site.register(PmUser)
admin.site.register(ProjectIdeas)
admin.site.register(UserSources)
# admin.site.register(ProjectCommonInfo)
admin.site.register(PartnerDetails)
admin.site.register(ProjectData)
admin.site.register(ProjectRequests)
admin.site.register(Article)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(HyperLinks)


