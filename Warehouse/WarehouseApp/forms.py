from asyncio.windows_events import NULL
from tabnanny import verbose
from django import forms
from .models import *

class UnitForm(forms.Form):
    name = forms.CharField(label='Единица измерения', max_length=25)

class SectionTypeForm(forms.Form):
    name = forms.CharField(label='Тип секции', max_length=125)

class GoodGroupForm(forms.Form):
    name = forms.CharField(label='Наименование группы товара', max_length=125)

class SectionForm(forms.Form):
    name = forms.CharField(label='Наименование секции', max_length=125)
    type = forms.ModelChoiceField(queryset=SectionType.objects.all(), empty_label='Тип секции')
    free_volume = forms.DecimalField(label='Свободный объем', max_digits=9, decimal_places=4)
    total_volume = forms.DecimalField(label='Общий объем', max_digits=9, decimal_places=4)

class CellStatusForm(forms.Form):
    name = forms.CharField(label='Статус ячейки', max_length=60)

class CellForm(forms.Form):
    section = forms.ModelChoiceField(queryset=Section.objects.all(), empty_label='Наименование секции')
    cell_status = forms.ModelChoiceField(queryset=CellStatus.objects.all(), empty_label='Статус ячейки')

class SupplierForm(forms.Form):
    company_name = forms.CharField(label='Наименованире кампании', max_length=125)
    company_phone = forms.CharField(label='Номер толефона', max_length=12)
    company_email = forms.EmailField(label='Электронная почта', widget=forms.EmailField)
    company_address = forms.CharField(label='Адрес', max_length=125)

class SupGoodForm(forms.Form):
    name = forms.CharField(label='Наименование товара', max_length=125)
    price = forms.DecimalField(label='Цена товара', max_digits=9, decimal_places=4)
    group = forms.ModelChoiceField(queryset=GoodGroup.objects.all(), empty_label = 'Товарная группа')
    volume = forms.DecimalField(label='Объем товара', max_digits=9, decimal_places=4)
    unit = forms.ModelChoiceField(queryset=Unit.objects.all(), empty_label='Единица измерения')
    supllier = forms.ModelChoiceField(queryset=Supplier.objects.all(), empty_label='Поставщик')

class PositionForm(forms.Form):
    pos_name = forms.CharField(label='Наименование позиции', max_length=120)
    salary = forms.DecimalField(label='Зарплата', max_digits=9, decimal_places=4)

class EmpForm(forms.Form):
    first_name = forms.CharField(label='Имя сотрудника', max_length=25)
    middle_name = forms.CharField(label='Имя сотрудника', max_length=25)
    last_name = forms.CharField(label='Имя сотрудника', max_length=25)
    phone = forms.CharField(label='Номер телефона', max_length=12)
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailField)
    position = forms.ModelChoiceField(queryset=Position.objects.all(), empty_label='Наименование должности')
    login = forms.CharField(label='Логин', max_length=25)
    password = forms.CharField(label='Пароль', max_length=25, widget=forms.PasswordInput)
    begin_date = forms.DateTimeField(label='Дата приема на работу')

class SupplyForm(forms.Form):
    supdate = forms.DateTimeField(label='Дата формирование поставки')
    total_cost = forms.DecimalField(label='Конечная цена', max_digits=9, decimal_places=4)
    emp = forms.ModelChoiceField(queryset=Emp.objects.all(), empty_label='Сотрудник, сформировавший поставку')

class SupStringForm(forms.Form):
    good = forms.ModelChoiceField(queryset=SupGood.objects.all(), empty_label='Товар поставки')
    amount = forms.IntegerField(label='Количество товара')

class CategoryForm(forms.Form):
    name = forms.CharField(label='Наименование категории', max_length=125)

class SubcategoryForm(forms.Form):
    name = forms.CharField(label='Наименование подкатегории', max_length=125)

class GoodsForm(forms.Form):
    name = forms.CharField(label='Наименование товара', max_length=125)
    price = forms.DecimalField(label='Цена товара', max_digits=12, decimal_places=4)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), empty_label='Поставщик')
    unit = forms.ModelChoiceField(queryse=Unit.objects.all(), empty_label='Единица измерения')
    volume = forms.DecimalField(label='Объем товара', max_digits=9, decimal_places=4)
    place = forms.ModelChoiceField(queryset=Cell.objects.all(), empty_label='Место на складе')
    icon = forms.ImageField(label='Иконка товара')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория товара')
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all(), empty_label='Подкатегория товара')
    group = forms.ModelChoiceField(queryset=GoodGroup.objects.all(), empty_label='Товарная группа')

class GoodMovingForm(forms.Form):
    place_from_section = forms.ModelChoiceField(queryset=Section.objects.all(), empty_label='Откуда: секция')
    place_from_cell = forms.ModelChoiceField(queryset=Cell.objects.all(), empty_label='Откуда: ячейка')
    place_to_section = forms.ModelChoiceField(queryset=Section.objects.all(), empty_label='Куда: секция')
    place_to_cell = forms.ModelChoiceField(queryset=Cell.objects.all(), empty_label='Куда: ячейка')
    good_moving = forms.ModelChoiceField(queryset=Goods.objects.all(), empty_label='Перемещаемый товар')
    emp = forms.ModelChoiceField(queryset=Emp.objects.all(), empty_label='Сотрудник')

class ReceiptsForm(forms.Form):
    taking_day = forms.DateTimeField(label='Дата приема товаров')
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), empty_label='Поставщик')
    receiver_company = forms.CharField(label='Кампания получатель', max_length=125)
    amount = forms.IntegerField(label='Количество товара')
    good = forms.ModelChoiceField(queryset=Goods.objects.all(), empty_label='Товар')
    total_cost = forms.DecimalField(label='Конечная цена', max_digits=9, decimal_places=5)
    emp = forms.ModelChoiceField(queryset=Emp.objects.all(), empty_label='Сотрудник')

class ExpenditureForm(forms.Form):
    issue_date = forms.DateTimeField(label='Дата выдачи')
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), empty_label='Поставщик')
    receiver_company = forms.CharField(label='Кампания получатель', max_length=125)
    amount = forms.IntegerField(label='Количество товара')
    good = forms.ModelChoiceField(queryset=Goods.objects.all(), empty_label='Товар')
    total_cost = forms.DecimalField(label='Конечная цена', max_digits=9, decimal_places=5)
    emp = forms.ModelChoiceField(queryset=Emp.objects.all(), empty_label='Сотрудник')

class LoadingForm(forms.Form):
    good = forms.ModelChoiceField(queryset=Goods.objects.all(), empty_label='Товар для отгрузки')
    amount = forms.IntegerField(label='Отгружаемое количество')
    date = forms.DateField(label='Дата отгрузки', auto_now_add=True)

class ReportForm(forms.Form):
    starting_good_balance = forms.IntegerField(label='Начальный остаток товара')
    receipts = forms.ModelChoiceField(queryset=Receipts.objects.all(), empty_label='Накладная')
    expenditure = forms.ModelChoiceField(queryset=Expenditure.objects.all(), empty_label='Доверенность')
    closing_good_balance = forms.IntegerField(label='Конечный остаток товара')