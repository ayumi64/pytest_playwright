import os
from configparser import ConfigParser

#继承导入的ConfigParser类
class myConfig(ConfigParser):
    def __init__(self):
        """
        初始化重构的配置文件类myConfig
        :param filename: config.txt
        """
        #先对父类进行初始化
        super().__init__()
        #获取当前文件的目录(str类型) os.path.dirname()：去掉（）内路径的文件名称部分。 os.path.abspath(__file__)：获取当前文件的绝对路径
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        print("parent_dir：", parent_dir)
        print(type(parent_dir))
        #利用os.path.join()方法连接绝对路径和配置文件，返回config.txt文件的绝对路径(str类型)
        configPath = os.path.join(parent_dir,'common/config.ini')
        print("configPath：", configPath)
        print(type(configPath))
        #读取配置文件，并设置文件编码格式
        self.read(configPath, encoding="utf-8")

if __name__ == "__main__":
    conf = myConfig()
    #myConfig,get(section,key)方法来获得配置文件中的database区块username的值
    userName = conf.get("database", "userName")
    print(userName)