from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'vocabularyBuilder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^lista/', 'app.views.lista', name='lista'),
    url(r'^jugar/(\d+)$', 'app.views.jugar', name='jugar'),
    url(r'^reprogramar/', 'app.views.reprogramar', name='reprogramar'),
    url(r'^nueva_palabra/(\d+)$', 'app.views.nueva_palabra', name='nueva_palabra'),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^salir/', 'app.views.salir', name='salir'),
    # url(r'^entrar/', 'app.views.entrar', name='entrar'),
    url(r'^entrar/$', 'django.contrib.auth.views.login', name="entrar"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
)
