
from django.conf.urls import url
from .views import index,list,detail,deletehero,deletebook,addhero

#这个app_name是一个键（封装起来了），名字不能随便写，后面的值必须和项目路由文件夹下面的应用路由
#名字一致
app_name='booktest'

urlpatterns=[
    url(r'list/',list,name='list'),
    url(r'detail/(\d+)/$',detail,name='detail'),
    url(r'^$',index,name='index'),
    url('^deletehero/(\d+)/$', deletehero, name='deletehero'),
    url('^deletebook/(\d+)/$',deletebook,name='deletebook'),


    #添加英雄
    url('^addhero/(\d+)/$',addhero,name='addhero')
]