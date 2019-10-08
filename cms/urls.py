from django.conf.urls import url, include
from django.views.generic import DetailView
from . import views


urlpatterns = [
    ############################# GENERAL ########################################
    url(r'^$', views.cms_home_view, name='cms_home_view'),
    url(r'^edithome/$', views.cms_edit_home, name='cms_edit_home'),
    url(r'^editcontact/$', views.cms_edit_contact, name='cms_edit_contact'),
    url(r'^editabout/$', views.cms_edit_about, name='cms_edit_about'),
    ############################# /GENERAL #######################################



    ############################# EDIT PAGES ########################################
    url(r'^editmain/$', views.cms_edit_main, name='cms_edit_main'),
    url(r'^editmain/upload/$', views.cms_edit_main_upload, name='cms_edit_main_upload'),
    url(r'^editcontactinfo/$', views.cms_edit_contact_post, name='cms_edit_contact_post'),
    ############################# /EDIT PAGES ########################################





    ############################# CATEGORIES and PROJECTS ########################################
    url(r'^categories/$', views.cms_categories, name='cms_categories'),
    url(r'^projects/$', views.cms_projects, name='cms_projects'),
    url(r'^projects/new/$', views.cms_projects_new, name='cms_projects_new'),
    url(r'^projects/project/$', views.cms_project, name='cms_project'),
    url(r'^projects/project/upload/$', views.cms_project_upload, name='cms_project_upload'),
    url(r'^projects/project/delete/$', views.cms_project_delete, name='cms_project_delete'),
    ############################# /CATEGORIES and PROJECTS ########################################





    ############################# STUDIO ########################################
    url(r'^studio/audio/$', views.cms_studio_audio, name='cms_studio_audio'),
    url(r'^studio/audio/get/$', views.cms_studio_audio_get, name='cms_studio_audio_get'),
    url(r'^studio/images/$', views.cms_studio_images, name='cms_studio_images'),
    url(r'^studio/images/delete/$', views.cms_si_delete, name='cms_si_delete'),
    ############################# /STUDIO ########################################





    ############################# AUTH #################################
    url(r'^login/$', views.login_vp, name='login_vp'),
    url(r'^logout/$', views.logout_g, name='logout_g'),
    # url(r'^register/$', views.register_pg, name='register_pg'),
    # url(r'^profile/$', views.profile_view, name='profile_view'),
    # url(r'^profile/edit/$', views.profile_edit_pg, name='profile_edit_pg'),
    # url(r'^user/$', views.user_view, name='user_view'),
    ############################# /AUTH ################################
]
