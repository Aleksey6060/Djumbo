from django import forms
from .models import Flower, Supplier, Delivery, Review, Promotion, Category

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name', 'description', 'price', 'photo', 'is_available', 'category']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_email', 'phone', 'address']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['name', 'cost', 'estimated_time']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['flower', 'customer_name', 'rating', 'comment']

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['title', 'description', 'discount', 'start_date', 'end_date', 'banner']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }