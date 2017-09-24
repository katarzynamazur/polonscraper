from django.conf.urls import include, url
from django.contrib import admin
from polonwebapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', views.logout_page, name="logout"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),   
    url(r'^register/$', views.register, name="register"),
    url(r'^register/success/$', views.register_success, name="register_success"),

    url(r'^db/scopus_hindex_all/$', views.scopus_hindex_all, name="scopus_hindex_all"),
    url(r'^db/scopus_hindex_dr/$', views.scopus_hindex_dr, name="scopus_hindex_dr"),
    url(r'^db/scopus_hindex_drhab/$', views.scopus_hindex_drhab, name="scopus_hindex_drhab"),

    url(r'^db/scopus_num_of_pubs_all/$', views.scopus_num_of_pubs_all, name="scopus_num_of_pubs_all"),
    url(r'^db/scopus_num_of_pubs_dr/$', views.scopus_num_of_pubs_dr, name="scopus_num_of_pubs_dr"),
    url(r'^db/scopus_num_of_pubs_drhab/$', views.scopus_num_of_pubs_drhab, name="scopus_num_of_pubs_drhab"),

    url(r'^db/google_scholar_citations_all/$', views.google_scholar_citations_all, name="google_scholar_citations_all"),
    url(r'^db/google_scholar_citations_dr/$', views.google_scholar_citations_dr, name="google_scholar_citations_dr"),
    url(r'^db/google_scholar_citations_drhab/$', views.google_scholar_citations_drhab, name="google_scholar_citations_drhab"),

    url(r'^db/google_scholar_hindex_all/$', views.google_scholar_hindex_all, name="google_scholar_hindex_all"),
    url(r'^db/google_scholar_hindex_dr/$', views.google_scholar_hindex_dr, name="google_scholar_hindex_dr"),
    url(r'^db/google_scholar_hindex_drhab/$', views.google_scholar_hindex_drhab, name="google_scholar_hindex_drhab"),

    url(r'^db/dblp_num_of_pubs_all/$', views.dblp_num_of_pubs_all, name="dblp_num_of_pubs_all"),
    url(r'^db/dblp_num_of_pubs_dr/$', views.dblp_num_of_pubs_dr, name="dblp_num_of_pubs_dr"),
    url(r'^db/dblp_num_of_pubs_drhab/$', views.dblp_num_of_pubs_drhab, name="dblp_num_of_pubs_drhab"),

    url(r'^homeit/$', views.homeit, name="homeit"),
]


