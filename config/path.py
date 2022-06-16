# 读取所有文件的路径
import os

# 当前文件的路径
config_path = os.path.abspath(__file__)
print(config_path)
# config目录
config_dir = os.path.dirname(config_path)
print(config_dir)
# 获取本项目的路径
root_dir = os.path.dirname(config_dir)
print(root_dir)
# 获取data的目录路径
data_dir = os.path.join(root_dir,'data')
print(data_dir)
if not os.path.exists(data_dir):
    os.mkdir(data_dir)
# yaml文件的配置
config_yaml_path = os.path.join(config_dir,'config.yaml')
# img文件的配置
img_path = os.path.join(root_dir,'img')
if not os.path.exists(img_path):
    os.mkdir(img_path)
