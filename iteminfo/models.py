from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=45)
    item_label = models.CharField(max_length=45)
    item_disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.item_disambiguator == '':
            result = '%s, %s' % (self.item_name, self.item_label)
        else:
            result = '%s, %s (%s)' % (self.item_name, self.item_label, self.item_disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('iteminfo_item_detailed_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('iteminfo_item_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('iteminfo_item_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['item_name', 'item_label', 'item_disambiguator']
        constraints = [
            UniqueConstraint(fields=['item_name', 'item_label', 'item_disambiguator'],
                             name='unique_item')
        ]


class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    warehouse_number = models.CharField(max_length=20)
    warehouse_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.warehouse_name, self.warehouse_number)

    def get_absolute_url(self):
        return reverse('iteminfo_warehouse_detailed_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('iteminfo_warehouse_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('iteminfo_warehouse_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['warehouse_name', 'warehouse_number']
        constraints = [
            UniqueConstraint(fields=['warehouse_name', 'warehouse_number'],
                             name='unique_warehouse')
        ]


class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    assignment_amount = models.CharField(max_length=20)
    warehouse = models.ForeignKey(Warehouse, related_name='assignments', on_delete=models.PROTECT)
    item = models.ForeignKey(Item, related_name='assignments', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s - %s' % (self.warehouse.warehouse_name, self.warehouse.warehouse_number, self.item.item_name)

    def get_absolute_url(self):
        return reverse('iteminfo_assignment_detailed_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('iteminfo_assignment_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('iteminfo_assignment_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['warehouse', 'assignment_amount']
        constraints = [
            UniqueConstraint(fields=['assignment_id', 'warehouse', 'item'],
                             name='unique_assignment')
        ]
