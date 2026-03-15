from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solution/', views.page_view, {'page_name': 'solution'}, name='solution'),
    path('product/', views.page_view, {'page_name': 'product'}, name='product'),
    path('scenarios/', views.page_view, {'page_name': 'scenarios'}, name='scenarios'),
    path('cases/', views.page_view, {'page_name': 'cases'}, name='cases'),
    path('cases/vnutripromyshlennaya-logistika/', views.page_view, {'page_name': 'case-vnutripromyshlennaya-logistika'}, name='case-vnutripromyshlennaya-logistika'),
    path('cases/odna-edinica-tehniki/', views.page_view, {'page_name': 'case-odna-edinica-tehniki'}, name='case-odna-edinica-tehniki'),
    path('cases/pogruzchik-priemka/', views.page_view, {'page_name': 'case-pogruzchik-priemka'}, name='case-pogruzchik-priemka'),
    path('cases/park-tehniki/', views.page_view, {'page_name': 'case-park-tehniki'}, name='case-park-tehniki'),
    path('blog/', views.page_view, {'page_name': 'blog'}, name='blog'),
    path('demo/', views.page_view, {'page_name': 'demo'}, name='demo'),
    path('faq/', views.page_view, {'page_name': 'faq'}, name='faq'),
    path('partners/', views.page_view, {'page_name': 'partners'}, name='partners'),
    path('materials/', views.page_view, {'page_name': 'materials'}, name='materials'),
    path('about/', views.page_view, {'page_name': 'about'}, name='about'),
    path('contacts/', views.page_view, {'page_name': 'contacts'}, name='contacts'),
    path('privacy/', views.page_view, {'page_name': 'privacy'}, name='privacy'),
    path('consent/', views.page_view, {'page_name': 'consent'}, name='consent'),
]
