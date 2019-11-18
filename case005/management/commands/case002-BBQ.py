from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count,Sum
# from mach.models import MachTask
from case002.models import Data2

import os
import array
import openpyxl
import statistics as stats

from openpyxl import load_workbook # to read

     # https://openpyxl.readthedocs.io/en/stable/tutorial.html#accessing-one-cell
from openpyxl import Workbook # to write

# 2019-6-15
# 為什麼發現 扣除未流轉，沒能更新到表單？
class Command(BaseCommand):
    help = 'Update Zone19 data'


        
    def handle(self, *args, **options):
        self.stdout.write('to solve BBQ headcnt')
        import os 
        # cwd=os.getcwd() 
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.stdout.write(BASE_DIR)

        src = os.path.join(BASE_DIR, 'src2.txt')
        import re
        # https://stackoverflow.com/questions/7485458/python-reading-text-file            
        def entireList():
            with open(src) as f:
                # [self.stdout.write(line.split()) for line in f]
                for line in f:
                    self.stdout.write('-------')
                    self.stdout.write(line)
                    self.stdout.write('-------')
                    # 51.Inman北京 12月昆山
                    # 取出 51
                    m = re.findall(r'^\d+', line)[0]
                    m_dot = re.findall(r'^\d+\.', line)[0]
                    self.stdout.write(m)
        
                    line2 = line.replace(m_dot,'')
                    
                    # self.stdout.write(line2)
                    okCnt = 0
                    for x in line2.split():
                        self.stdout.write(x)
                        if x == 'OK':
                            okCnt += 1
                    if okCnt == 1:
                        self.stdout.write('已確定，未繳費')
                    if okCnt == 2:
                        self.stdout.write('已繳費')
                        
        def paidList():
            cnt =0 
            with open(src) as f:
                # [self.stdout.write(line.split()) for line in f]
                for line in f:
                    # self.stdout.write('-------')
                    # self.stdout.write(line)
                    # self.stdout.write('-------')
                    # 51.Inman北京 12月昆山
                    # 取出 51
                    m = re.findall(r'^\d+', line)[0]
                    m_dot = re.findall(r'^\d+\.', line)[0]
                    # self.stdout.write(m)
        
                    line2 = line.replace(m_dot,'')
                    
                    # self.stdout.write(line2)
                    okCnt = 0
                    for x in line2.split():
                        # self.stdout.write(x)
                        if x == 'OK':
                            okCnt += 1
                    if okCnt == 2:
                        cnt += 1
                        temp ="("+str(cnt)+") "+ m +"."+ line2.split()[0]
                        self.stdout.write(temp)
                        
                    # if okCnt == 1:
                        # self.stdout.write('已確定，未繳費')
        def goingToPayList():
            cnt =0 
            with open(src) as f:
                # [self.stdout.write(line.split()) for line in f]
                for line in f:
                    # self.stdout.write('-------')
                    # self.stdout.write(line)
                    # self.stdout.write('-------')
                    # 51.Inman北京 12月昆山
                    # 取出 51
                    m = re.findall(r'^\d+', line)[0]
                    m_dot = re.findall(r'^\d+\.', line)[0]
                    # self.stdout.write(m)
        
                    line2 = line.replace(m_dot,'')
                    
                    # self.stdout.write(line2)
                    okCnt = 0
                    for x in line2.split():
                        # self.stdout.write(x)
                        if x == 'OK':
                            okCnt += 1
                    if okCnt == 1:
                        cnt += 1
                        temp ="("+str(cnt)+") "+ m +"."+ line2.split()[0]
                        self.stdout.write(temp)


        def otherList():
            cnt =0 
            with open(src) as f:
                # [self.stdout.write(line.split()) for line in f]
                for line in f:
                    # self.stdout.write('-------')
                    # self.stdout.write(line)
                    # self.stdout.write('-------')
                    # 51.Inman北京 12月昆山
                    # 取出 51
                    m = re.findall(r'^\d+', line)[0]
                    m_dot = re.findall(r'^\d+\.', line)[0]
                    # self.stdout.write(m)
        
                    line2 = line.replace(m_dot,'')
                    
                    # self.stdout.write(line2)
                    okCnt = 0
                    for x in line2.split():
                        # self.stdout.write(x)
                        if x == 'OK':
                            okCnt += 1
                    if okCnt == 0:
                        cnt += 1
                        temp ="("+str(cnt)+") "+ m +"."+ line2
                        self.stdout.write(temp)
        
        entireList()
       
        self.stdout.write('-----------')
        self.stdout.write('已繳費')
        self.stdout.write('-----------')
        paidList()
        self.stdout.write('-----------')
        self.stdout.write('已決定，待繳費')
        self.stdout.write('-----------')
        goingToPayList()
        self.stdout.write('-----------')
        self.stdout.write('其它')
        self.stdout.write('-----------')
        otherList()
                    
       