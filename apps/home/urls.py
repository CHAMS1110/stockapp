from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),
    path('', views.index, name="index"),
    path('stocks/<str:tid>', views.chart, name="ticker"),
    #path('histo', views.histo_ticker, name="histo"),
    path('stocks/', views.test, name="test"),
    #path('chart/', views.chart, name="chart"),
    path('trans/', views.page_trans, name="trans"),
 ]
