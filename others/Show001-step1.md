# 增加頁面標準步骤
## url
- 使用 Django 版本 2 起的 path 
    - 根目錄不加 /，直接使用空白。
    - 其它各路徑要加 /。
- 使用 manage.py startapp case001 後，需要手動加 urls.py 檔案
    - 直接複製已有的再行修改
    - 修改 app_name = 'case001'
    - path('/', views.index, name='index'),做為索引

- 在上層的 urls.py，也就是 misdj 的 urls.py 檔案，要加上一個 path
    - path('case001/', include('case001.urls')), 



## view
- 基本上使用 template
    - 再進階時，也會不使用 template

## template
- 在同樣風格時要有基礎模板，通常命名為 base.html。
- 如果展示的格式一樣，可以共用模板。
    - 在不同頁面重覆出現的格式，可以先做成一個組件以供調用。

