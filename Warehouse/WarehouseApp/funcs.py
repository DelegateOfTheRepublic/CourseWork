from django.db.models import *

from WarehouseApp.models import *
from WarehouseApp.forms import *

class Filter:
    rangeNames = ['price', 'date', 'total_cost']

    def __init__(self, *args, **kwargs):
        super(Filter, self).__init__(*args, **kwargs)

    def makeFilterFromRanges(**kwargs):
        result = Q()
        print('makeFilterFromRanges1')
        if len(kwargs) != 0:
            print(kwargs)
            for kwargKey in kwargs.keys():
                if kwargs[kwargKey] != None:
                    result &= Q(**{kwargKey+'__gte': kwargs[kwargKey][0],
                               kwargKey+'__lte': kwargs[kwargKey][1]})
        return result

    def makeFilter(querySet, filters: list, select: Q = NULL, **kwargs):
        if len(filters) != 0:
            print('makeFilter1')
            print(kwargs)
            resultFilter = Q()
            print(filters)
            print('makeFilter2')
            print('makeFilter3')
            for key in filters:
                print('makeFilter4')
                if (querySet[key] != ''):
                    resultFilter &= Q(**{key: querySet[key]})
            filterFromRanges = Filter.makeFilterFromRanges(**kwargs)
            print('makeFilter5 {0}'.format(resultFilter if select == NULL else select & resultFilter & filterFromRanges))
            return resultFilter & filterFromRanges if select == NULL else select & resultFilter & filterFromRanges
        else:
            filterFromRanges = Filter.makeFilterFromRanges(**kwargs)
            return filterFromRanges if select == NULL else select & filterFromRanges

    def makeOrderString(order: list):
        print('makeOrderString1 {0}'.format(order))
        if order[0] in [' ', '-']:
            print('makeOrderString2')
            return (order[0]+"id").strip() if len(order) == 1 else (order[0]+order[1]).strip()
        else:
            order.reverse()
            print('makeOrderString3 ({0})'.format("".join(order).strip()))
            return "".join(order).strip()

    def makeOrder(querySet, model, order: list, filters: list = NULL, select: Q = NULL, **kwargs):
        resultOrder = None
        print('makeOrder1{0}'.format(order))
        print('makeOrder2{0}'.format(select))
        if filters != NULL:
            print('makeOrder3')
            filter = Filter.makeFilter(querySet, filters, select, **kwargs)
            print('makeOrder4 {0} ({1})'.format(filter, Filter.makeOrderString(order)))
            resultOrder = model.objects.filter(filter).order_by(Filter.makeOrderString(order))
            print('makeOrder5 {0}'.format(resultOrder))
        else:
            if select == NULL:
                resultOrder = model.objects.all().order_by(Filter.makeOrderString(order))
            else:
                resultOrder = model.objects.filter(select).order_by(Filter.makeOrderString(order))
            print('makeOrder6')
        return resultOrder

    def getFilters(querySet):
        filters = []
        for key in querySet.keys():
            if not (key in Filter.rangeNames or key in ['order']):
                filters.append(key)
        return filters

    def checkRenges(ranges):
        booleans = [range != None for range in ranges.values()]
        result = False
        for bool in booleans:
            result = result or bool
        return result if len(ranges) != 0 else False

    def applyFilter(querySet, model, select: Q = NULL):
        result = model.objects.all() if select == NULL else model.objects.filter(select)
        ranges = {}

        if (querySet):
            queryKeys = querySet.keys()
            print(queryKeys)
            orders = querySet.getlist('order') if 'order' in queryKeys else None
            filters = Filter.getFilters(querySet)
            filters = filters if len(filters) != 0 else None
            for rangeName in Filter.rangeNames:
                if rangeName in querySet:
                    print(querySet.getlist(rangeName))
                    ranges[rangeName] = querySet.getlist(rangeName) if len(querySet.getlist(rangeName)[0]) != 0 and len(querySet.getlist(rangeName)[1]) != 0 else None
            print('applyFilter1 {0} {1} {2}'.format(orders, filters, ranges))

            if (orders != None and filters != None and Filter.checkRenges(ranges)):
                print('bbbbbbbbbbbb')
                result = Filter.makeOrder(querySet, model, orders, filters, select, **ranges)
                print('aaaaaaaaaaaa')
                print('applyFilter2 {0}'.format(result))

            if orders != None and not (filters == None and Filter.checkRenges(ranges)):
                print('applyFilter3')
                result = Filter.makeOrder(querySet, model, orders, select= select)

            if orders == None:
                if filters != None and Filter.checkRenges(ranges):
                    print('applyFilter4')
                    result = model.objects.filter(Filter.makeFilter(querySet, filters, select, **ranges))
                elif filters == None and Filter.checkRenges(ranges):
                    print('applyFilter5')
                    result = model.objects.filter(Filter.makeFilter(querySet, [], select, **ranges))
                    print('applyFilter6')
                elif filters != None and not Filter.checkRenges(ranges):
                    print('applyFilter7')
                    result = model.objects.filter(Filter.makeFilter(querySet, filters, select))
                    print('applyFilter8')
        return result