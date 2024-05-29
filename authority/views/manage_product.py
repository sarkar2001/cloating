from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

# class-based view classes
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Permission and Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permissions import AdminPassesTestMixin

# Import Models
from ClothingApp.models import(
    Category,
    SubCategory,
    ProductCategory,
    ProductSize,
    ProductColor,
    PRODUCT
)

# Import Filters
from authority.filters import(
    CategoryFilter,
    SubCategoryFilter,
    ProductCategoryFilter,
    ProductColorFilter,
    ProductSizeFilter,
    ProductListFilter
    
)
   


#Import Forms
from authority.forms import(
    CategoryForm,
    SubCategoryForm,
    ProductCategoryForm,
    ProductColorForm,
    ProductSizeForm,
    ProductFrom
)

#<<----------------- List, Add, Update Category ---------------->>
class CategoryListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = Category.objects.all()
    filterset_class = CategoryFilter
    template_name = 'product/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Category List"
        context["category_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context

class UpdateCategoryView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model= Category
    form_class= CategoryForm
    template_name='product/add_update_category.html'
    success_url= reverse_lazy('authority:category_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Category"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Category Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

class AddCategoryView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'product/add_update_category.html'
    success_url = reverse_lazy('authority:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add category"

        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Category Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

#<<----------------- List, Add, Update Sub-Category ---------------->>   
class SubCategoryListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = SubCategory.objects.all()
    filterset_class = SubCategoryFilter
    template_name = 'product/sub_category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sub-Category List"
        context["category_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context

class UpdateSubCategoryView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model= SubCategory
    form_class= SubCategoryForm
    template_name='product/add_update_sub_category.html'
    success_url= reverse_lazy('authority:sub_category_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Sub-Category"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Sub-Category Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

class AddSubCategoryView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'product/add_update_sub_category.html'
    success_url = reverse_lazy('authority:sub_category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Sub-category"

        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Sub-Category Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)
    
    
#<<----------------- List, Add, Update Product-Category ---------------->>   
class ProductCategoryListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = ProductCategory.objects.all()
    filterset_class = ProductCategoryFilter
    template_name = 'product/product_category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Product Category List"
        context["category_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context

class UpdateProductCategoryView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model= ProductCategory
    form_class=ProductCategoryForm
    template_name='product/add_update_product_category.html'
    success_url= reverse_lazy('authority:product_category_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Product-Category"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Product Category Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

class AddProductCategoryView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'product/add_update_product_category.html'
    success_url = reverse_lazy('authority:product_category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Sub-category"

        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Product Category Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)
    
    
#<<----------------- List, Add, Update Product-Size ---------------->>   
class ProductSizeListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = ProductSize.objects.all()
    filterset_class = ProductSizeFilter
    template_name = 'product/product_size_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Product Size List"
        context["size_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context

class UpdateProductSizeView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model= ProductSize
    form_class=ProductSizeForm
    template_name='product/add_update_product_size.html'
    success_url= reverse_lazy('authority:product_size_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Product Size"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Product Size Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

class AddProductSizeView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = ProductSize
    form_class = ProductSizeForm
    template_name = 'product/add_update_product_size.html'
    success_url = reverse_lazy('authority:product_size_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Product Size"

        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Product Size Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)
    
    
#<<----------------- List, Add, Update Product-Color ---------------->>   
class ProductColorListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = ProductColor.objects.all()
    filterset_class = ProductColorFilter
    template_name = 'product/product_color_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Product Color List"
        context["color_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context

class UpdateProductColorView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model= ProductColor
    form_class=ProductColorForm
    template_name='product/add_update_product_color.html'
    success_url= reverse_lazy('authority:product_color_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Product Color"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Product Color Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

class AddProductColorView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = ProductColor
    form_class = ProductColorForm
    template_name = 'product/add_update_product_color.html'
    success_url = reverse_lazy('authority:product_color_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Product Color"

        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Product Color Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)


#<<--------------------- Add, Update, View Product ---------------------->>
class ProductListView(LoginRequiredMixin, AdminPassesTestMixin, ListView):
    queryset = PRODUCT.objects.all()
    filterset_class = ProductListFilter
    template_name = 'product/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Product List"
        context["product_list"] =  self.filterset_class(self.request.GET, queryset=self.queryset)
        return context



class UpdateProductView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model= PRODUCT
    form_class= ProductFrom
    template_name='product/add_update_product.html'
    success_url= reverse_lazy('authority:product_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Product"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Product Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)

class AddProductView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = PRODUCT
    form_class = ProductFrom
    template_name = 'product/add_update_product.html'
    success_url = reverse_lazy('authority:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Product"

        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Product Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong please try again!")
        return super().form_invalid(form)
