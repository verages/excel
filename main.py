import os
import sys
import glob

from utils import read_excel_content
#主函数入口
def main():
    #获取当前路径
    curPath = os.path.abspath(os.path.dirname(__file__))
    #筛选目录下的 xls 文件和 xlsx 文件
    fileList = glob.glob(curPath + '/*.xls')
    file_list = glob.glob(curPath + '/*.xlsx')
    #合并列表
    fileList.extend(file_list)
    #遍历文件
    for file in fileList:
        #判断文件后缀
        if os.path.splitext(file)[1] == '.xls':
        #读取表头
            head,content = read_excel_content(file)
            # print(head)

if __name__ == '__main__':
    main()