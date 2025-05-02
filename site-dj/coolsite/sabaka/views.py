from django.shortcuts import render, get_object_or_404
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
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def all_products(request):
    flowers = Flower.objects.filter(is_available=True)
    return render(request, 'all_products.html', {'flowers': flowers})

def flowers_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    flowers = Flower.objects.filter(category=category, is_available=True)
    return render(request, 'flowers_by_category.html', {'category': category, 'flowers': flowers})

# Category CRUD
class CategoryListView(ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'
    paginate_by = 10

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories_delete.html'
    success_url = reverse_lazy('category_list')

class FlowerListView(ListView):
    model = Flower
    template_name = 'flowers_list.html'
    context_object_name = 'flowers'
    paginate_by = 10

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
    paginate_by = 10

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
    paginate_by = 10

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
    paginate_by = 10

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

class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotions_list.html'
    context_object_name = 'promotions'
    paginate_by = 10

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
    paginate_by = 10

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
    paginate_by = 10

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