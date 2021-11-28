from django.urls import path
from . import views
from .views import ArticleListView
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView, 
   ArticleCreateView, 


    RecipeListView,
    RecipeUpdateView,
    RecipeDetailView,
    RecipeDeleteView, 
    RecipeCreateView, 
)

urlpatterns = [
    # Home page and Stripe Urls
    path('', views.index, name='index'),
    path('config/', views.stripe_config),
    path('plan/AshsdhdyyeyDhshshDSGSYTSREWHJejhejej/', views.plans, name="plan"),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),  
    path('cancel/', views.cancel),  
    path('webhook/', views.stripe_webhook),  

    #article Urls
    path('article/<int:pk>/edit/',ArticleUpdateView.as_view(), name='article_edit'), 
    path('article/<int:pk>/',ArticleDetailView.as_view(), name='article_detail'), 
    path('article/<int:pk>/delete/',ArticleDeleteView.as_view(), name='article_delete'),  
    path('article/', ArticleListView.as_view(), name='article_list'),
    path('article/new/', ArticleCreateView.as_view(), name='article_new'),

    #recipe Urls
    path('recipe/<int:pk>/edit/recipe/',RecipeUpdateView.as_view(), name='recipe_edit'), 
    path('recipe/<int:pk>/recipe/',RecipeDetailView.as_view(), name='recipe_detail'), 
    path('recipe/<int:pk>/delete/recipe/',RecipeDeleteView.as_view(), name='recipe_delete'),  
    path('recipe/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/new/recipe/', RecipeCreateView.as_view(), name='recipe_new'),
]