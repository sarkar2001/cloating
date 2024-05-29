from django.urls import path


app_name='authority'

from authority.views import authority_main
from authority.views import manage_user
from authority.views import manage_product
from authority.views import manage_banner
from authority.views import manage_message
from authority.views import manage_order


urlpatterns = [
    path('admin/', authority_main.AdminView.as_view(), name='authority_admin')
]

#Manage User
urlpatterns += [
    path('user-list/', manage_user.UserListView.as_view(), name='user_list'),
    path('user-update/<int:pk>/', manage_user.EditUserInfoView.as_view(), name='update_user'),
]

#Manage Product
urlpatterns += [
    path('category-list/', manage_product.CategoryListView.as_view(), name='category_list'),
    path('category-update/<int:pk>/', manage_product.UpdateCategoryView.as_view(), name='update_category'),
    path('add-category', manage_product.AddCategoryView.as_view(), name='add_category'),
    
    # Manage Sub-Category
    path('sub-category-list/', manage_product.SubCategoryListView.as_view(), name='sub_category_list'),
    path('sub-category-update/<int:pk>/', manage_product.UpdateSubCategoryView.as_view(), name='update_sub_category'),
    path('add-sub-category', manage_product.AddSubCategoryView.as_view(), name='add_sub_category'),
    
    # Manage Product-Category
    path('product-category-list/', manage_product.ProductCategoryListView.as_view(), name='product_category_list'),
    path('product-category-update/<int:pk>/', manage_product.UpdateProductCategoryView.as_view(), name='update_product_category'),
    path('add-product-category', manage_product.AddProductCategoryView.as_view(), name='add_product_category'),
    
    # Manage Product-Category
    path('product-size-list/', manage_product.ProductSizeListView.as_view(), name='product_size_list'),
    path('product-size-update/<int:pk>/', manage_product.UpdateProductSizeView.as_view(), name='update_product_size'),
    path('add-product-size', manage_product.AddProductSizeView.as_view(), name='add_product_size'),
    
    # Manage Product-Category
    path('product-color-list/', manage_product.ProductColorListView.as_view(), name='product_color_list'),
    path('product-color-update/<int:pk>/', manage_product.UpdateProductColorView.as_view(), name='update_product_color'),
    path('add-color-size', manage_product.AddProductColorView.as_view(), name='add_product_color'),
    
    #Manage Product
    path('product-list/', manage_product.ProductListView.as_view(), name='product_list'),
    path('product-update/<int:pk>/', manage_product.UpdateProductView.as_view(), name='product_update'),
    path('add-product/', manage_product.AddProductView.as_view(), name='add_product'),
    
]

# Manage Slider Banner 
urlpatterns +=[
    path('slider-banner-list/', manage_banner.SliderBannerListView.as_view(), name='banner_image_list'),
    path('update-slider-banner/<int:pk>/', manage_banner.UpdateBannerImageView.as_view(), name='update_banner_image'),
    path('add-slider-banner/', manage_banner.AddBannerImageView.as_view(), name='add_banner_image'), 
]

# Manage About Us 
urlpatterns +=[
    path('about-us-list/', manage_banner.AboutListView.as_view(), name='about_us_list'),
    path('update-about-us/<int:pk>/', manage_banner.UpdateAboutUsView.as_view(), name='update_about_us'),
    path('add-about-us/', manage_banner.AddAboutUsView.as_view(), name='add_about_us'), 
]
# Manage Brand
urlpatterns +=[
    path('brand-list/', manage_banner.BrandListView.as_view(), name='brand_list'),
    path('update-brand/<int:pk>/', manage_banner.UpdateBrandView.as_view(), name='update_brand'),
    path('add-brand/', manage_banner.AddBrandView.as_view(), name='add_brand'), 
]

# Manage Contact Us
urlpatterns +=[
    path('contact-us-list/', manage_banner.ContactUsListView.as_view(), name='contact_us_list'),
    path('update-contact-us/<int:pk>/', manage_banner.UpdateContactUsView.as_view(), name='update_contact_us'),
    path('add-contact-info/', manage_banner.AddContactUsView.as_view(), name='add_contact_us'), 
]

# Manage Contact Us
urlpatterns +=[
    path('message-list/', manage_message.MassageListView.as_view(), name='message_list'),
    path('message-details/<int:pk>/', manage_message.MessageDetailView.as_view(), name='message_details'),
   
]

# Manage Orders
urlpatterns +=[
    path('order-list/', manage_order.OrderListView.as_view(), name='order_list'),
    path('order-details/<int:pk>/', manage_order.OrderDetailView.as_view(), name='order_details'),
   
]


