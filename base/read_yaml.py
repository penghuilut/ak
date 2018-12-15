import os

import yaml

class ReadYaml():
    def __init__(self,filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename

    def read_yaml(self):
        with open(self.filename,"r",encoding="utf-8") as f:
            return yaml.load(f)

    def read_yaml_1(self):
        with open('../data/data_login.yaml',"r",encoding="utf-8") as f:
            return yaml.load(f)

if __name__ == '__main__':
    # 获取所有的数据
    datas = ReadYaml("lk").read_yaml_1()
    print(datas)
# 创建空列表
    arrs =[]
    # 获取所有的值并遍历
    for data1 in datas.values():
        arrs.append((data1.get("username"),data1.get("password")))
        print(arrs)
