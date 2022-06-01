from time import timezone
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.

class Unit(models.Model):
    name = models.CharField('Единица измерения', max_length=25)

    def __str__(self):
        return self.name

class SectionType(models.Model):
    name = models.CharField('Тип секции', max_length=125)

    def __str__(self):
        return self.name

class GoodGroup(models.Model):
    name = models.CharField('Наименование группы товара', max_length=125)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField('Наименование секции', max_length=125)
    type = models.ForeignKey(SectionType, on_delete=models.SET_NULL, null=True, verbose_name='Тип секции')
    free_volume = models.DecimalField('Свободный объем', max_digits=9, decimal_places=4)
    total_volume = models.DecimalField('Общий объем', max_digits=9, decimal_places=4)

    def __str__(self):
        return self.name

class CellStatus(models.Model):
    name = models.CharField('Статус ячейки', max_length=60)

    def __str__(self):
        return self.name

class Cell(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Наименование секции')
    cell_status = models.ForeignKey(CellStatus, on_delete=models.SET_NULL, null=True, verbose_name='Статус ячейки', default=0)

    def __str__(self):
        return '{0}:{1}'.format(self.section, self.id)

class Supplier(models.Model):
    company_name = models.CharField('Наименованире кампании', max_length=125)
    company_phone = models.CharField('Номер толефона', max_length=12)
    company_email = models.EmailField('Электронная почта')
    company_address = models.CharField('Адрес', max_length=125)

    def get_supplier_goods(self):
        return SupGood.objects.filter(supllier = self.id)

    def get_verbose_name(self, field_name):
        return self._meta.get_field(field_name).verbose_name

    def get_model_fields(self):
        return self._meta.fields

    def __str__(self):
        return self.company_name

class SupGood(models.Model):
    name = models.CharField('Наименование товара', max_length=125)
    price = models.DecimalField('Цена товара', max_digits=9, decimal_places=4)
    group = models.ForeignKey(GoodGroup, on_delete=models.SET_NULL, null=True, verbose_name = 'Товарная группа')
    volume = models.DecimalField('Объем товара', max_digits=9, decimal_places=4)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, verbose_name='Единица измерения')
    supllier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, verbose_name='Поставщик')

    def get_verbose_name(self, field_name):
        return self._meta.get_field(field_name).verbose_name

    def get_model_fields(self):
        return self._meta.fields

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField('Наименование позиции', max_length=120)
    salary = models.DecimalField('Зарплата', max_digits=9, decimal_places=4)

    def __str__(self):
        return self.name

class Emp(models.Model):
    first_name = models.CharField('Имя сотрудника', max_length=25)
    middle_name = models.CharField('Фамилия сотрудника', max_length=25)
    last_name = models.CharField('Отчество сотрудника', max_length=25)
    phone = models.CharField('Номер телефона', max_length=12)
    email = models.EmailField('Электронная почта')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, verbose_name='Наименование должности')
    login = models.CharField('Логин', max_length=25)
    password = models.CharField('Пароль', max_length=25)
    begin_date = models.DateTimeField('Дата приема на работу')

    def __str__(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.middle_name)

class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, verbose_name='Постащик')
    date = models.DateTimeField('Дата формирование поставки', auto_now_add=True, blank=True)
    total_cost = models.DecimalField('Конечная цена', max_digits=9, decimal_places=4)
    emp = models.ForeignKey(Emp, on_delete=models.SET_NULL, null=True, verbose_name='Сотрудник, сформировавший поставку')

    def get_supply_string(self):
        return SupString.objects.filter(supply = self.id)

    def get_verbose_name(self, field_name):
        return self._meta.get_field(field_name).verbose_name

    def get_model_fields(self):
        return self._meta.fields

    def __str__(self):
        return 'Supply №{0}'.format(self.id)

class SupString(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, verbose_name='Номер поставки')
    good = models.ForeignKey(SupGood, on_delete=models.SET_NULL, null=True, verbose_name='Товар поставки')
    amount = models.IntegerField('Количество товара')
    cost = models.DecimalField('Стоимость, в соответствии с количеством товара', max_digits=9, decimal_places=5)

    def get_verbose_name(self, field_name):
        return self._meta.get_field(field_name).verbose_name

    def get_model_fields(self):
        return self._meta.fields

    def calc_cost(self):
        self.cost = self.amount * self.good.price

    def __str__(self):
        return '{0}:SubString №{1}'.format(self.supply, self.id)

class Category(models.Model):
    name = models.CharField('Наименование категории', max_length=125)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField('Наименование подкатегории', max_length=125)

    def __str__(self):
        return self.name

def good_path(good, filename):
    return '{0}/{1}/{2}/supplier_{3}_{4}/{5}'.format(good.category, good.subcategory, good.group, good.supplier.id, good.name, filename)

