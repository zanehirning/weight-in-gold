from django.db import models

class convTable(models.Model):
    unit = models.CharField(max_length=10)
    float = models.FloatField(max_length=40)
    def toUnit(self):
        return self.float
    #def toPound(self, firstUnit, secondUnit, value):
    #    unit_conversions = {
    #        ('t_oz', 'lb'): 0.0685714,
    #        ('T', 'lb'): 2204.62,
    #        ('g', 'lb'): 0.00220462,
    #        ('kg', 'lb'): 2.20462,
    #        ('oz', 'lb'): 0.0625,
    #        ('lb', 'lb'): 1,
    #    }
    #    return (float(value) * unit_conversions[f'{firstUnit}', f'{secondUnit}']);
#
    #def toUnit(self, firstUnit, secondUnit, value):
    #    pounds = convTable.toPound(self, firstUnit, 'lb', value)
    #    unit_conversions = {
    #        ('lb', 'T'): 0.0005,
    #        ('lb', 't_oz'): 14.5833,
    #        ('lb', 'g'): 453.592,
    #        ('lb', 'kg'): 0.453592,
    #        ('lb', 'oz'): 16,
    #    }
    #    return (float(pounds) * unit_conversions[f'lb', f'{secondUnit}']);

# Create your models here.
