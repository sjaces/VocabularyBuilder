from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'vocabularyBuilder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^lista/', 'app.views.lista', name='lista'),

    url(r'^admin/', include(admin.site.urls)),
)
