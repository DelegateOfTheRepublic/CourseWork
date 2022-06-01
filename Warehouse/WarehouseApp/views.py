import json
import os
from django.db import models
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.defaulttags import register

from WarehouseApp.models import *

# Create your views here.

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_attribute(model, field):
    return getattr(model, field.name)

@register.filter
def get_verb_name(model, field):
    return model.get_verbose_name(field.name)

def login(request):
    return HttpResponse('<h2>Aaaa</h2>')

def warehouseMap(request):
    sections = Section.objects.all()
    return render(request, "WarehouseApp/warehouseMap/map.html", {'sections':sections})

def sectionDetail(request, section_id):
    try:
        goods = Goods.objects.filter(place__section__id = section_id)
    except:
        raise Http404('Данной секции не существует')
    return render(request, 'WarehouseApp/sections/sectionDetail.html', {'goods':goods})

def goods(request):
    goods = Goods.objects.all()
    return render(request, 'WarehouseApp/goods/goods.html', {'goods':goods})

def goodDetail(request, section_id, good_id):
    good = Goods.objects.get(id = good_id)
    abs_path = os.path.abspath(__file__).split('\\')
    del abs_path[-1]
    del abs_path[-1]
    abs_path = '\\'.join(abs_path)
    file_name = good.specs.url.split('/')[-1]
    path_to_json_specs = (abs_path + "/itemsIcons/" + good.category.name + "/" + good.subcategory.name + "/" + good.group.name + "/supplier_" + str(good.supplier.id) + "_" + good.name + "/" + file_name)
    path_to_json_specs = path_to_json_specs.replace('/', '\\')
    print(path_to_json_specs)
    with open(path_to_json_specs, 'rb') as json_data:
        good_specs = json.load(json_data)
    return render(request, 'WarehouseApp/goods/goodDetail.html', {'good':good, 'good_specs':good_specs})

def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'WarehouseApp/suppliers/suppliers.html', {'suppliers':suppliers})

def supplierDetail(request, supplier_id):
    supplier = Supplier.objects.get(id = supplier_id)
    return render(request, 'WarehouseApp/suppliers/supplierDetail.html', {'supplier':supplier})

def supplyGoodDetail(request, supplier_id, supplyGood_id):
    try:
        supply_good = SupGood.objects.get(id = supplyGood_id)
    except:
        raise Http404('Данного товара нет в списке поставляемых товаров, поставщика ' + str(Supplier.objects.get(id = supplier_id)))
    return render(request, 'WarehouseApp/suppliers/supplyGoodDetail.html', {'supply_good':supply_good})

def supplyForm(request):
    return HttpResponse('<h2>It\'s supply form</h2>')

def reportForm(request):
    return HttpResponse('<h2>It\'s report form</h2>')

def units(request):
    units = Unit.objects.all()
    return render(request, 'WarehouseApp/units/units.html', {'units':units})

def addUnit(request):
    return HttpResponse('<h2>Add</h2>')

def delUnit(request):
    return HttpResponse('<h2>Del</h2>')

def editUnit(request):
    return HttpResponse('<h2>Edit</h2>')

def sectionTypes(request):
    sectionTypes = SectionType.objects.all()
    return render(request, 'WarehouseApp/sections/sectionTypes.html', {'sectionTypes':sectionTypes})

def addSectionType(request):
    return HttpResponse('<h2>Add</h2>')

def delSectionType(request):
    return HttpResponse('<h2>Del</h2>')

def editSectionType(request):
    return HttpResponse('<h2>Edit</h2>')

def addSupplier(request):
    return HttpResponse('<h2>Asd</h2>')

def delSupplier(request):
    return HttpResponse('<h2>Asd</h2>')

def addSupply(request):
    return HttpResponse('<h2>Asd</h2>')

def supplies(request):
    supplies = Supply.objects.all()
    return render(request, 'WarehouseApp/supplies/supplies.html', {'supplies':supplies})

def delSupply(request):
    return HttpResponse('<h2>Asd</h2>')

def supplyDetail(request, supply_id):
    try:
        supply = Supply.objects.get(id = supply_id)
    except:
        return Http404('Такой поставки нет в базе данных')
    return render(request, 'WarehouseApp/supplies/supplyDetail.html', {'supply':supply})

def addReport(request):
    return HttpResponse('<h2>Asd</h2>')

def delReport(request):
    return HttpResponse('<h2>Asd</h2>')

def reportDetail(request, report_id):
    try:
        report = Report.objects.get(id = report_id)
    except:
        return Http404('Такого отчета в базе данных нет')
    return render(request, 'WarehouseApp/reports/reportDetail.html', {'report':report})

def reports(request):
    reports = Report.objects.all()
    return render(request, 'WarehouseApp/reports/reports.html', {'reports':reports})

def loadingForm(request):
    return HttpResponse('<h2>Asd</h2>')

