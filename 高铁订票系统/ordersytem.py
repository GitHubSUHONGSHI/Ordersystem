'''
@时间  : 2022/4/4 19:18
@作者  : 苏大文豪
@FileName: ordersytem.py
'''


'''
... tb = pt.PrettyTable()
>>> tb.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
>>> tb.add_row(["Adelaide",1295, 1158259, 600.5])
>>> tb.add_row(["Brisbane",5905, 1857594, 1146.4])
>>> tb.add_row(["Darwin", 112, 120900, 1714.7])
>>> tb.add_row(["Hobart", 1357, 205556,619.5])
>>> 
>>> print(tb)
'''

import  prettytable as pt
import  os
#创建一个表
# def showtable(row,cloum):
#     tb = pt.PrettyTable()  # 创表
#     tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
#     for i in range(13):
#
#         lit = ['第{}行'.format(i + 1), '有票', '有票', '有票', '有票', '有票']
#         tb.add_row(lit)
#     print(tb)

orderFile = "oderFile"
def show(number):
    # if os.path.exists(orderFile):
    #     if os.path.getsize(orderFile)>0:
    #         pass
    #     pass
    # else:
    #     wfile = open(orderFile,'w',encoding='utf-8')

    #lis = []
    tb = pt.PrettyTable() # 创表
    tb.field_names = ['行号','座位1','座位2','座位3','座位4','座位5']
    # wfile.write(str(['行号','座位1','座位2','座位3','座位4','座位5'])+'\n')
    # pass
    # tb.add_row("1","2","3","4","5")
    for i in range(number):
        lit = ['第{}行'.format(i+1),'有票','有票','有票','有票','有票']
        #创建一个字典
        # d = f'第{i+1}行'
        # print(d)
        # dit = dict(d={'有票','有票','有票','有票','有票'})
        # lis.append(dit)
        #print(lis)
        #wfile.write(str(lit)+'\n')
        tb.add_row(lit)
    print(tb)

# 订票
def order_ticket(row_numb,row,colum):
    l = []
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_numb):
        if int(row) == int(i+1):
            lit = [f'第{i+1}','有票','有票','有票','有票','有票']
            lit[int(colum)] = '\033[0;31m已售\033[m'
            tb.add_row(lit)
            l.append(lit[int(colum)])
            print('--------',l)
        else:
            lit = [f'第{i + 1}', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lit)
    print(tb)

# 用于已经售的高铁票
def  sodl():
    pass
if __name__ == '__main__':
    number = 13
    show(number)
    while True:
        row_lit = input('请输入您要查的座位是否有票，格式如：13,5}: ')
        try:
            row, cloume = row_lit.split(',')
        except:
            print('你输入信息有误')
        order_ticket(number,row,cloume)
        t = input('你是否还继续查询呢 Y/N:')
        if not t:
            print('你输入的数字不规范，请重新输入')
            continue
        if t == 'Y' or t == 'y':
            break
        else:
            continue

