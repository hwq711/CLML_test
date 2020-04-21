from django.urls import path, re_path
# 导入 myapp 应用的 views 文件
from . import views

urlpatterns = [
    re_path(r'save_data$', views.save_data),   # 存数据到数据库
    re_path(r'search_drug$', views.search_drug)   # 查询与drug相关联的
]