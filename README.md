
# 練習在 github 協作, Mac 使用者
## 0. 在 github 頁面先  Fork 本項目




## 1. 統一由 django-team 目錄開始出發
進入一個乾淨的 terminal
統一在你的根目錄建立 django-team 目錄並進入 
```
pwd
mkdir django-team
cd django-team
pwd
ls -l
```


## 2. 建立工作目錄并 clone 本項目
在你的工作區，新建一個檔案夾 misdj-case001，以後我們稱之為本項目的工作目錄


```
mkdir misdj-case001
cd misdj-case001

# 要 clone 你們剛才 Fork 後自己的。
# git clone https://github.com/<你自己的>/misdj-case001.git 
# 以 Leanne 為例
https://github.com/leanneshen1/misdj-case001.git

cd misdj-case001
pwd
ls -l
git remote -v
cd ..
pwd
ls -l
```

## 3. 建立該項目的虛擬環境
虛擬環境是指 Python3.6 以上的。


```
python3 -m venv venv
pwd
ls -l
```
## 4. 啟用上述虛擬環境並安裝所需
虛擬環境是指 Python3.6 以上的。


```
source venv/bin/activate
pip install -r misdj-case001/requirements.txt
pwd
ls -l
```

## 5.檢查虛擬環境安裝是否正確

使用指令  pip freeze 查看，是否如同以下結果
```
(venv) $ pip freeze
defusedxml==0.6.0
diff-match-patch==20181111
Django==2.2.6
django-import-export==1.2.0
et-xmlfile==1.0.1
jdcal==1.4.1
MarkupPy==1.14
odfpy==1.4.0
openpyxl==3.0.0
pytz==2019.3
PyYAML==5.1.2
sqlparse==0.3.0
tablib==0.14.0
xlrd==1.2.0
xlwt==1.3.0
```

## 6. 確認目前的配置
以 Mac 使用者 為例，pinglingchen 會是你在 Mac 的用戶名
```
pwd
cd ~/django-team
tree -L 2 misdj-case001/
```



到這裡要達到的效果是這樣子的



```
$ pwd
/Users/pinglingchen/django-team
$ tree -L 2 misdj-case001/
misdj-case001/               這是本項目的工作目錄
├── misdj-case001            這是本項目的代碼
│   ├── README.md
│   ├── case001
│   ├── case001-data
│   ├── db.sqlite3
│   ├── go
│   ├── img
│   ├── manage.py
│   ├── misdj
│   ├── misdj-ww-steps-master
│   ├── note
│   ├── others
│   ├── requirements.txt
│   └── sharing
└── venv                     這是本項目的虛擬環境
    ├── bin
    ├── include
    ├── lib
    ├── pip-selfcheck.json
    └── pyvenv.cfg

13 directories, 7 files
```
# jungle123-case002
# jungle123-case002
# jungle123-case002
# jungle123-case003
# jungle123-case005
# tmc
