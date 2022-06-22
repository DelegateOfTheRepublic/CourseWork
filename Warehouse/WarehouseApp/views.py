from ast import Or
from contextlib import closing
from datetime import date
import json
import math
import os
from django.db import connection
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template.defaulttags import register
from django.db.models import *
from django.core import serializers
from django.forms.models import model_to_dict

from WarehouseApp.models import *
from WarehouseApp.forms import *
from WarehouseApp.funcs import *


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_item_by_id(list, index):
    return list[index]

@register.filter
def get_good(key):
    return key.split('_')[0]

@register.filter
def get_supplier(key):
    return Supplier.objects.get(id = int(key.split('_')[1]))

@register.filter
def get_attribute(model, field):
    return getattr(model, field.name)

@register.filter
def get_verb_name(model, field):
    return model.get_verbose_name(field.name)

@register.filter
def get_id(model):
    return model.get_id()

def login(request):
    return render(request, "WarehouseApp/login/login.html")

def warehouseMap(request):
    sections = Section.objects.all()
    goods = Goods.objects.all()
    return render(request, "WarehouseApp/warehouseMap/map.html", {'sections':sections, 'goods':goods})

def sectionDetail(request, section_id):
    queryFilter = Filter
    good_specs = {}
    try:
        temp_goods = Goods.objects.filter(place__section__id = section_id)
        abs_path = os.path.abspath(__file__).split('\\')
        del abs_path[-1]
        del abs_path[-1]
        abs_path = '\\'.join(abs_path)
        for good in temp_goods:
            file_name = good.specs.url.split('/')[-1]
            path_to_json_specs = (abs_path + "/itemsIcons/" + good.category.name + "/" + good.subcategory.name + "/" + good.group.name + "/supplier_" + str(good.supplier.id) + "_" + good.name + "/" + file_name)
            path_to_json_specs = path_to_json_specs.replace('/', '\\')
            print("a: " + path_to_json_specs)
            with open(path_to_json_specs, 'rb') as json_data:
                good_specs[good] = json.load(json_data)
        suppliers = Supplier.objects.all()
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        goodGroups = GoodGroup.objects.all()
        querySet = request.GET
        resultQuery = queryFilter.applyFilter(querySet, Goods, Q(place__section__id = section_id))
    except:
        raise Http404('Данной секции не существует')
    return render(request, 'WarehouseApp/sections/sectionDetail.html', {'goods':resultQuery, 'section_id':section_id, 
                                                                        'suppliers':suppliers, 'categories':categories,
                                                                        'subcategories':subcategories, 'goodGroups':goodGroups,
                                                                        'specs':good_specs})

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
    return render(request, 'WarehouseApp/goods/goodDetail.html', {'good':good, 'good_specs':good_specs, 'section_id':section_id})

def suppliers(request):
    suppliers = Supplier.objects.all()
    supGoods = SupGood.objects.all().distinct()
    goodGroups = GoodGroup.objects.all()

    querySet = request.GET
    addFilterOptions = ['price', 'name', 'group']
    supGoodQuerySet = querySet.copy()
    supplierQuerySet = querySet.copy()

    print('ASA {0}'.format(querySet))
    print('ASA5 {0}'.format(supGoodQuerySet))

    for key in list(supGoodQuerySet.keys()):
        if not key in addFilterOptions:
            supGoodQuerySet.pop(key)

    for key in addFilterOptions:
        if key in supplierQuerySet.keys():
            supplierQuerySet.pop(key)

    filteredSupGoods = Filter.applyFilter(supGoodQuerySet, SupGood)
    filteredSuppliers = Supplier.objects.filter(id__in = [fsg.supplier.id for fsg in filteredSupGoods])
    orderedSuppliers = Filter.applyFilter(supplierQuerySet, Supplier)
    print('ASA2 {0}'.format(supplierQuerySet))
    print('ASA3 {0}'.format(supGoodQuerySet))
    print('ASA {0}'.format(orderedSuppliers))
    print('ASA {0}'.format(filteredSuppliers))

    suppliers = orderedSuppliers & filteredSuppliers

    return render(request, 'WarehouseApp/suppliers/suppliers.html', {'suppliers':suppliers, 'supGoods':supGoods,
                                                                     'goodGroups':goodGroups})

