from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from WarehouseApp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('warehouseMap/', views.warehouseMap, name='warehouseMap'),
    path('warehouseMap/section_<int:section_id>/', views.sectionDetail, name='sectionDetail'),
    path('warehouseMap/section_<int:section_id>/good_<int:good_id>/', views.goodDetail, name='goodDetail'),
    
    path('suppliers/', views.suppliers, name='suppliers'),
    path('suppliers/supplier_<int:supplier_id>/', views.supplierDetail, name='supplierDetail'),
    path('suppliers/supplier_<int:supplier_id>/supgood_<int:supplyGood_id>/', views.supplyGoodDetail, name='supplyGoodDetail'),

    path('supplyForm/', views.supplyForm, name='supplyForm'),
    path('supplies/', views.supplies, name='supplies'),
    path('supplies/supply_<int:supply_id>/', views.supplyDetail, name='supplyDetail'),

    path('reportForm/', views.reportForm, name='reportForm'),
    path('reports/', views.reports, name='reports'),
    path('reports/report_<int:report_id>/', views.reportDetail, name='reportDetail'),

    path('loadingForm/', views.loadingForm, name='loadingForm'),
    path('loadingForm/addLoading/', views.addLoading, name='addLoading'),
    path('loadings/', views.loadings, name='loadings'),
    path('loading/loading_<int:loading_id>/', views.loadingDetail, name='loadingDetail'),

    path('units/', views.units, name='units'),

    path('sectionTypes/', views.sectionTypes, name='sectionTypes'),

    path('emps/', views.emps, name='emps'),
    path('emps/emp_<int:emp_id>/', views.empDetail, name='empDetail'),

    path('receipts/', views.receipts, name='receipts'),
    path('receipts/receipt_<int:receipt_id>/', views.receiptDetail, name='receiptDetail'),

    path('expenditures/', views.expenditures, name='expenditures'),
    path('expenditures/expenditure_<int:expenditure_id>/', views.expenditureDetail, name='expenditureDetail'),

    path('goodMovings/', views.goodMovings, name='goodMovings')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)