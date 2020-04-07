#_*_coding_:utf-8_*_
# Author：ibell
# Create_time: 2020-04-01 14:36 
# File: do_excel.py

from openpyxl import load_workbook
from project_path import test_data_path,case_config_path
from read_config import ReadConfig
from my_log import MyLogging

class DoExcel:

    def get_data(self,file_name):
        wb=load_workbook(file_name)
        #获取配置信息，获取到的是字符串类型的类似字典格式数据，需要转成字典格式 eg:{"login":"all","withraw":[1,3]}
        mode=eval(ReadConfig().get_config(case_config_path,'MODE','mode'))
        MyLogging().info("获取到的测试用例配置是{}".format(mode))
        test_data=[]


        for sheet_name in mode:
            sheet = wb[sheet_name]
            #该表格中用例需要全部执行,"login":"all"
            if mode[sheet_name]=='all':
                for i in range(2,sheet.max_row+1):
                    row_data = {}
                    row_data['code'] = sheet.cell(i, 1).value
                    row_data['module'] = sheet.cell(i, 2).value
                    row_data['title'] = sheet.cell(i, 3).value
                    row_data['url'] = sheet.cell(i, 4).value
                    row_data['data'] = sheet.cell(i, 5).value
                    row_data['method'] = sheet.cell(i, 6).value
                    row_data['expected'] = sheet.cell(i, 7).value
                    row_data['check_database'] = sheet.cell(i, 8).value
                    row_data['sheet_name'] = sheet_name  ##
                    test_data.append(row_data)
                MyLogging().info("{}的配置是{},获取到的测试数据是{}".format(sheet_name,mode[sheet_name],test_data))


            #执行部分模块的某几条用例"withraw":[1,3]
            else:
                for case_id in mode[sheet_name]:
                    row_data={}
                    row_data['code'] = sheet.cell(case_id+1, 1).value
                    row_data['module'] = sheet.cell(case_id+1, 2).value
                    row_data['title'] = sheet.cell(case_id+1, 3).value
                    row_data['url'] = sheet.cell(case_id+1, 4).value
                    row_data['data'] = sheet.cell(case_id+1, 5).value
                    row_data['method'] = sheet.cell(case_id+1, 6).value
                    row_data['expected'] = sheet.cell(case_id+1, 7).value
                    row_data['check_database'] = sheet.cell(case_id+1, 8).value
                    row_data['sheet_name']=sheet_name  ##写数据到excel需要
                    test_data.append(row_data)



                MyLogging().info("{}的配置是{},获取到的测试数据是{}".format(sheet_name,mode[sheet_name] , test_data))

        # 判断测试用例中，每条case中是否包含占位符
        tel = wb['tel_data'].cell(2, 1).value
        for item in test_data:
            if str(item).find('${tel}') !=-1:
                item['data']=str(item['data']).replace('${tel}',str(tel))
            elif str(item).find('${tel_1}') !=-1:
                item['data']=str(item['data']).replace('${tel_1}',str(tel+1))

        #将手机号更新到表格中
        tel = tel + 1
        self.update_tel(file_name,'tel_data',tel)

        return test_data


    #将返回结果，测试结果写回表格中
    def write_back(self,file_name,sheet_name,row_no,response_result,check_result,test_result):
        wb=load_workbook(file_name)
        sheet=wb[sheet_name]
        sheet.cell(row_no,9).value=response_result
        sheet.cell(row_no,10).value=check_result
        sheet.cell(row_no,11).value=test_result
        wb.save(file_name)

    #更新表格手机号数据
    def update_tel(self,file_name,sheet_name,tel):
        wb=load_workbook(file_name)
        sheet=wb[sheet_name]
        sheet.cell(2,1).value=tel
        wb.save(file_name)



if __name__ == '__main__':
    DoExcel().get_data(test_data_path)