def supplierDetail(request, supplier_id):
    suppliers = Supplier.objects.all()
    supplier = Supplier.objects.get(id = supplier_id)
    return render(request, 'WarehouseApp/suppliers/supplierDetail.html', {'supplier':supplier, 'suppliers': suppliers})

def supplyGoodDetail(request, supplier_id, supplyGood_id):
    try:
        supplier = Supplier.objects.get(id = supplier_id)
        supply_good = SupGood.objects.get(id = supplyGood_id)
    except:
        raise Http404('Данного товара нет в списке поставляемых товаров, поставщика ' + str(Supplier.objects.get(id = supplier_id)))
    return render(request, 'WarehouseApp/suppliers/supplyGoodDetail.html', {'supply_good':supply_good, 'supplier':supplier})

def units(request):
    units = Unit.objects.all()
    return render(request, 'WarehouseApp/units/units.html', {'units':units})

def sectionTypes(request):
    sectionTypes = SectionType.objects.all()
    return render(request, 'WarehouseApp/sections/sectionTypes.html', {'sectionTypes':sectionTypes})

def supplies(request):
    supplies = Supply.objects.all()
    emps = Emp.objects.all()
    suppliers = Supplier.objects.all()

    supplies = Filter.applyFilter(request.GET, Supply)

    return render(request, 'WarehouseApp/supplies/supplies.html', {'supplies':supplies, 'suppliers':suppliers,
                                                                   'emps':emps})

def supplyDetail(request, supply_id):
    try:
        supply = Supply.objects.get(id = supply_id)
        supplies = Supply.objects.all()
    except:
        return Http404('Такой поставки нет в базе данных')
    return render(request, 'WarehouseApp/supplies/supplyDetail.html', {'supply':supply, 'supplies':supplies})

def reportDetail(request, report_id):
    try:
        report = Report.objects.get(id = report_id)
        reports = Report.objects.all()
    except:
        return Http404('Такого отчета в базе данных нет')
    return render(request, 'WarehouseApp/reports/reportDetail.html', {'report':report, 'reports':reports})

def reports(request):
    queryFilter = Filter
    querySet = request.GET
    resultQuery = Report.objects.all()
    emps = Emp.objects.all()
    receipts = Receipts.objects.all()
    loadings = Loading.objects.all()
    copyQuerySet = querySet.copy()

    addFilterOprions = {'emp': [EmpReport, Report], 'receipts': [ReportString, Report], 'loading': [ReportString, Report]}
    addFilterOprionsKI = {}
    reports = {}
    resultReports = []

    for key in addFilterOprions.keys():
        id = copyQuerySet.pop('afo_'+key)[0] if 'afo_'+key in copyQuerySet.keys() else None
        addFilterOprionsKI[key] = id

    for key in addFilterOprionsKI.keys():
        if addFilterOprionsKI[key] != None:
            reports = addFilterOprions[key][0].objects.filter(Q(**{key: addFilterOprionsKI[key]}))
            reports = addFilterOprions[key][1].objects.filter(id__in = [report.report.id for report in reports])
            resultReports.append(reports)
    
    if len(resultReports) != 0:
        resultReport = resultReports[0]
        for index in range(1, len(resultReports)):
            resultReport &= resultReports[index]
        resultQuery = resultQuery & resultReport
    else:
        resultQuery = queryFilter.applyFilter(copyQuerySet, Report)
    
    return render(request, 'WarehouseApp/reports/reports.html', {'reports':resultQuery, 'emps':emps,
                                                                 'receipts':receipts, 'loadings':loadings})

def supplyForm(request):
    supply_goods = SupGood.objects.all()

    if request.method == 'POST':
        emp = 1

        supplierSupGoods = {}
        for key in request.POST.keys():
            if 'id_' in key:
                supGoodId = key.split('_')[-1]
                supplierId = SupGood.objects.get(id = supGoodId).supplier.id
                if supplierId in supplierSupGoods.keys():
                    supplierSupGoods[supplierId].append(supGoodId)
                else:
                    supplierSupGoods[supplierId] = [supGoodId]
                
        for supplierId in supplierSupGoods.keys():
            totalCost = sum([supplyGood.price * int(request.POST.getlist('id_'+str(supplyGood.id))[-1]) for supplyGood in SupGood.objects.filter(supplier = supplierId, id__in = supplierSupGoods[supplierId])])
            newSupply = Supply.objects.create(
                supplier_id = supplierId,
                total_cost = totalCost,
                emp_id = 1
            )

            supplyId = Supply.objects.aggregate(Max('id'))['id__max']
            for supplyGoodId in supplierSupGoods[supplierId]:
                needAmount = int(request.POST.getlist('id_'+supplyGoodId)[-1])
                newSupString = SupString.objects.create(
                    supply_id = supplyId,
                    good_id = supplyGoodId,
                    amount = needAmount,
                    cost = needAmount * SupGood.objects.get(id = supplyGoodId).price
                )

        return redirect('supplyForm')
    return render(request, 'WarehouseApp/supplyForm/supplyForm.html', {'supply_goods':supply_goods})

