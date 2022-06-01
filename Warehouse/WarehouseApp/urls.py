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
    path('suppliers/addSupllier/', views.addSupplier, name='addSupplier'),
    path('suppliers/delSupllier/', views.delSupplier, name='delSupplier'),
    path('suppliers/supplier_<int:supplier_id>/', views.supplierDetail, name='supplierDetail'),
    path('suppliers/supplier_<int:supplier_id>/supgood_<int:supplyGood_id>/', views.supplyGoodDetail, name='supplyGoodDetail'),

    path('supplyForm/', views.supplyForm, name='supplyForm'),
    path('supplyForm/addSupply/', views.addSupply, name='addSupply'),
    path('supplies/', views.supplies, name='supplies'),
    path('supplies/delSupply/', views.delSupply, name='delSupply'),
    path('supplies/supply_<int:supply_id>/', views.supplyDetail, name='supplyDetail'),

    path('reportForm/', views.reportForm, name='reportForm'),
    path('reportForm/addReport/', views.addReport, name='addReport'),
    path('reports/', views.reports, name='reports'),
    path('reports/report_<int:report_id>/', views.reportDetail, name='reportDetail'),
    path('reports/delReport/', views.delReport, name='delReport'),

    path('loadingForm/', views.loadingForm, name='loadingForm'),
    path('loadingForm/addLoading/', views.addLoading, name='addLoading'),
    path('loadings/', views.loadings, name='loadings'),
    path('loading/loading_<int:loading_id>/', views.loadingDetail, name='loadingDetail'),

    path('units/', views.units, name='units'),
    path('units/addUnit/', views.addUnit, name='addUnit'),
    path('units/delUnit/', views.delUnit, name='delUnit'),
    path('units/editUnit/', views.editUnit, name='editUnit'),

    path('sectionTypes/', views.sectionTypes, name='sectionTypes'),
    path('sectionTypes/addSectionType/', views.addSectionType, name='addSectionType'),
    path('sectionTypes/delSectionType/', views.delSectionType, name='delSectionType'),
    path('sectionTypes/editSectionType/', views.editSectionType, name='editSectionType'),

    path('cellStatus/', views.cellStatus, name='cellStatus'),
    path('cellStatus/addCellStatus/', views.addCellStatus, name='addCellStatus'),
    path('cellStatus/delCellStatus/', views.delCellStatus, name='delCellStatus'),
    path('cellStatus/editCellStatus/', views.editCellStatus, name='editCellStatus'),

    path('goodGroups/', views.goodGroups, name='goodGroups'),
    path('goodGroups/addGoodGroups/', views.addGoodGroup, name='addGoodGroup'),
    path('goodGroups/delGoodGroups/', views.delGoodGroup, name='delGoodGroup'),
    path('goodGroups/editGoodGroups/', views.editGoodGroup, name='editGoodGroup'),

    path('positions/', views.positions, name='positions'),
    path('positions/addPosition/', views.addPosition, name='addPosition'),
    path('positions/delPosition/', views.delPosition, name='delPosition'),
    path('positions/editPosition/', views.editPosition, name='editPosition'),

    path('categories/', views.categories, name='categories'),
    path('categories/addCategory/', views.addCategory, name='addCategory'),
    path('categories/delCategory/', views.delCategory, name='delCategory'),
    path('categories/editCategory/', views.editCategory, name='editCategory'),

    path('subcategories/', views.subcategories, name='subcategories'),
    path('subcategories/addSubcategory/', views.addSubcategory, name='addSubcategory'),
    path('subcategories/delSubcategory/', views.delSubcategory, name='delSubcategory'),
    path('subcategories/editSubcategory/', views.editSubcategory, name='editSubcategory'),

    path('emps/', views.emps, name='emps'),
    path('emps/emp_<int:emp_id>/', views.empDetail, name='empDetail'),
    path('emps/addEmp/', views.addEmp, name='addEmp'),
    path('emps/delEmp/', views.delEmp, name='delEmp'),
    path('emps/editEmp/', views.editEmp, name='editEmp'),

    path('goods/', views.goods, name='goods'),
    path('goods/addGood/', views.addGood, name='addGood'),
    path('goods/delGood/', views.delGood, name='delGood'),
    path('goods/editGood/', views.editGood, name='editGood'),

    path('receipts/', views.receipts, name='receipts'),
    path('receipts/receipt_<int:receipt_id>/', views.receiptDetail, name='receiptDetail'),
    path('receipts/addReceip/', views.addReceip, name='addReceip'),
    path('receipts/delReceip/', views.delReceip, name='delReceip'),
    path('receipts/editReceip/', views.editReceip, name='editReceip'),

    path('expenditures/', views.expenditures, name='expenditures'),
    path('expenditures/expenditure_<int:expenditure_id>/', views.expenditureDetail, name='expenditureDetail'),
    path('expenditures/addExpenditure/', views.addExpenditure, name='addExpenditure'),
    path('expenditures/delExpenditure/', views.delExpenditure, name='delExpenditure'),
    path('expenditures/editExpenditure/', views.editExpenditure, name='editExpenditure'),

    path('goodMovings/', views.goodMovings, name='goodMovings'),
    path('goodMovings/addGoodMoving/', views.addGoodMoving, name='addGoodMoving'),
    path('goodMovings/delGoodMoving/', views.delGoodMoving, name='delGoodMoving')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)