class Goods(models.Model):
    name = models.CharField('Наименование товара', max_length=125)
    price = models.DecimalField('Цена товара', max_digits=12, decimal_places=4)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, verbose_name='Поставщик')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, verbose_name='Единица измерения')
    volume = models.DecimalField('Объем товара', max_digits=9, decimal_places=4)
    place = models.ForeignKey(Cell, on_delete=models.SET_NULL, null=True, verbose_name='Место на складе')
    icon = models.ImageField(upload_to=good_path, max_length=500)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, verbose_name='Подкатегория')
    group = models.ForeignKey(GoodGroup, on_delete=models.SET_NULL, null=True, verbose_name='Группа')
    specs = models.FileField(upload_to=good_path, validators=[FileExtensionValidator(allowed_extensions=["json"])], max_length=500)

    def __str__(self):
        return self.name

class GoodMoving(models.Model):
    progressStatus = (
        ('ps', 'Well done'),
        ('ip', 'In progress')
    )

    place_from_section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, verbose_name='Откуда: секция', related_name='place_from_section')
    place_from_cell = models.ForeignKey(Cell, on_delete=models.SET_NULL, null=True, verbose_name='Откуда: ячейка', related_name='place_from_cell')
    place_to_section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, verbose_name='Куда: секция', related_name='place_to_section')
    place_to_cell = models.ForeignKey(Cell, on_delete=models.SET_NULL, null=True, verbose_name='Куда: ячейка', related_name='place_to_cell')
    good_moving = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Перемещаемый товар')
    emp = models.ForeignKey(Emp, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сотрудник')
    status = models.CharField('Статус выполнения', max_length=2, choices=progressStatus, default='ip')

    def __str__(self):
        return 'Good moving №{0}'.format(self.id)

class Receipts(models.Model):
    taking_day = models.DateTimeField()
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Поставщик')
    receiver_company = models.CharField('Кампания получатель', max_length=125)
    total_cost = models.DecimalField('Конечная цена', max_digits=9, decimal_places=5)
    rec_employee = models.ForeignKey(Emp, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сотрудник')

    def __str__(self):
        return 'Receipts №{0}'.format(self.id)

class ReceiptString(models.Model):
    receipt = models.ForeignKey(Receipts, on_delete=models.CASCADE, verbose_name='Номер накладной')
    good = models.ForeignKey(SupGood, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Товар')
    amount = models.IntegerField('Количество товара')

    def __str__(self):
        return '{0}:ReceiptString №{1}'.format(self.receipt, self.id) 

class Expenditure(models.Model):
    issue_date = models.DateTimeField()
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Поставщик')
    receiver_company = models.CharField('Кампания получатель', max_length=125)
    total_cost = models.DecimalField('Конечная цена', max_digits=9, decimal_places=5)
    exp_employee = models.ForeignKey(Emp, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сотрудник')

    def __str__(self):
        return 'Expenditure №{0}'.format(self.id)

class ExpenditureString(models.Model):
    expenditure = models.ForeignKey(Expenditure, on_delete=models.CASCADE, verbose_name='Номер доверенности')
    good = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Товар')
    amount = models.IntegerField('Количество товара')

    def __str__(self):
        return '{0}:ExpenditureString №{1}'.format(self.expenditure, self.id)

class Loading(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField('Отгружаемое количество')
    date = models.DateField('Дата отгрузки', auto_now_add=True)

    def __str__(self):
        return 'Loading №{0}'.format(self.id)

class Register(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True)
    starting_amount = models.IntegerField('Начальное количество товара')
    receive_date = models.DateField('Дата поступления')
    receipt = models.ForeignKey(Receipts, on_delete=models.SET_NULL, null=True)
    expiration_date = models.DateField('Дата реализации', null=True, blank=True)
    loading = models.ForeignKey(Loading, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return 'Register №{0}'.format(self.id)

class Report(models.Model):
    date = models.DateTimeField('Дата формирования отчета', auto_now_add=True)

    def __str__(self):
        return 'Report №{0}'.format(self.id)

class ReportString(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, verbose_name='Номер отчета')
    starting_good_balance = models.IntegerField('Начальный остаток товара')
    receipts = models.ForeignKey(Receipts, on_delete=models.SET_NULL, null=True, verbose_name='Накладная')
    loading = models.ForeignKey(Loading, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Отгрузка')
    closing_good_balance = models.IntegerField('Конечный остаток товара')

    def __str__(self):
        return '{0}:ReportString №{1}'.format(self.report, self.id)

class EmpReport(models.Model):
    emp = models.ForeignKey(Emp, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сотрудник')
    report = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Отчет')

    def __str__(self):
        return 'EmpReport №{0}'.format(self.id)