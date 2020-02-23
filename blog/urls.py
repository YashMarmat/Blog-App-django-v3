from django.urls import path
from .views import(
    BlogList,
    BlogDetail,
    BlogCreate,
    BlogUpdate,
    BlogDelete,
)


urlpatterns = [
    path('', BlogList.as_view(), name = "blog_list"),
    path('blog/<int:pk>', BlogDetail.as_view(), name = "blog_detail"),
    path('blog/new/', BlogCreate.as_view(), name = 'blog_new'), 
    path('blog/<int:pk>/update', BlogUpdate.as_view(), name = 'blog_update'),
    path('blog/<int:pk>/delete', BlogDelete.as_view(), name = 'blog_delete'),
]
