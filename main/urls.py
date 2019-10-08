from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# MAIN ########################################
    url(r'^$', views.home_view, name='home_view'),
    url(r'^send_email$', views.send_email, name='send_email'),
    url(r'^about/$', views.about_view, name='about_view'),
    url(r'^categories/$', views.projects_view, name='projects_view'),
    url(r'^studio/$', views.studio_view, name='studio_view'),
    url(r'^contact/$', views.contact_view, name='contact_view'),
    ############################# /MAIN #######################################

    ############################# SPECIFIC ########################################
    url(r'^projects/$', views.projects_list_view, name='projects_list_view'),
    ############################# /SPECIFIC ########################################

    ############################# AUTH #################################
    # url(r'^login/$', views.login_post, name='login_post'),
    # url(r'^logout/$', views.logout_get, name='logout_get'),
    # url(r'^register/$', views.register_pg, name='register_pg'),
    ############################# /AUTH ################################
]