def addLoading(request):
    return HttpResponse('<h2>Asd</h2>')

def loadings(request):
    loadings = Loading.objects.all()
    return render(request, 'WarehouseApp/loadings/loadings.html', {'loadings':loadings})

def loadingDetail(request, loading_id):
    try:
        loading = Loading.objects.get(id = loading_id)
    except:
        return Http404('Данного документа нет в бд')
    return render(request, 'WarehouseApp/loadings/loadingDetail.html', {'loading':loading})

def cellStatus(request):
    cellStatus = CellStatus.objects.all()
    return render(request, 'WarehouseApp/cellStatus/cellStatus.html', {'cellStatus':cellStatus})

def addCellStatus(request):
    return HttpResponse('<h2>Asd</h2>')

def delCellStatus(request):
    return HttpResponse('<h2>Asd</h2>')

def editCellStatus(request):
    return HttpResponse('<h2>Asd</h2>')

def goodGroups(request):
    groups = GoodGroup.objects.all()
    return render(request, 'WarehouseApp/goodGroups/goodGroups.html', {'groups':groups})

def addGoodGroup(request):
    return HttpResponse('<h2>Asd</h2>')

def delGoodGroup(request):
    return HttpResponse('<h2>Asd</h2>')

def editGoodGroup(request):
    return HttpResponse('<h2>Asd</h2>')

def positions(request):
    positions = Position.objects.all()
    return render(request, 'WarehouseApp/positions/positions.html', {'positions':positions})

def addPosition(request):
    return HttpResponse('<h2>Asd</h2>')

def delPosition(request):
    return HttpResponse('<h2>Asd</h2>')

def editPosition(request):
    return HttpResponse('<h2>Asd</h2>')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'WarehouseApp/categories/categories.html', {'categories':categories})

def addCategory(request):
    return HttpResponse('<h2>Asd</h2>')

def delCategory(request):
    return HttpResponse('<h2>Asd</h2>')

def editCategory(request):
    return HttpResponse('<h2>Asd</h2>')

def subcategories(request):
    subcategories = Subcategory.objects.all()
    return render(request, 'WarehouseApp/subcategories/subcategories.html', {'subcategories':subcategories})

def addSubcategory(request):
    return HttpResponse('<h2>Asd</h2>')

def delSubcategory(request):
    return HttpResponse('<h2>Asd</h2>')

def editSubcategory(request):
    return HttpResponse('<h2>Asd</h2>')

def emps(request):
    emps = Emp.objects.all()
    return render(request, 'WarehouseApp/emps/emps.html', {'emps':emps})

def empDetail(request, emp_id):
    try:
        emp = Emp.objects.get(id = emp_id)
    except:
        return Http404('Данного сотрудника нет в бд')
    return render(request, 'WarehouseApp/emps/empDetail.html', {'emp':emp})

def addEmp(request):
    return HttpResponse('<h2>Asd</h2>')

def delEmp(request):
    return HttpResponse('<h2>Asd</h2>')

def editEmp(request):
    return HttpResponse('<h2>Asd</h2>')

def addGood(request):
    return HttpResponse('<h2>Asd</h2>')

def delGood(request):
    return HttpResponse('<h2>Asd</h2>')

def editGood(request):
    return HttpResponse('<h2>Asd</h2>')

def receipts(request):
    receipts = Receipts.objects.all()
    return render(request, 'WarehouseApp/receipts/receipts.html', {'receipts':receipts})

def receiptDetail(request, receipt_id):
    try:
        receipt = Receipts.objects.get(id = receipt_id)
    except:
        return Http404('Данной накладной нет в бд')
    return render(request, 'WarehouseApp/receipts/receiptDetail.html', {'receipt':receipt})

def addReceip(request):
    return HttpResponse('<h2>Asd</h2>')

def delReceip(request):
    return HttpResponse('<h2>Asd</h2>')

def editReceip(request):
    return HttpResponse('<h2>Asd</h2>')

def expenditures(request):
    expenditures = Expenditure.objects.all()
    return render(request, 'WarehouseApp/expenditures/expenditures.html', {'expenditures':expenditures})

def expenditureDetail(request, expenditure_id):
    try:
        expenditure = Expenditure.objects.get(id = expenditure_id)
    except:
        return Http404('Данной накладной нет в бд')
    return render(request, 'WarehouseApp/expenditures/expenditureDetail.html', {'expenditure':expenditure})

def addExpenditure(request):
    return HttpResponse('<h2>Asd</h2>')

def delExpenditure(request):
    return HttpResponse('<h2>Asd</h2>')

def editExpenditure(request):
    return HttpResponse('<h2>Asd</h2>')

def goodMovings(request):
    return HttpResponse('<h2>Asd</h2>')

def addGoodMoving(request):
    return HttpResponse('<h2>Asd</h2>')

def delGoodMoving(request):
    return HttpResponse('<h2>Asd</h2>')