def loadingForm(request):
    goods = Goods.objects.all()

    if request.method == "POST":

        copyQuerySet = request.POST.copy()
        for key in list(copyQuerySet.keys()):
            if not 'id_' in key:
                copyQuerySet.pop(key)

        if len(copyQuerySet) > 0:
            loading = Loading.objects.create()
            empLoading = EmpLoading.objects.create(
                loading_id = loading.id,
                emp_id = 1
            )  

            for key in copyQuerySet.keys():
                if 'id_' in key:
                    good = Goods.objects.get(id = int(key.split('_')[-1]))
                    loadingAmount = int(copyQuerySet.getlist(key)[-1])
                    loadingString = LoadingString.objects.create(
                        loading_id = loading.id,
                        good_id = good.id,
                        loading_amount = loadingAmount
                    )
                    print(f"{key}: {good}, {good.id}, {loading.date}")
                    regGood = Register.objects.filter(good__id = good.id, receive_date = loading.date)
                    print(regGood)
                    if len(regGood) != 0:
                        print(regGood)
                        regGood.expiration_date = loading.date
                        regGood.loading_id = loading.id
                        regGood.loading_amount = loadingAmount
                        regGood.save()
                    else:
                        registerItem = Register.objects.create(
                            good_id = good.id,
                            starting_amount = good.amount,
                            expiration_date = date.today(),
                            loading_id = loading.id,
                            loading_amount = loadingAmount
                        )

                    good.amount -= loadingAmount
                    good.save()
        return redirect('loadingForm')

    return render(request, 'WarehouseApp/loadingForm/loadingForm.html', {'goods':goods})

global resultRegister
resultRegister = {}

def reportForm(request):
    global resultRegister
    if request.method == "GET" and len(request.GET) > 0:
        resultRegister = {}
        dates = request.GET.getlist('date')
        registersWRD = Register.objects.filter(receive_date__gte = dates[0], receive_date__lte = dates[1]).distinct()
        registersWED = Register.objects.filter(expiration_date__gte = dates[0], expiration_date__lte = dates[1]).distinct()
        unionRegister = registersWRD | registersWED

        for registerItem in unionRegister:
            key = f"{registerItem.good}_{registerItem.good.supplier.id}"
            if key in resultRegister.keys():
                resultRegister[key].append(registerItem)
            else:
                resultRegister[key] = [registerItem]    
        print(resultRegister) 

    elif request.method == "POST":
        if len(resultRegister) != 0:
            report = Report.objects.create()
            empReport = EmpReport.objects.create(
                emp_id = 1,
                report_id = report.id
            )
            print(resultRegister)
            for key in resultRegister.keys():
                for registerItem in resultRegister[key]:
                    reportString = ReportString.objects.create(
                        good_id = registerItem.good.id,
                        report_id = report.id,
                        starting_good_balance = int(registerItem.starting_amount),
                        receipts_id = registerItem.receipt.id if registerItem.receipt != None else None,
                        loading_id = registerItem.loading.id if registerItem.loading != None else None,
                        closing_good_balance = int(registerItem.starting_amount) - int(registerItem.loading_amount if registerItem.loading_amount != None else 0)
                    )
            resultRegister = {}
            return redirect('reportForm')
        else: return redirect('reportForm')

    return render(request, 'WarehouseApp/reportForm/reportForm.html', {'register':resultRegister})

def addLoading(request):
    return HttpResponse('<h2>Asd</h2>')

