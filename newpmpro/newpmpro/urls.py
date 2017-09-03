"""newpmpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from newpmpro.view import home_page, new_project_idea_page, search_project_page

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'new-project-idea', new_project_idea_page, name='new-project-idea'),
    url(r'articles/', include('articleManagement.urls'), name='articles-page'),
    # url(r'search-project', search_project_page, name='search-projects'),
    url(r'account/api/', include('userManagement.api_urls')),
    url(r'api/project/', include('searchProjectManagement.api_urls')),
    url(r'api/idea/', include('newProjectIdeaManagement.api_urls')),
    url(r'api/article', include('articleManagement.api_urls')),
    url(r'', home_page, name='home-page'),
]
