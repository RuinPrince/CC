from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("categories/",views.category,name="category"),
    path("categories/<str:tname>/act/",views.acts,name="act"),
    path("categories/<str:tname>/act/<str:act>/chapter_list/",views.chapter,name="chapter"),
    path("categories/<str:tname>/act/<str:act>/chapter_list/chapter/<int:no>/",views.section,name="section"),
    path("categories/<str:tname>/act/<str:act>/chapter_list/chapter/<int:cno>/law/<int:lno>/", views.law_detail, name="lawdetails"),
    path("quick-law/<str:act>/<str:section_id>/", views.quick_law_redirect, name="quick_law_redirect"),
    path("upload-document/", views.ocr_page_view, name="ocr"),
    path("bookmarks/", views.bookmarks_page_view, name="bookmarks"),
    path("profile/", views.profile_page_view, name="web_profile"),
    path("dashboard/", views.dashboard_page_view, name="dashboard"),
    path("admin-dashboard/", views.admin_dashboard_page_view, name="admin_dashboard"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]