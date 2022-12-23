from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    
    path('',views.index, name='index'),
    path('dashboard/',views.dashboard, name='dashboard'),


    path('about/',views.create_about, name='about'),
    path('edit-about/',views.edit_about, name='edit-about'),
    path('delete-about/<str:id>',views.delete_about, name='delete-about'),

    path('testmony/',views.create_testmony, name='testmony'),
    path('edit-testmony/<str:id>',views.edit_testmony, name='edit-testmony'),
    path('delete-testmony/<str:id>',views.delete_testmony, name='delete-testmony'),
    
    path('service/',views.create_service, name='service'),
    path('edit-service/<str:id>',views.edit_service, name='edit-service'),
    path('delete-service/<str:id>',views.delete_service, name='delete-service'),

    path('settings/',views.create_settings, name='settings'),
    path('edit-settings/',views.edit_settings, name='edit-settings'),
    path('delete-settings/<str:id>',views.delete_settings, name='delete-settings'),

    path('team/',views.create_team, name='team'),
    path('edit-team/<str:id>',views.edit_team, name='edit-team'),
    path('delete-team/<str:id>',views.delete_team, name='delete-team'),

    path('order/',views.list_order, name='order'),
    path('create-order/',views.create_order, name='create-order'),
    path('confirm-order/<str:id>',views.confirm_order, name='confirm_order'),
    path('complete-order/<str:id>',views.complete_order, name='complete_order'),
    path('cancel-order/<str:id>',views.cancel_order, name='cancel_order'),
    path('view-order/<str:id>',views.view_order, name='view_order_details'),


    path('hero/',views.create_hero, name='hero'),
    path('edit-hero/',views.edit_hero, name='edit-hero'),
    path('delete-hero/<str:id>',views.delete_hero, name='delete-hero'),
    path('edit-hero-image/<str:id>',views.edit_hero_image, name='edit_image'),

    path('social-links/',views.create_link, name='social'),
    path('edit-social-links/<str:id>',views.edit_link, name='edit-social'),
    path('delete-social-links/<str:id>',views.delete_link, name='delete-social'),


    path('aboutus/',views.get_about, name='aboutus'),
    path('product/',views.get_product, name='product'),
    path('our-services/',views.get_service, name='services'),
   

]