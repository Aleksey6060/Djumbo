from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from .forms import *

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def how_to_find(request):
    return render(request, 'how_to_find.html')

def categories(request):
    return render(request, 'categories.html')

def all_products(request):
    flowers = Flower.objects.filter(is_available=True)
    return render(request, 'all_products.html', {'flowers': flowers})


class FlowerListView(ListView):
    model = Flower
    template_name = 'flowers_list.html'
    context_object_name = 'flowers'

class FlowerDetailView(DetailView):
    model = Flower
    template_name = 'flowers_detail.html'
    context_object_name = 'flower'

class FlowerCreateView(CreateView):
    model = Flower
    form_class = FlowerForm
    template_name = 'flowers_form.html'
    success_url = reverse_lazy('flower_list')

class FlowerUpdateView(UpdateView):
    model = Flower
    form_class = FlowerForm
    template_name = 'flowers_form.html'
    success_url = reverse_lazy('flower_list')

class FlowerDeleteView(DeleteView):
    model = Flower
    template_name = 'flowers_delete.html'
    success_url = reverse_lazy('flower_list')


class SupplierListView(ListView):
    model = Supplier
    template_name = 'suppliers_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'suppliers_detail.html'
    context_object_name = 'supplier'

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'suppliers_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'suppliers_delete.html'
    success_url = reverse_lazy('supplier_list')


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'deliveries_list.html'
    context_object_name = 'deliveries'

class DeliveryDetailView(DetailView):
    model = Delivery
    template_name = 'deliveries_detail.html'
    context_object_name = 'delivery'

class DeliveryCreateView(CreateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'deliveries_form.html'
    success_url = reverse_lazy('delivery_list')

class DeliveryUpdateView(UpdateView):
    model = Delivery
    form_class = DeliveryForm
    template_name = 'deliveries_form.html'
    success_url = reverse_lazy('delivery_list')

class DeliveryDeleteView(DeleteView):
    model = Delivery
    template_name = 'deliveries_delete.html'
    success_url = reverse_lazy('delivery_list')


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews_detail.html'
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews_form.html'
    success_url = reverse_lazy('review_list')

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews_form.html'
    success_url = reverse_lazy('review_list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'reviews_delete.html'
    success_url = reverse_lazy('review_list')

# Promotion CRUD
class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotions_list.html'
    context_object_name = 'promotions'

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'promotions_detail.html'
    context_object_name = 'promotion'

class PromotionCreateView(CreateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotions_form.html'
    success_url = reverse_lazy('promotion_list')

class PromotionUpdateView(UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotions_form.html'
    success_url = reverse_lazy('promotion_list')

class PromotionDeleteView(DeleteView):
    model = Promotion
    template_name = 'promotions_delete.html'
    success_url = reverse_lazy('promotion_list')


class ShopListView(ListView):
    model = Shop
    template_name = 'shops_list.html'
    context_object_name = 'shops'

class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shops_detail.html'
    context_object_name = 'shop'

class ShopCreateView(CreateView):
    model = Shop
    template_name = 'shops_form.html'
    fields = ['name', 'address', 'phone', 'email', 'working_hours']
    success_url = reverse_lazy('shop_list')

class ShopUpdateView(UpdateView):
    model = Shop
    template_name = 'shops_form.html'
    fields = ['name', 'address', 'phone', 'email', 'working_hours']
    success_url = reverse_lazy('shop_list')

class ShopDeleteView(DeleteView):
    model = Shop
    template_name = 'shops_delete.html'
    success_url = reverse_lazy('shop_list')


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employees_form.html'
    fields = ['name', 'position', 'shop']
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employees_form.html'
    fields = ['name', 'position', 'shop']
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees_delete.html'
    success_url = reverse_lazy('employee_list')

