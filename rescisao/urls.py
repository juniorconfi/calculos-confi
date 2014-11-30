from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'rescisao.views.index', name='homeRescisao'), #pagina 1123
    #url(r'^calculos$', 'calcsalarios.views.home2', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
