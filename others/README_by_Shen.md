https://www.cnblogs.com/sunnydou/p/5801760.html

## pip freeze 的結果如下
```
(venv) leanneshendeMacBook-Air:ww leanneshen$ pip freeze
backports.csv==1.0.7
defusedxml==0.6.0
diff-match-patch==20181111
Django==2.2.6
django-import-export==1.2.0
et-xmlfile==1.0.1
jdcal==1.4.1
odfpy==1.4.0
openpyxl==3.0.0
pytz==2019.3
PyYAML==5.1.2
sqlparse==0.3.0
tablib==0.13.0
xlrd==1.2.0
xlwt==1.3.0

```

## 我的工作目錄是  pwd
```
(venv) leanneshendeMacBook-Air:ww leanneshen$ pwd
/Users/leanneshen/misdj/ww

```

## 新建  app, ./manage.py startapp case001
```
(venv) leanneshendeMacBook-Air:misdj005-master leanneshen$ ./manage.py startapp case001

```


## 20191119 工作环境设定及遇到的问题

1. 本地代码上传
  
  a. 在本地代码与GitHub两边内容一模一样时，尝试终端五步上传，系统则提示没有可更新内容

![Step1](img/01_上传.png)


  b. 尝试在本地READme中添加文字“进度大纲”后重新上传，则提示有更新

![Step2](img/02_上传.png)

2. 命令确认好后，到服务器端确认之前可以运行的 http://127.0.0.1:8000/ww2 是否可正常运行

  a. 运行失败，显示错误信息如下:
  
 ![Step3](img/03_运行ww2.png)
 
  b. 经过确认，发现目前使用的Django版本是1.8.19
  
 ![Step4](img/04_pipfreeze.png)
  
  c. 重新安装 pip install django
             pip install django-import-export
     后运行 pip freeze 结果如下
     
 ![Step5](img/05_pipreeze.png)
 
  d. 确认版本正确后，重新确认服务器端http://127.0.0.1:8000/ww2 的运行情况

 ![Step6](img/04_运行ww2.png)
 
3. 在本地编译器ww目录下添加img文件夹，用来存放本地需要上传的图片
 
 ![Step7](img/06_addimg.png)
 
4. 新建  app, ./manage.py startapp case001
   在case001/models 下添加
```
from django.db import models
class Data1(models.Model):
    date1 = models.DateField()
    place = models.CharField(max_length=100)
    worker = models.CharField(max_length=100)
    thing = models.CharField(max_length=100)
```
  ![Step8](img/07_createcase01.png)
  
    在case001/admin 下添加
```
from django.contrib import admin

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Data1

class Data1Resource(resources.ModelResource):
    class Meta:
        model = Data1

class Data1Admin(ImportExportModelAdmin):
    resource_class = Data1Resource
    list_display = ('date1','place', 'worker','thing')
    list_filter = ['place','worker']
    search_fields = ['date1','thing']
   
admin.site.register(Data1, Data1Admin)
```
  ![Step9](img/08_createcase01.png)
  
 
5. 在终端运行
```
./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic
./manage.py runserver

ls -l
cat go
```
![Step10](img/09_catgo.png)

6. 在note/urls目录下增加附录
```
 # NOTE: 根目录不必 /
 # path('/', views.index, name='index'),
```
![Step11](img/10_增加附录.png)

7. Timezone

 a. 回到终端检查，发现Timezone时区有错误

![Step12](img/11_timezone.png)

 b. 检查misdj/settings
```
将TIME_ZONE修改成 TIME_ZONE = 'Asia/Shanghai'
```
![Step12](img/12_timezone.png)

 c. 修改完成后确认确认终端时间，已变成正确时区
 
![Step13](img/13_timezone.png)

## Excel数据导入

1. 登录http://127.0.0.1:8000/admin

![Step14](img/14_dataimport.png)

2. 将需要上传Excel格式数据放到本地 misdj005-master目录下

![Step15](img/15_dataimport.png)

3. 将需要上传Excel格式数据放到本地 misdj005-master目录下

![Step15](img/15_dataimport.png)

4. 点击【导入】按钮选择需要导入的Excel，成功导入后，数据总笔数为：4983笔

![Step16](img/16_dataimport.png)

5. 点击右边过滤器【112园】即可查询出所有112园的具体人天数量

![Step17](img/17_dataimport.png)

6. 还可以在搜索框中录入月份，查询给定月份的每天具体人天数量
   
   以此数据为例，17园在2019-07总计有395人天

![Step18](img/18_dataimport.png)
![Step19](img/19_dataimport.png)

 从下表中可以找到对应的395人天的数据，也可作为交互确认
![Step20](img/20_dataimport.png)

 



# misdj-case001
