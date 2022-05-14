from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView

from iteminfo.forms import ItemForm, AssignmentForm, WarehouseForm
from iteminfo.models import Item, Assignment, Warehouse
from iteminfo.utils import PageLinksMixin


class ItemList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Item


class ItemDetail(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        item = self.get_object()
        assignment_list = item.assignments.all()
        context['assignment_list'] = assignment_list
        return context


class ItemCreate( CreateView):
    form_class = ItemForm
    model = Item


class ItemUpdate(UpdateView):
    form_class = ItemForm
    model = Item
    template_name = 'iteminfo/item_form_update.html'


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('iteminfo_item_list_urlpattern')

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        assignments = item.assignments.all()
        if assignments.count() > 0:
            return render(
                request,
                'iteminfo/item_refuse_delete.html',
                {'item': item,
                 'assignments': assignments,
                 }
            )
        else:
            return render(
                request,
                'iteminfo/item_confirm_delete.html',
                {'item': item}
            )


class WarehouseList(ListView):
    model = Warehouse


class WarehouseDetail(DetailView):
    model = Warehouse

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        warehouse = self.get_object()
        assignment_list = warehouse.assignments.all()
        context['assignment_list'] = assignment_list
        return context


class WarehouseCreate(CreateView):
    form_class = WarehouseForm
    model = Warehouse


class WarehouseUpdate(UpdateView):
    form_class = WarehouseForm
    model = Warehouse
    template_name = 'iteminfo/warehouse_form_update.html'


class WarehouseDelete(DeleteView):
    model = Warehouse
    success_url = reverse_lazy('iteminfo_warehouse_list_urlpattern')

    def get(self, request, pk):
        warehouse = get_object_or_404(Warehouse, pk=pk)
        assignments = warehouse.assignments.all()
        if assignments.count() > 0:
            return render(
                request,
                'iteminfo/warehouse_refuse_delete.html',
                {'warehouse': warehouse,
                 'assignments': assignments,
                 }
            )
        else:
            return render(
                request,
                'iteminfo/warehouse_confirm_delete.html',
                {'warehouse': warehouse}
            )


class AssignmentList(ListView):
    model = Assignment


class AssignmentDetail(DetailView):
    model = Assignment

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        assignment = self.get_object()
        item = assignment.item
        warehouse = assignment.warehouse
        context['item'] = item
        context['warehouse'] = warehouse
        return context


class AssignmentCreate(CreateView):
    form_class = AssignmentForm
    model = Assignment


class AssignmentUpdate(UpdateView):
    form_class = AssignmentForm
    model = Assignment
    template_name = 'iteminfo/assignment_form_update.html'


class AssignmentDelete(DeleteView):
    model = Assignment
    success_url = reverse_lazy('iteminfo_assignment_list_urlpattern')

    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        return render(
            request,
            'iteminfo/assignment_confirm_delete.html',
            {'assignment': assignment}
        )

