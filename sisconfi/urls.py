from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pagina_inicial.views.PaginaInicial', name='home'),
    url(r'^novidades$', 'pagina_inicial.views.Novidades', name='novidades'),
	#url(r'calculos^$', 'calcsalarios.views.homeCalculos', name='home'),
	url(r'^calculos-folha-pagamento/', include('folhapagto.urls')),
	url(r'^calculos-rescisao/', include('rescisao.urls')),
	url(r'^calculos-ferias/', include('ferias.urls')),
	url(r'^calculos-decimo-terceiro/', include('decimoterceiro.urls')),
	url(r'^calculos-seguro-desemprego/', include('calculossegdesemp.urls')),
	url(r'^calculos-fgts/', include('calculosfgts.urls')),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