def loadings(request):
    emps = Emp.objects.all()
    goods = Goods.objects.all()

    querySet = request.GET
    copyQuerySet = querySet.copy()

    addFilterOprions = {'emp': [EmpLoading, Loading], 'good': [LoadingString, Loading], 'loading_amount': [LoadingString, Loading]}
    addFilterOprionsKI = {}
    loadings = {}
    resultQuery = Loading.objects.all()
    resultLoadings = []

    for key in addFilterOprions.keys():
        if len(copyQuerySet.getlist('afo_'+key)) == 2:
            id = copyQuerySet.pop('afo_'+key) if 'afo_'+key in copyQuerySet.keys() and len(querySet.getlist('afo_'+key)[0]) != 0 and len(querySet.getlist('afo_'+key)[1]) != 0 else None
        else:
            id = copyQuerySet.pop('afo_'+key)[0] if 'afo_'+key in copyQuerySet.keys() else None
        addFilterOprionsKI[key] = id
    print('AGA {0}'.format(addFilterOprionsKI))

    for key in addFilterOprionsKI.keys():
        if addFilterOprionsKI[key] != None:
            if len(addFilterOprionsKI[key]) == 2:
                if addFilterOprionsKI[key][0] != '' and addFilterOprionsKI[key][1] != '':
                    loadings = addFilterOprions[key][0].objects.filter(Q(**{key+"__gte": addFilterOprionsKI[key][0],
                                                                            key+"__lte": addFilterOprionsKI[key][1]}))
                else:
                    loadings = {}                                                        
            else:
                loadings = addFilterOprions[key][0].objects.filter(Q(**{key: addFilterOprionsKI[key]}))
            loadings = addFilterOprions[key][1].objects.filter(id__in = [loading.loading.id for loading in loadings])
            resultLoadings.append(loadings)
    
    if len(resultLoadings) != 0:
        resultLoading = resultLoadings[0]
        for index in range(1, len(resultLoadings)):
            resultLoading &= resultLoadings[index]
        resultQuery = resultQuery & resultLoading
    else:
        resultQuery = Filter.applyFilter(copyQuerySet, Loading)

    return render(request, 'WarehouseApp/loadings/loadings.html', {'loadings':resultQuery, 'emps':emps,
                                                                   'goods':goods})

def loadingDetail(request, loading_id):
    try:
        loading = Loading.objects.get(id = loading_id)
        loadings = Loading.objects.all()
    except:
        return Http404('Данного документа нет в бд')
    return render(request, 'WarehouseApp/loadings/loadingDetail.html', {'loading':loading, 'loadings':loadings})

def emps(request):
    queryFilter = Filter
    querySet = request.GET
    resultQuery = queryFilter.applyFilter(querySet, Emp)
    positions = Position.objects.all()
    return render(request, 'WarehouseApp/emps/emps.html', {'emps':resultQuery, 'positions':positions})

def empDetail(request, emp_id):
    try:
        emp = Emp.objects.get(id = emp_id)
        emps = Emp.objects.all()
    except:
        return Http404('Данного сотрудника нет в бд')
    return render(request, 'WarehouseApp/emps/empDetail.html', {'emp':emp, 'emps':emps})

def receipts(request):
    queryFilter = Filter
    querySet = request.GET
    resultQuery = queryFilter.applyFilter(querySet, Receipts)
    emps = Emp.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'WarehouseApp/receipts/receipts.html', {'receipts':resultQuery, 'emps':emps,
                                                                   'suppliers':suppliers})

def receiptDetail(request, receipt_id):
    try:
        receipt = Receipts.objects.get(id = receipt_id)
        receipts = Receipts.objects.all()
    except:
        return Http404('Данной накладной нет в бд')
    return render(request, 'WarehouseApp/receipts/receiptDetail.html', {'receipt':receipt, 'receipts':receipts})

def expenditures(request):
    queryFilter = Filter
    querySet = request.GET
    resultQuery = queryFilter.applyFilter(querySet, Expenditure)
    emps = Emp.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'WarehouseApp/expenditures/expenditures.html', {'expenditures':resultQuery, 'emps':emps,
                                                                           'suppliers':suppliers})

def expenditureDetail(request, expenditure_id):
    try:
        expenditure = Expenditure.objects.get(id = expenditure_id)
        expenditures = Expenditure.objects.all()
    except:
        return Http404('Данной накладной нет в бд')
    return render(request, 'WarehouseApp/expenditures/expenditureDetail.html', {'expenditure':expenditure, 'expenditures':expenditures})

def goodMovings(request):
    goodMovings = GoodMoving.objects.all()
    return render(request, 'WarehouseApp/goodMoving/goodMovings.html', {'goodMovings':goodMovings})