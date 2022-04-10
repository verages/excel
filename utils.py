#读取操作excel文件
import xlrd
#写入操作excel文件
import xlwt

#读取表格内容
def read_excel_content(file):
    #打开文件
    data = xlrd.open_workbook(file)
    #获取全部sheet
    sheet_names = data.sheet_names()
    #遍历sheet获取表头
    for sheet_name in sheet_names:
        #获取sheet
        sheet = data.sheet_by_name(sheet_name)
        #获取表头
        head = sheet.row_values(0)
        print(head)
    table = data.sheets()[0]
    # print(sheet)
    #获取表头
    head = table.row_values(0)
    #获取表格内容
    content = table.col_values(0)
    return head,content
#写入表格内容
def write_excel_content(file,head,content):
    #创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')
    #创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    #写入表头
    for i in range(0,len(head)):
        worksheet.write(0,i,head[i])
    #写入表格内容
    for i in range(0,len(content)):
        worksheet.write(i+1,0,content[i])
    #保存文件
    workbook.save(file) 