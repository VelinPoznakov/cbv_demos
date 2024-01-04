from django.urls import path

from cbv_demos.web.views import ArticleView, ArticleDetail, ArticleCreate, ArticleDelete

urlpatterns = [
    path('', ArticleView.as_view(), name='article'),
    path('detail/<int:pk>', ArticleDetail.as_view(), name='detail'),
    path('create/', ArticleCreate.as_view(), name='create'),
    path('delete/<int:pk>', ArticleDelete.as_view(), name='delete'),


]
