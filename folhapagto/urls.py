from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'folhapagto.views.index',  name='homeFolhaPagamento'), 
    #url(r'^calculos$', 'calcsalarios.views.home2', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
